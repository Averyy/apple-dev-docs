# NSView.ExclusiveGestureBehavior

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Exclusive gesture behavior

**Availability**:
- macOS 27.0+

## Declaration

```swift
enum ExclusiveGestureBehavior
```

```c
enum NSViewExclusiveGestureBehavior : NSInteger;
```

## Overview

See the `exclusiveGestureBehavior` property of `NSView` more information.

## Topics

### Getting exclusivity values
- [NSView.ExclusiveGestureBehavior.exclusive](./exclusivegesturebehavior-swift.enum/exclusive.md)
  This view and its subviews have exclusive gestures
- [NSView.ExclusiveGestureBehavior.inherit](./exclusivegesturebehavior-swift.enum/inherit.md)
  Inherit from superview
- [NSView.ExclusiveGestureBehavior.notExclusive](./exclusivegesturebehavior-swift.enum/notexclusive.md)
  This view and its subviews do not have exclusive gestures
### Initializers
- [init?(rawValue: Int)](./exclusivegesturebehavior-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing gesture exclusivity
- [var exclusiveGestureBehavior: NSView.ExclusiveGestureBehavior](./exclusivegesturebehavior-swift.property.md)
  Declares whether gesture recognizers should be exclusive in this view and its subviews.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/exclusivegesturebehavior-swift.enum)*