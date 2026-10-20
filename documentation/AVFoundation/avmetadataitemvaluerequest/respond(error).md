# respond(error:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns an error when the system fails to load the value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func respond(error: any Error)
```

```objc
- (void) respondWithError:(NSError *) error;
```

## Parameters

- `error`: The error to return for the request.

## See Also

### Handling the response
- [func respond(value: any NSCopying & NSObjectProtocol)](./respond%28value%29.md)
  Returns the metadata item’s value.
- [var metadataItem: AVMetadataItem?](./metadataitem.md)
  The metadata item to request a value for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/respond(error:))*