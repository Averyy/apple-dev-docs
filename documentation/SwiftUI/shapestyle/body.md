# body

**Framework**: SwiftUI  
**Kind**: property

A rectangular view that’s filled with the shape style.

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
var body: _ShapeView<Rectangle, Self> { get }
```

#### Discussion

For a [`ShapeStyle`](shapestyle.md) that also conforms to the [`View`](view.md) protocol, like [`Color`](color.md) or [`LinearGradient`](lineargradient.md), this default implementation of the [`body`](view/body-8kl5o.md) property provides a visual representation for the shape style. As a result, you can use the shape style in a view hierarchy like any other view:

```swift
ZStack {
    Color.cyan
    Text("Hello!")
}
.frame(width: 200, height: 50)
```

![A screenshot of a cyan rectangle with the text hello appearing](https://docs-assets.developer.apple.com/published/d98cc7c4fc793e30a60868b76210d872/ShapeStyle-body-1%402x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shapestyle/body)*