# Apps and books metadata for organizations

**Framework**: Device Management

Get metadata for apps and books your organization owns.

#### Overview

Use the Apps and Books Metadata for Organizations API to retrieve metadata for apps and books that your organization owns, or to search for and retrieve metadata for apps and books in the public catalog.

This API requires authentication that you’re a member of the Apple Developer Program and a trusted developer. Each request requires a signed developer token as a header. Requests for apps and books your organization owns also require your organization’s `sToken` as a cookie.

## Topics

### Getting started
- [Generating developer tokens](generating-developer-tokens.md)
  Create a JSON Web Token to authorize your requests to the Apps and Books Metadata for Organizations API.
- [Common objects](common-objects.md)
  Understand the common JSON objects that framework responses contain.
### Handling requests
- [Handling requests and responses](handling-requests-and-responses.md)
  Write a request for app or book metadata and handle responses from the API.
### Interpreting responses
- [object ResourceCollectionResponse](resourcecollectionresponse.md)
  A response that contains the resource objects for the request.
- [object ResultsResponse](resultsresponse.md)
  A response that contains the resource objects for the request.
- [object AppsResponse](appsresponse.md)
  A response that contains the resource objects for the request.
- [object BooksResponse](booksresponse.md)
  A response that contains the resource objects for the request.
- [object UnauthorizedResponse](unauthorizedresponse.md)
  A response that indicates an incorrect authorization header.
- [object ErrorsResponse](errorsresponse.md)
  The collection of errors that occurred while processing the request.
### Fetching information
- [Fetching resources with extended attributes](fetching-resources-with-extended-attributes.md)
  Specify additional attributes for the API to include in a response.
- [Fetching storefront objects](fetching-storefront-objects.md)
  Pick a region-specific geographic location to retrieve catalog information from.
### Retrieving app and book metadata
- [Get Metadata for Your Authenticated Purchases](get-v1-catalog-_storefront_-stoken-authenticated-purchases.md)
  Fetch metadata for your authenticated purchases by using their identifiers with a specified resource type.
- [Get Metadata for Your Apps](get-your-apps-metadata.md)
  Fetch metadata for your apps by using their identifiers.
- [Get Metadata for Your Books](get-your-books-metadata.md)
  Fetch metadata for your books by using their identifiers.
- [Get Metadata for a Catalog App](get-v1-catalog-_storefront_-apps-_id_.md)
  Fetch metadata for an app from the catalog by using its identifier.
- [Get Metadata for Multiple Catalog Apps](get-v1-catalog-_storefront_-apps.md)
  Fetch metadata for apps from the catalog by using their identifiers.
- [Get Metadata for a Catalog Book](get-v1-catalog-_storefront_-books-_id_.md)
  Fetch metadata for a book from the catalog by using its identifier.
- [Get Metadata for Multiple Catalog Books](get-v1-catalog-_storefront_-books.md)
  Fetch metadata for books from the catalog by using their identifiers.
- [Get Catalog Search Results](get-catalog-search-results.md)
  Fetch metadata for apps, books, and subscriptions from the catalog by using a search term.
### Fetching relationships
- [Fetch a apps resource's relationship](fetch-a-apps-resource's-relationship.md)
- [Fetch a books resource's relationship](fetch-a-books-resource's-relationship.md)
- [object RelationshipResponse](relationshipresponse.md)
### Fetching genres
- [Get Multiple Genres](get-multiple-genres.md)
  Fetch metadata for genres from the catalog by using their identifiers.
- [Get a Genre](get-a-genre.md)
  Fetch metadata for a genre from the catalog by using its identifier.

## See Also

- [Getting started with the management API](getting-started-with-the-management-api.md)
  Configure your MDM client to handle content and user assignments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apps-and-books-metadata-for-organizations)*