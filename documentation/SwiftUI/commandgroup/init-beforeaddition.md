# init(before:addition:)

**Framework**: SwiftUI  
**Kind**: init

A value describing the addition of the given views to the beginning of the indicated group.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(before group: CommandGroupPlacement, @ViewBuilder addition: () -> Content)
```

## See Also

- [init(after: CommandGroupPlacement, addition: () -> Content)](commandgroup/init(after:addition:).md)
  A value describing the addition of the given views to the end of the indicated group.
- [init(replacing: CommandGroupPlacement, addition: () -> Content)](commandgroup/init(replacing:addition:).md)
  A value describing the complete replacement of the contents of the indicated group with the given views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandgroup/init(before:addition:))*