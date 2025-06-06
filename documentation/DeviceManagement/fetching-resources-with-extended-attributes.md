# Fetching resources with extended attributes

**Framework**: Device Management

Specify additional attributes for the API to include in a response.

#### Overview

You may want to access some attributes that the server doesn’t fetch unless specifically requested. By default, responses contain only a subset of the available attributes for a resource. The attributes that the server doesn’t fetch by default are known as . Use the `extend` query parameter to request a set of additional attributes for a resource type.

For example, when fetching an apps resource, you can request that the server add the extended `latestVersionInfo` attribute to the other attributes it returns:

```other
GET https://api.ent.apple.com/v1/catalog/{storefront}/stoken-authenticated-apps?ids=1376597908,2001350931&platform=iphone&extend[apps]=latestVersionInfo
```

Available extended attributes include:

- `fileSizeByDevice`
- `languageList`
- `description`
- `latestVersionInfo`
- `privacyPolicyUrl`
- `screenshotsByType`
- `supportURLForLanguage`
- `versionHistory`
- `websiteUrl`
- `requirementsByDeviceFamily`

## See Also

- [Generating developer tokens](generating-developer-tokens.md)
  Create a JSON Web Token to authorize your requests to the Apps and Books for Organizations API.
- [Handling requests and responses](handling-requests-and-responses.md)
  Write a request for app or book metadata and handle responses from the API.
- [Fetching storefront objects](fetching-storefront-objects.md)
  Pick a region-specific geographic location to retrieve catalog information from.
- [Common Objects](common-objects.md)
  Understand the common JSON objects that framework responses contain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetching-resources-with-extended-attributes)*