# AVMetadataItemValueRequest

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVMetadataItemValueRequest : NSObject
```

## Topics

### Handling the response
- [func respond(value: any NSCopying & NSObjectProtocol)](./avmetadataitemvaluerequest/respond%28value%29.md)
  Returns the metadata item’s value.
- [func respond(error: any Error)](./avmetadataitemvaluerequest/respond%28error%29.md)
  Returns an error when the system fails to load the value.
- [var metadataItem: AVMetadataItem?](./avmetadataitemvaluerequest/metadataitem.md)
  The metadata item to request a value for.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a metadata item
- [init(propertiesOfMetadataItem: AVMetadataItem, valueLoadingHandler: (AVMetadataItemValueRequest) -> Void)](./avmetadataitem/init%28propertiesofmetadataitem,valueloadinghandler%29.md)
  Creates a metadata item whose value loads on an on-demand basis only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitemvaluerequest)*