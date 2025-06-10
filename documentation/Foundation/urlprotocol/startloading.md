# startLoading()

**Framework**: Foundation  
**Kind**: method

Starts protocol-specific loading of the request.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func startLoading()
```

#### Discussion

When this method is called, the subclass implementation should start loading the request, providing feedback to the URL loading system via the [`URLProtocolClient`](urlprotocolclient.md) protocol.

Subclasses must implement this method.

## See Also

- [func stopLoading()](urlprotocol/stoploading.md)
  Stops protocol-specific loading of the request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlprotocol/startloading())*