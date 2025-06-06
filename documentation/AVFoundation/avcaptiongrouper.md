# AVCaptionGrouper

**Framework**: AVFoundation  
**Kind**: class

An object that analyzes the temporal overlaps of caption objects to create caption groups for each span of concurrent captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaptionGrouper
```

## Topics

### Adding Captions
- [func add(AVCaption)](avcaptiongrouper/add(_:).md)
  Adds a caption to the pending group.
### Generating Captions Groups
- [func flushAddedCaptions(upTo: CMTime) -> [AVCaptionGroup]](avcaptiongrouper/flushaddedcaptions(upto:).md)
  Creates caption groups for the captions you enqueue up to the time.

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

- [class AVCaptionGroup](avcaptiongroup.md)
  An object that represents zero or more captions that intersect in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptiongrouper)*