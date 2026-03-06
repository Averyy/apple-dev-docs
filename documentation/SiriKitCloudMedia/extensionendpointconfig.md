# ExtensionEndpointConfig

**Framework**: SiriKit Cloud Media  
**Kind**: dictionary

Instructions for accessing an intent endpoint.

**Availability**:
- SiriKit Cloud Media 1.0.2+

## Declaration

```swift
object ExtensionEndpointConfig
```

## Topics

### Requiring Headers for All Endpoints
- [object ExtensionEndpointConfig.Hdr](extensionendpointconfig/hdr-data.dictionary.md)
  Headers to include with requests to intent endpoints.

## Properties

- `hdr` (ExtensionEndpointConfig.Hdr): Headers the client must include in requests to this endpoint.
- `url` (string): The path to access this endpoint. The path may be an absolute URL, or relative to the resolved [`Configure Your Service Endpoints`](configuration-resource.md) URL. Provide an empty string if your service doesn’t support this endpoint.

## Relationships

### Inherited By
- [ExtensionConfig.Intent.AddMedia](extensionconfig/intent-data.dictionary/addmedia-data.dictionary.md)
- [ExtensionConfig.Intent.PlayMedia](extensionconfig/intent-data.dictionary/playmedia-data.dictionary.md)
- [ExtensionConfig.Intent.UpdateMediaAffinity](extensionconfig/intent-data.dictionary/updatemediaaffinity-data.dictionary.md)

## See Also

- [object ExtensionConfig.Intent](extensionconfig/intent-data.dictionary.md)
  Instructions for accessing your media service’s intent endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sirikitcloudmedia/extensionendpointconfig)*