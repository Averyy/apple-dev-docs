# resetOrder()

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

### Managing the customization
- [subscript(visibility _: String) -> Visibility](./subscript%28visibility%29.md)
  The visibility of the column identified by its identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumncustomization/resetorder())*