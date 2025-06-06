# init()

**Framework**: SwiftUI  
**Kind**: init

Initializes an instance with default spacing values.

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
init()
```

#### Discussion

Use this initializer to create a spacing preferences instance with default values. Then use [`formUnion(_:edges:)`](viewspacing/formunion(_:edges:).md) to combine preferences from other views with the new instance. You typically do this in a custom layout’s implementation of the [`spacing(subviews:cache:)`](layout/spacing(subviews:cache:).md) method.

## See Also

- [static let zero: ViewSpacing](viewspacing/zero.md)
  A view spacing instance that contains zero on all edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewspacing/init())*