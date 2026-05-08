# subviews

**Framework**: SwiftUI  
**Kind**: property

Enable all gestures in the subview hierarchy but disable the added gesture.

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
static let subviews: GestureMask
```

## See Also

- [static let all: GestureMask](gesturemask/all.md)
  Enable both the added gesture as well as all other gestures on the view and its subviews.
- [static let gesture: GestureMask](gesturemask/gesture.md)
  Enable the added gesture but disable all gestures in the subview hierarchy.
- [static let none: GestureMask](gesturemask/none.md)
  Disable all gestures in the subview hierarchy, including the added gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gesturemask/subviews)*