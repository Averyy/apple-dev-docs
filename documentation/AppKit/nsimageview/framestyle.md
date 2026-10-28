# NSImageView.FrameStyle

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that allow you to specify the kind of frame bordering the image.

**Availability**:
- macOS

## Declaration

```swift
enum FrameStyle
```

```c
enum NSImageFrameStyle : NSUInteger;
```

## Overview

These constants are used by [`imageFrameStyle`](../nsimagecell/imageframestyle.md). Note that some of these constants are stylistically obsolete and should be considered deprecated.

## Topics

### Constants
- [NSImageView.FrameStyle.none](./framestyle/none.md)
  An invisible frame
- [NSImageView.FrameStyle.photo](./framestyle/photo.md)
  A thin black outline and a dropped shadow.
- [NSImageView.FrameStyle.grayBezel](./framestyle/graybezel.md)
  A gray, concave bezel that makes the image look sunken.
- [NSImageView.FrameStyle.groove](./framestyle/groove.md)
  A thin groove that looks etched around the image.
- [NSImageView.FrameStyle.button](./framestyle/button.md)
  A convex bezel that makes the image stand out in relief, like a button.
### Initializers
- [init?(rawValue: UInt)](./framestyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum NSImageAlignment](../nsimagealignment.md)
  Constants used by [`imageAlignment`](../nsimagecell/imagealignment.md) that allow you to specify the location of the image in the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimageview/framestyle)*