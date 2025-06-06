# gesture

**Framework**: SwiftUI  
**Kind**: property

Enable the added gesture but disable all gestures in the subview hierarchy.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static let gesture: GestureMask
```

## See Also

- [static let all: GestureMask](gesturemask/all.md)
  Enable both the added gesture as well as all other gestures on the view and its subviews.
- [static let subviews: GestureMask](gesturemask/subviews.md)
  Enable all gestures in the subview hierarchy but disable the added gesture.
- [static let none: GestureMask](gesturemask/none.md)
  Disable all gestures in the subview hierarchy, including the added gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturemask/gesture)*