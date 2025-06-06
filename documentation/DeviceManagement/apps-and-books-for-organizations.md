# Apps and Books for Organizations

**Framework**: Device Management

Get details about apps and books to show to your users.

#### Overview

Use the Apps and Books for Organizations API to retrieve metadata for apps and books that your organization owns, or to search for and retrieve metadata for apps and books in the public catalog.

This API requires authentication that you’re a member of the Apple Developer Program and a trusted developer. Each request requires a signed developer token as a header. Requests for apps and books your organization owns also require your organization’s `sToken` as a cookie.

## Topics

### Essentials
- [Generating developer tokens](generating-developer-tokens.md)
  Create a JSON Web Token to authorize your requests to the Apps and Books for Organizations API.
- [Handling requests and responses](handling-requests-and-responses.md)
  Write a request for app or book metadata and handle responses from the API.
- [Fetching resources with extended attributes](fetching-resources-with-extended-attributes.md)
  Specify additional attributes for the API to include in a response.
- [Fetching storefront objects](fetching-storefront-objects.md)
  Pick a region-specific geographic location to retrieve catalog information from.
- [Common Objects](common-objects.md)
  Understand the common JSON objects that framework responses contain.
### App and book metadata
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
  Fetch metadata for apps and books from the catalog by using a search term.

## See Also

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
  Associate app and book purchases with users or devices.
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)
  Manage devices and content across your organization using the new API version.
- [Managing Assets](managing-assets.md)
  Retrieve key information to effectively manage assets across an organization’s users and devices.
- [Managing Users](managing-users.md)
  Retrieve key information to effectively manage users across an organization.
- [Using Paginated Endpoints](using-paginated-endpoints.md)
  Manage paginated endpoints to efficiently work with large record sets.
- [Subscribing to Notifications](subscribing-to-notifications.md)
  Listen to notifications to keep track of the latest events for an organization.
- [Handling Error Responses](handling-error-responses.md)
  Investigate service request errors and troubleshoot solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apps-and-books-for-organizations)*