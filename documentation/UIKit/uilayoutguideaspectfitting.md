# UILayoutGuideAspectFitting

**Framework**: UIKit  
**Kind**: protocol

The interface for a layout guide that supports a particular aspect ratio.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol UILayoutGuideAspectFitting : NSObjectProtocol
```

#### Overview

The [`safeAreaAspectFitLayoutGuide`](uiwindow/safeareaaspectfitlayoutguide.md) property adopts this protocol to provide a layout guide for placing media content of a particular aspect ratio.

## Topics

### Specifying the aspect ratio
- [var aspectRatio: CGFloat](uilayoutguideaspectfitting/aspectratio.md)
  The content’s aspect ratio.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var safeAreaAspectFitLayoutGuide: any UILayoutGuide & UILayoutGuideAspectFitting](uiwindow/safeareaaspectfitlayoutguide.md)
  A layout guide for placing content of a particular aspect ratio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilayoutguideaspectfitting)*