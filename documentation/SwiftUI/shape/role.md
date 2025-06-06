# role

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

An indication of how to style a shape.

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
nonisolated
static var role: ShapeRole { get }
```

#### Discussion

SwiftUI looks at a shape’s role when deciding how to apply a [`ShapeStyle`](shapestyle.md) at render time. The [`Shape`](shape.md) protocol provides a default implementation with a value of [`ShapeRole.fill`](shaperole/fill.md). If you create a composite shape, you can provide an override of this property to return another value, if appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shape/role)*