# resetOrder()

**Framework**: SwiftUI  
**Kind**: method

Resets the column order back to the default, preserving the customized visibility and size.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
mutating func resetOrder()
```

#### Discussion

Tables that are bound to this state will order their columns as described by their column builder.

## See Also

- [subscript(visibility _: String) -> Visibility](tablecolumncustomization/subscript(visibility:).md)
  The visibility of the column identified by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumncustomization/resetorder())*