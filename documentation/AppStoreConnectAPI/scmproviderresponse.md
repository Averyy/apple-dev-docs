# ScmProviderResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single SCM provider connected to Xcode Cloud.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmProviderResponse
```

## Properties

- `data` (ScmProvider) *(required)*: The resource data.
- `links` (DocumentLinks) *(required)*: The navigational links that include the self-link.

## See Also

- [object ScmProvider](scmprovider.md)
  A source code management provider, such as GitHub or Bitbucket, connected to Xcode Cloud for accessing repositories.
- [object ScmProvidersResponse](scmprovidersresponse.md)
  The response body for endpoints that list SCM providers connected to Xcode Cloud.
- [object ScmProviderRepositoriesLinkagesResponse](scmproviderrepositorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmproviderresponse)*