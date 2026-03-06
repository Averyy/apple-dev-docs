# ScmProvider

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represents a Providers resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object ScmProvider
```

## Topics

### Objects and Types
- [object ScmProvider.Attributes](scmprovider/attributes-data.dictionary.md)
  The attributes that describe a Providers resource.
- [object ScmProviderType](scmprovidertype.md)
  The source code management provider’s type.
### Dictionaries
- [object ScmProvider.Relationships](scmprovider/relationships-data.dictionary.md)

## Properties

- `attributes` (ScmProvider.Attributes): The attributes that describe the Providers resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies a Providers resource.
- `links` (ResourceLinks): The navigational links that include the self-link.
- `relationships` (ScmProvider.Relationships)
- `type` (string) *(required)*: The resource type.

## See Also

- [object ScmProviderResponse](scmproviderresponse.md)
  A response that contains a single Providers resource.
- [object ScmProvidersResponse](scmprovidersresponse.md)
  A response that contains a list of Providers resources.
- [object ScmProviderRepositoriesLinkagesResponse](scmproviderrepositorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/scmprovider)*