# effectWithPreview:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a pointer content effect with the given preview’s view.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) effectWithPreview:(UITargetedPreview *) preview;
```

## Discussion

`UIPointerEffect` attempts to determine the appropriate effect for the given preview automatically. Use one of its subclasses to request a specific system-provided effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointereffect-c.class/effectwithpreview:)*