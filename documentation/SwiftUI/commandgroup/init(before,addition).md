# init(before:addition:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

A value describing the addition of the given views to the beginning of the indicated group.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(before group: CommandGroupPlacement, @ContentBuilder addition: () -> Content)
```

## See Also

### Creating a command group
- [init(after: CommandGroupPlacement, addition: () -> Content)](./init%28after,addition%29.md)
  A value describing the addition of the given views to the end of the indicated group.
- [init(replacing: CommandGroupPlacement, addition: () -> Content)](./init%28replacing,addition%29.md)
  A value describing the complete replacement of the contents of the indicated group with the given views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/commandgroup/init(before:addition:))*