# Building a searchable catalog for your marketplace app for inclusion in Spotlight

**Framework**: App Store Connect API

Set up and build your alternative marketplace’s searchable index.

#### Overview

Apple builds an index of alternative marketplace apps in order to integrate them into Spotlight. You can set up a catalog of your applications so the Applebot web crawler discovers, indexes, and then shows your apps as Spotlight results on iOS. You must implement this interface to be part of search results in Spotlight.

##### Understand Basic Requirements

The application catalog-crawling mechanism is based on two standard industry practices: [`sitemaps`](https://developer.apple.comhttps://sitemaps.org) and semantic, [`structured data schemas`](https://developer.apple.comhttps://schema.org).

App developers for alternative marketplaces need to maintain a web presence, which means being reachable over the web, and use App Store Connect API to submit the URL of a root sitemap. To learn more see, [`Add a marketplace search detail URL`](post-v1-marketplacesearchdetails.md). Apple uses the root sitemap for further URL discovery and traverses subsequent sitemaps when a catalog is large enough to need fragmentation, or directly uses application URLs. Each application URL needs to return an HTML document enriched with structured data annotated in accordance with schema.org’s schemas, specifically the `MobileApplication` type. Apple defines which fields must be populated using a mixture of standard fields and additional proprietary properties specified using the `supportingData` field, which is described below.

Here’s an example catalog with two applications – an app called Backyard Birds, and another called Camping App:

```other
example.com
  /crawler-site
     |
     | - sitemap.xml
     | - apps -
                   | - backyard-birds.html
                   | - camping-app.html
```

The following items are required for the alternative marketplace:

- Enable SSL.
- Serve the sitemap and app pages from the same hostname (`example.com` in the example). If you intend to operate two marketplaces, you need to use two hostnames, for example `www.example.com` and `www.example2.com`.
- Render structured data schema server-side. The schema must not require any client-side JavaScript processing.

> **Note**:  Apple infers the hostname from the root sitemap URL you configure by using [`Add a marketplace domain`](post-v1-marketplacedomains.md).

 Apple infers the hostname from the root sitemap URL you configure by using [`Add a marketplace domain`](post-v1-marketplacedomains.md).

The marketplace submits the sitemap URL to App Store Connect with [`Add a marketplace search detail URL`](post-v1-marketplacesearchdetails.md).

The sitemap is the root file where Applebot start its crawl and then it proceeds to the application URLs.

Here’s an example sitemap:

```other
curl -X GET https://example.com/apps/sitemap.xml 

<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
   <url>
      <loc>https://example.com/apps/catalog/backyard-birds.html</loc>
      <lastmod>2023-06-20</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.8</priority>
   </url>
   <url>
      <loc>https://example.com/apps/catalog/camping-app.html</loc>
      <lastmod>2023-07-10</lastmod>
      <changefreq>daily</changefreq>
      <priority>0.8</priority>
   </url>
</urlset> 
```

The [`Applebot`](https://developer.apple.comhttps://support.apple.com/en-us/HT204683) web crawler fetches the list of URLs present in the sitemap and crawls them all. Each URL needs to point to an HTML document that contains structured data schemas that include essential information about the content using the [`JSON-LD format.`](https://developer.apple.comhttps://json-ld.org)

> **Note**:  If you have catalog discovery issues contact [`applebot@apple.com`](https://developer.apple.commailto://applebot@apple.com) for assistance.

 If you have catalog discovery issues contact [`applebot@apple.com`](https://developer.apple.commailto://applebot@apple.com) for assistance.

Here’s an example markup:

```other
curl -X GET https://example.com/apps/catalog/backyard-birds.html

<!DOCTYPE html>
<html>
<head>

<!-- This document applies to app version v0.0.1. -->
<script type="application/ld+json"> 
  {
    "@context": "https://schema.org/",
    "@type": "MobileApplication",
    "datePublished": "2024-02-20T11:01:11Z",
    "countriesSupported": ["PL", "FR"],
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 4.8,
        "reviewCount": 2381453,
        "bestRating": 5,
        "worstRating: 1"
    },
    "supportingData": {
      "@type": "DataFeed",
      "dataFeedElement": [
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.appleItemId",
          "value": "6448401697"
        },
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.appleVersionId",
          "value": "173757332"
        },
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.ranking.popularity", 
          "value": 26.48
        }
      ]
    }
  }
</script>

<!-- This document applies to app version v0.0.2 - note the different appleVersionId. -->
<script type="application/ld+json"> 
  {
    "@context": "https://schema.org/",
    "@type": "MobileApplication",
    "datePublished": "2024-02-21T09:45:01Z",
    "countriesSupported": ["PL", "FR"],
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 4.5,
        "reviewCount": 238153,
        "bestRating": 5,
        "worstRating": 1
    },
    "supportingData": {
      "@type": "DataFeed",
      "dataFeedElement": [
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.appleItemId",
          "value": "6448401697"
        },
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.appleVersionId",
          "value": "2347437814"
        },
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.ranking.popularity", 
          "value": 22.12
        }
      ]
    }
  }
</script>

<!-- This document applies to app version v0.0.3 - note the different appleVersionId, some ranking signals also changed. -->
<script type="application/ld+json"> 
  {
    "@context": "https://schema.org/",
    "@type": "MobileApplication",
    "datePublished": "2024-02-22T06:19:45Z",
    "countriesSupported": ["PL", "FR"],
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": 3.5,
        "reviewCount": 2814,
        "bestRating": 5,
        "worstRating": 1
    },
    "supportingData": {
      "@type": "DataFeed",
      "dataFeedElement": [
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.appleItemId",
          "value": "6448401697"
        },
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.appleVersionId",
          "value": "2347437815"
        },
        {
          "@type": "PropertyValue",
          "name": "com.apple.alternativeDistribution.search.ranking.popularity", 
          "value": 15.32
        }
      ]
    }
  }
</script>
</head>

<body>
<h1>Backyard Birds</h1>
<p>Identify the birds in your backyard!</p>
<p>Category: utility</p>
</body>

</html>
```

##### Include Mandatory Fields

These fields are the exact and only fields that are mandatory for `MobileApplication`. For more information see [`supportingData`](https://developer.apple.comhttps://schema.org/supportingData).

| Field name | Name in code | Type | Note |
| --- | --- | --- | --- |
| App Apple ID | `com.apple.alternativeDistribution.search.appleItemId` | `string` | You can find this value in the alternative distribution package’s manifest.json under the key `appleItemId.` |
| Apple Version ID | `com.apple.alternativeDistribution.search.appleVersionId` | `string` | You can find this value in the alternative distribution package’s manifest.json under the key `appleVersionId`. |
| Date published | `datePublished` | `string` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) following the [`ISO 8601`](https://developer.apple.comhttps://www.iso.org/iso-8601-date-and-time-format.html) standard, in the format `YYYY-MM-DDThh:mm:ssZ` | The UTC timestamp at which time the app version published on the marketplace. |

> **Note**:  For each version of your app, provide all the fields contained in `supportingData` in a single instance of `supportingData` that wraps all of them.

 For each version of your app, provide all the fields contained in `supportingData` in a single instance of `supportingData` that wraps all of them.

##### Consider Optional Fields

Optionally, every instance  define additional ranking signals to facilitate surfacing the best results. These signals use [`structured data schemas`](https://developer.apple.comhttps://schema.org)’s `aggregateRating`, which is an app-rating value, together with the total review count and the rating range. The widest supported rating range is from 0 to 100. When using `aggregateRating`, all four properties are mandatory. For more information see [`aggregateRating`](https://developer.apple.comhttps://schema.org/aggregateRating).

| Property name | Name in code | Type | Note |
| --- | --- | --- | --- |
| Aggregate rating | `aggregateRating` | `object` | This object is not in `supportingData` object. All four fields are mandatory. For more information, see the next table. |
| Country supported | `countriesSupported` | `array` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) 2-letter country codes as defined per [`ISO 3166-1 alpha-2`](https://developer.apple.comhttps://www.iso.org/obp/ui/#search/code/) | You can use this array to filter the availabilty of apps per country for Spotlight. |
| Popularity | `com.apple.alternativeDistribution.search.ranking.popularity` | `float, 0` to `100` | A higher number means a more popular app, that gives a notion of popularity in an alternative marketplace by comparing apps within a specific marketplace. |

This table shows details for the `AggregateRating` properties:

| Property name | Name in code | Type | Note |
| --- | --- | --- | --- |
| Rating value | `ratingValue` | `float` | The overall average rating |
| Review Count | `reviewCount` | `integer` | The count of total reviews of the app |
| Best rating | `bestRating` | `integer`, 0 to 100 | The single best rating of the app |
| Worst rating | `worstRating` | `integer`, 0 to 100 | The single worst rating of the app |

This example shows the `popularity` property as part of the `supportingData` code block:

```other
"supportingData": {
    "@type": "DataFeed",
    "dataFeedElement": [
        {
            "@type": "PropertyValue",
            "name": "com.apple.alternativeDistribution.search.ranking.popularity",
            "value": 15.32
        }
    ]
}
```

##### Understand Supported Countries

Searchabilty for apps distributed on alternative marketplaces has two approaches: Applebot web crawler uses `countriesSupported`, while [`MarketplaceKit`](https://developer.apple.com/documentation/MarketplaceKit) uses `searchTerritory`.

`countriesSupported` is an array that contains a list of 2-letter country codes as defined by [`ISO 3166-1 alpha-2`](https://developer.apple.comhttps://www.iso.org/obp/ui/#search). Use these codes to filter the availabilty of an app per country for search. You’re responsible for setting an optional territory as necessary inside your marketplace app. To learn more about territory support, see the MarketplaceKit property `searchTerritory`.

When someone searchs inside Lookup, Safari, or Spotlight, the request context contains the territory, which you set through the `setSearchTerritory` instance method on `AppLibrary`.

For this example, the user searches for outdoor apps. There are three apps that match the query in the table below. The user is in France, `territory: FR,` so Spotlight returns the two apps that match `countriesSupported.` In this example Spotlight returns Camping App and Forest Explorer.

| App name | Countries supported |
| --- | --- |
| Backyard Birds | `PL, IT` |
| Camping App | `PL, FR` |
| Forest Explorer | `DE, FR` |

## See Also

- [Add a marketplace search detail URL](post-v1-marketplacesearchdetails.md)
  Add a search detail URL for the alternative marketplace.
- [Read the marketplace search detail URL](get-v1-apps-_id_-marketplacesearchdetail.md)
  Get search detail URL for the alternative marketplace.
- [Modify a marketplace search detail URL](patch-v1-marketplacesearchdetails-_id_.md)
  Update the search detail URL for the alternative marketplace.
- [Delete a marketplace search detail URL](delete-v1-marketplacesearchdetails-_id_.md)
  Delete search detail URL for the alternative marketplace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight)*