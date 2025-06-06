# init(bounds:format:)

**Framework**: UIKit  
**Kind**: init

Creates a new graphics renderer with the specified bounds and format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(bounds: CGRect, format: UIGraphicsPDFRendererFormat)
```

#### Return Value

An initialized PDF graphics renderer.

#### Discussion

Use this initializer to create a PDF renderer when you want to override the default format for the current device. Otherwise, use the [`init(bounds:)`](uigraphicsrenderer/init(bounds:).md) method present on the abstract superclass, [`UIGraphicsRenderer`](uigraphicsrenderer.md).

## Parameters

- `bounds`: The bounds of the Core Graphics context available to the renderer, with values in points.
- `format`: A   object that encapsulates the format applied to the renderer’s context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/init(bounds:format:))*