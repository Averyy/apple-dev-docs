# AVMetadataItemValueRequest

**Framework**: AVFoundation  
**Kind**: class

An object that responds to a request to load the value of a metadata item.

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
class AVMetadataItemValueRequest
```

## Topics

### Handling the response
- [func respond(value: any NSCopying & NSObjectProtocol)](avmetadataitemvaluerequest/respond(value:).md)
  Returns the metadata item’s value.
- [func respond(error: any Error)](avmetadataitemvaluerequest/respond(error:).md)
  Returns an error when the system fails to load the value.
- [var metadataItem: AVMetadataItem?](avmetadataitemvaluerequest/metadataitem.md)
  The metadata item to request a value for.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(propertiesOfMetadataItem: AVMetadataItem, valueLoadingHandler: (AVMetadataItemValueRequest) -> Void)](avmetadataitem/init(propertiesofmetadataitem:valueloadinghandler:).md)
  Creates a metadata item whose value loads on an on-demand basis only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest)*