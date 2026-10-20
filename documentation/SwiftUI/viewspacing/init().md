# init()

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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

Use this initializer to create a spacing preferences instance with default values. Then use [`formUnion(_:edges:)`](./formunion%28_,edges%29.md) to combine preferences from other views with the new instance. You typically do this in a custom layout’s implementation of the [`spacing(subviews:cache:)`](../layout/spacing%28subviews,cache%29.md) method.

## See Also

### Creating spacing instances
- [static let zero: ViewSpacing](./zero.md)
  A view spacing instance that contains zero on all edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/viewspacing/init())*