# init(size:label:opaque:colorMode:renderer:)

**Framework**: SwiftUI  
**Kind**: init

Initializes an image of the given size, with contents provided by a custom rendering closure.

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
init(size: CGSize, label: Text? = nil, opaque: Bool = false, colorMode: ColorRenderingMode = .nonLinear, renderer: @escaping (inout GraphicsContext) -> Void)
```

#### Discussion

Use this initializer to create an image by calling drawing commands on a [`GraphicsContext`](graphicscontext.md) provided to the `renderer` closure.

The following example shows a custom image created by passing a `GraphicContext` to draw an ellipse and fill it with a gradient:

```swift
let mySize = CGSize(width: 300, height: 200)
let image = Image(size: mySize) { context in
    context.fill(
        Path(
            ellipseIn: CGRect(origin: .zero, size: mySize)),
            with: .linearGradient(
                Gradient(colors: [.yellow, .orange]),
                startPoint: .zero,
                endPoint: CGPoint(x: mySize.width, y:mySize.height))
    )
}
```

![An ellipse with a gradient that blends from yellow at the upper-](https://docs-assets.developer.apple.com/published/0c7d3728c4b4e45be13673be65c95a0d/Image-2%402x.png)

## Parameters

- `size`: The size of the newly-created image.
- `label`: The label associated with the image. SwiftUI uses the label   for accessibility.
- `opaque`: A Boolean value that indicates whether the image is fully   opaque. This may improve performance when  . Don’t render   non-opaque pixels to an image declared as opaque. Defaults to  .
- `colorMode`: The working color space and storage format of the image.   Defaults to  .
- `renderer`: A closure to draw the contents of the image. The closure   receives a   as its parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/image/init(size:label:opaque:colormode:renderer:))*