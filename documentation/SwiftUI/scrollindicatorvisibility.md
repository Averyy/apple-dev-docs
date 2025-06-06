# ScrollIndicatorVisibility

**Framework**: SwiftUI  
**Kind**: struct

The visibility of scroll indicators of a UI element.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct ScrollIndicatorVisibility
```

#### Overview

Pass a value of this type to the [`scrollIndicators(_:axes:)`](view/scrollindicators(_:axes:).md) method to specify the preferred scroll indicator visibility of a view hierarchy.

## Topics

### Getting visibilties
- [static var automatic: ScrollIndicatorVisibility](scrollindicatorvisibility/automatic.md)
  Scroll indicator visibility depends on the policies of the component accepting the visibility configuration.
- [static var hidden: ScrollIndicatorVisibility](scrollindicatorvisibility/hidden.md)
  Hide the scroll indicators.
- [static var never: ScrollIndicatorVisibility](scrollindicatorvisibility/never.md)
  Scroll indicators should never be visible.
- [static var visible: ScrollIndicatorVisibility](scrollindicatorvisibility/visible.md)
  Show the scroll indicators.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [func scrollIndicatorsFlash(onAppear: Bool) -> some View](view/scrollindicatorsflash(onappear:).md)
  Flashes the scroll indicators of a scrollable view when it appears.
- [func scrollIndicatorsFlash(trigger: some Equatable) -> some View](view/scrollindicatorsflash(trigger:).md)
  Flashes the scroll indicators of scrollable views when a value changes.
- [func scrollIndicators(ScrollIndicatorVisibility, axes: Axis.Set) -> some View](view/scrollindicators(_:axes:).md)
  Sets the visibility of scroll indicators within this view.
- [var horizontalScrollIndicatorVisibility: ScrollIndicatorVisibility](environmentvalues/horizontalscrollindicatorvisibility.md)
  The visibility to apply to scroll indicators of any horizontally scrollable content.
- [var verticalScrollIndicatorVisibility: ScrollIndicatorVisibility](environmentvalues/verticalscrollindicatorvisibility.md)
  The visiblity to apply to scroll indicators of any vertically scrollable content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollindicatorvisibility)*