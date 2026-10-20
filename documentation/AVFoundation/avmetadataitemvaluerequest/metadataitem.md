# metadataItem

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The metadata item to request a value for.

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
weak var metadataItem: AVMetadataItem? { get }
```

```objc
@property (weak, readonly) AVMetadataItem * metadataItem;
```

## See Also

### Handling the response
- [func respond(value: any NSCopying & NSObjectProtocol)](./respond%28value%29.md)
  Returns the metadata item’s value.
- [func respond(error: any Error)](./respond%28error%29.md)
  Returns an error when the system fails to load the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest/metadataitem)*