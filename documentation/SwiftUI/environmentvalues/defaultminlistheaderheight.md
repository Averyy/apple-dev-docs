# defaultMinListHeaderHeight

**Framework**: SwiftUI  
**Kind**: property

The default minimum height of a header in a list.

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
var defaultMinListHeaderHeight: CGFloat? { get set }
```

#### Discussion

When this value is `nil`, the system chooses the appropriate height. The default is `nil`.

## See Also

- [func headerProminence(Prominence) -> some View](view/headerprominence(_:).md)
  Sets the header prominence for this view.
- [var headerProminence: Prominence](environmentvalues/headerprominence.md)
  The prominence to apply to section headers within a view.
- [enum Prominence](prominence.md)
  A type indicating the prominence of a view hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/defaultminlistheaderheight)*