# Visibility.visible

**Framework**: SwiftUI  
**Kind**: case

The element may be visible.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case visible
```

#### Discussion

Some APIs may use this value to represent a hint or preference, rather than a mandatory assertion. For example, setting list row separator visibility to `visible` using the [`listRowSeparator(_:edges:)`](view/listrowseparator(_:edges:).md) modifier may not always result in any visible separators, especially for list styles that do not include separators as part of their design.

## See Also

- [Visibility.automatic](visibility/automatic.md)
  The element may be visible or hidden depending on the policies of the component accepting the visibility configuration.
- [Visibility.hidden](visibility/hidden.md)
  The element may be hidden.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/visibility/visible)*