# Storefronts and Localization

**Framework**: Apple Music API

Pick a region-specific geographic location from which to retrieve catalog information, or retrieve information from the user’s personal library.

#### Overview

Apple Music is a worldwide service that operates in many countries, regions, and languages. Content varies from one geographic region to another, so each request must contain a . Storefront defines the desired region and the supported languages for that region. For most requests, you specify the storefront associated with the current user, but you may also specify other storefronts as needed. For example, you might specify a storefront that better matches the user’s preferred language.

Each storefront has a default language, and may support one or more additional languages. For example, the United States storefront includes American English as the default language, but also includes Mexican Spanish as an additional supported language. Apple Music automatically localizes responses using the storefront’s default language, but you can localize to a different language using the `l query` parameter. The value of that parameter must be one of the values in the `supportedLanguageTags` attribute of the storefront object. For example, the following request asks the US storefront to return an album in the Mexican Spanish (`es-MX`) localization.

```other
GET https://api.music.apple.com/v1/catalog/us/albums/310730204?l=es-MX
```

## Topics

### Requesting a Catalog Storefront
- [Get a Storefront](get-a-storefront.md)
  Fetch a single storefront by using its identifier.
- [Get Multiple Storefronts](get-multiple-storefronts.md)
  Fetch one or more storefronts by using their identifiers.
- [Get All Storefronts](get-all-storefronts.md)
  Fetch all the storefronts in alphabetical order.
### Localization
- [Get the best supported language for a storefront](get-the-best-supported-language-based-on-the-acceptlanguage.md)
  Fetch the best supported language for a storefront from a list.
### Handling the Response
- [object Storefronts](storefronts.md)
  A resource object that represents a storefront, an Apple Music and iTunes Store territory that the content is available in.

## See Also

- [Generating Developer Tokens](generating-developer-tokens.md)
  Generate a developer token needed to make requests to Apple Music API.
- [User Authentication for MusicKit](user-authentication-for-musickit.md)
  Authenticate requests for user data using the Music User Token.
- [Handling Requests and Responses](handling-requests-and-responses.md)
  Write a request and handle responses from the API.
- [Handling Resource Representation and Relationships](handling-resource-representation-and-relationships.md)
  Fetch resources with extended attributes and included relationships and relationship views.
- [Common Objects](common-objects.md)
  Understand the common JSON objects that framework responses contain.
- [Managing Content Ratings, Alternate Versions, and Equivalencies](managing-content-ratings-alternate-versions-and-equivalencies.md)
  Handle multiple and alternate versions of content.
- [Fetching Resources by Page](fetching-resources-by-page.md)
  Use pagination to fetch the next set of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/storefronts-and-localization)*