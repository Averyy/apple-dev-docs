# CPImageOverlay.Alignment

**Framework**: CarPlay  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the placement of overlay images in a thumbnail.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
enum Alignment
```

```c
enum CPImageOverlayAlignment : NSInteger;
```

## Overview

CarPlay displays overlays inside the bounds of the thumbnail image and along the top edge. The constants in this type specify whether the overlay aligns to the leading or trailing edges of the thumbnail or to the center.

## Topics

### Enumeration Cases
- [CPImageOverlay.Alignment.center](./alignment-swift.enum/center.md)
  An option to align the overlay to the top center of the thumbnail.
- [CPImageOverlay.Alignment.leading](./alignment-swift.enum/leading.md)
  An option to align the overlay to the top leading edge of the thumbnail.
- [CPImageOverlay.Alignment.trailing](./alignment-swift.enum/trailing.md)
  An option to align the overlay to the top trailing edge of the thumbnail.
### Initializers
- [init?(rawValue: Int)](./alignment-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the overlay position
- [var alignment: CPImageOverlay.Alignment](./alignment-swift.property.md)
  The alignment of the overlay inside the top edge of the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageoverlay/alignment-swift.enum)*