# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a 2D `EdgeInsets` from an `EdgeInsets3D`, dropping its `front` and `back` values.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
init(_ i: EdgeInsets3D)
```

**Other overloads**:

```swift
init(_ nsEdgeInsets: NSDirectionalEdgeInsets)
```

## See Also

### Creating an edge inset
- [init()](./init%28%29.md)
- [init(top: CGFloat, leading: CGFloat, bottom: CGFloat, trailing: CGFloat)](./init%28top,leading,bottom,trailing%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/edgeinsets/init(_:))*