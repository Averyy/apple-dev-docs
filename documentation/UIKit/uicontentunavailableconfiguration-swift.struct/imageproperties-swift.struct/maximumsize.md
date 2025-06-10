# maximumSize

**Framework**: UIKit  
**Kind**: property

A maximum size for the image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
var maximumSize: CGSize { get set }
```

#### Discussion

The default value is [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero). Setting a [`width`](https://developer.apple.com/documentation/CoreFoundation/CGSize/width) or [`height`](https://developer.apple.com/documentation/CoreFoundation/CGSize/height) of zero makes the size unconstrained on that dimension. If the image exceeds [`maximumSize`](uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/maximumsize.md) size on either dimension, the view reduces its size proportionately, maintaining aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentunavailableconfiguration-swift.struct/imageproperties-swift.struct/maximumsize)*