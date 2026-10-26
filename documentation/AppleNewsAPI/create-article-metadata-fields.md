# Create Article Metadata Fields

**Framework**: AppleNewsAPI  
**Kind**: dictionary  
**Role**: Object

See the optional metadata fields for the Create an Article Request.

**Availability**:
- Apple News API 1.0+

## Declaration

```
object Create Article Metadata Fields
```

## Mentions

- [Apple News API Release Notes](../AppleNews/apple-news-api-release-notes.md)
- [Publishing an Article](../AppleNews/publishing-an-article.md)

## Properties

- `accessoryText` (string) *(deprecated)*: The text to include below the article excerpt in the channel view, such as a `byline` or `category` label.

  **Default**: `metadata.authors`; **Maximum Length**: `100`
- `isCandidateToBeFeatured` (boolean): A Boolean that indicates whether this article should be considered for featuring in Apple News.

  **Default**: `false`
- `isHidden` (boolean): A Boolean that indicates whether the article should be temporarily hidden from display in feeds in Apple News. Note that a hidden article is accessible if you have a direct link to the article.

  **Default**: `false`
- `isPreview` (boolean): A Boolean that indicates whether this article should be public (live) or should be a preview that’s only visible to members of your channel. Set `isPreview` to `false` to publish the article immediately and make it visible to all News users.

  If your channel hasn’t yet been approved to publish articles in Apple News Format, setting `isPreview` to `false` results in an `ONLY_PREVIEW_ALLOWED` error.

  **Default**: `false`
- `isSponsored` (boolean): A Boolean that indicates whether this article consists of sponsored content for promotional purposes. You must mark sponsored content as such; channels that don’t follow this policy may be suspended.

  When using `isSponsored`, if you don’t want the sponsored article to appear in your channel’s feed, set sections to `[]` (an empty array).

  **Default**: `false`
- `links` (ArticleLinksRequest): The section links for the article.
- `maturityRating` (string): A string that indicates the viewing audience for the content.

  `MATURE` indicates explicit content that’s only appropriate for a specific audience.

  By default, the article inherits the value you set for your channel in News Publisher.

  **Default**: `null`; **Allowed Values**: `KIDS`, `MATURE`, `GENERAL`
- `targetTerritoryCountryCodes` ([string]): The target country codes required for publishing the article. You must enable the specified country codes in your channel. For example, to publish an article only in the United Kingdom and Australia, specify `GB` and `AU`. By default, an article inherits the channel’s territories.

  Country codes must be in ISO 3166-1 alpha-2 code format; for example, `AU` for Australia. For a complete list of ISO country codes, see [App Store Territories](https://help.apple.com/app-store-connect/#/dev997f9cf7c).

  If you specify a country code that isn’t defined in your channel, the  `ARTICLE_TERRITORY_NOT_ALLOWED` error is generated. If you specify an invalid country code, the server generates an `INVALID_ARTICLE_TERRITORY` error.

## See Also

### Articles
- [Create an Article](./post-channels-_channelid_-articles.md)
  Publish an article to your channel.
- [Read Article Information](./get-articles-_articleid_.md)
  Retrieve information about an article, such as the revision number and maturity rating.
- [Search Articles in a Channel](./get-channels-_channelid_-articles.md)
  See a list of all articles in a channel that match the specified search criteria.
- [Search Articles in a Section](./get-sections-_sectionid_-articles.md)
  See a list of all articles in a section that match the specified search criteria.
- [Update an Article](./post-articles-_articleid_.md)
  Update an existing article in your channel.
- [Delete an Article](./delete-articles-_articleid_.md)
  Delete the specified article from your channel.
- [object ArticleLinksRequest](./articlelinksrequest.md)
  See the required field for the Create an Article request.
- [object Update Article Metadata Fields](./update-article-metadata-fields.md)
  See the metadata fields for the Update an Article request.
- [object Article](./article.md)
  See the fields the article endpoints returned.
- [object ArticleResponse](./articleresponse.md)
  See which objects make up the Create an Article, Read an Article, and Update an Article responses.
- [object ArticleLinksResponse](./articlelinksresponse.md)
  See the links the article endpoints returned.
- [object SearchResponse](./searchresponse.md)
  See the fields the search article endpoints returned.
- [object Meta](./meta.md)
  See the object that wraps the throttling information that’s returned for the Create an Article and Read an Article endpoints.
- [object Throttling](./throttling.md)
  See the object that wraps the throttling information that’s returned for the Create an Article and Update an Article endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/create-article-metadata-fields)*