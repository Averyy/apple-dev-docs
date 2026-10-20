# AVCaptionGrouper

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaptionGrouper : NSObject
```

## Topics

### Adding captions
- [func add(AVCaption)](./avcaptiongrouper/add%28_%29.md)
  Adds a caption to the pending group.
### Generating captions groups
- [func flushAddedCaptions(upTo: CMTime) -> [AVCaptionGroup]](./avcaptiongrouper/flushaddedcaptions%28upto%29.md)
  Creates caption groups for the captions you enqueue up to the time.

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

### Groups
- [class AVCaptionGroup](./avcaptiongroup.md)
  An object that represents zero or more captions that intersect in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptiongrouper)*