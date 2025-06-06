# init(opaque:colorMode:rendersAsynchronously:renderer:symbols:)

**Framework**: SwiftUI  
**Kind**: init

Creates and configures a canvas that you supply with renderable child views.

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
init(opaque: Bool = false, colorMode: ColorRenderingMode = .nonLinear, rendersAsynchronously: Bool = false, renderer: @escaping (inout GraphicsContext, CGSize) -> Void, @ViewBuilder symbols: () -> Symbols)
```

#### Discussion

This initializer behaves like the [`init(opaque:colorMode:rendersAsynchronously:renderer:)`](canvas/init(opaque:colormode:rendersasynchronously:renderer:).md) initializer, except that you also provide a collection of SwiftUI views for the renderer to use as drawing elements.

SwiftUI stores a rendered version of each child view that you specify in the `symbols` view builder and makes these available to the canvas. Tag each child view so that you can retrieve it from within the renderer using the [`resolveSymbol(id:)`](graphicscontext/resolvesymbol(id:).md) method. For example, you can create a scatter plot using a passed-in child view as the mark for each data point:

```swift
struct ScatterPlotView<Mark: View>: View {
    let rects: [CGRect]
    let mark: Mark

    enum SymbolID: Int {
        case mark
    }

    var body: some View {
        Canvas { context, size in
            if let mark = context.resolveSymbol(id: SymbolID.mark) {
                for rect in rects {
                    context.draw(mark, in: rect)
                }
            }
        } symbols: {
            mark.tag(SymbolID.mark)
        }
        .frame(width: 300, height: 200)
        .border(Color.blue)
    }
}
```

You can use any SwiftUI view for the `mark` input:

```swift
ScatterPlotView(rects: rects, mark: Image(systemName: "circle"))
```

If the `rects` input contains 50 randomly arranged [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) instances, SwiftUI draws a plot like this:

![A screenshot of a scatter plot inside a blue rectangle, containing](https://docs-assets.developer.apple.com/published/c9690af16722852c643d0340841d7eb1/Canvas-init-1%402x.png)

The symbol inputs, like all other elements that you draw to the canvas, lack individual accessibility and interactivity, even if the original SwiftUI view has these attributes. However, you can add accessibility and interactivity modifers to the canvas as a whole.

## Parameters

- `opaque`: A Boolean that indicates whether the canvas is fully   opaque. You might be able to improve performance by setting this   value to  , but then drawing a non-opaque image into the   context produces undefined results. The default is  .
- `colorMode`: A working color space and storage format of the canvas.   The default is  .
- `rendersAsynchronously`: A Boolean that indicates whether the canvas   can present its contents to its parent view asynchronously. The   default is  .
- `renderer`: A closure in which you conduct immediate mode drawing.   The closure takes two inputs: a context that you use to issue   drawing commands and a size — representing the current   size of the canvas — that you can use to customize the content.   The canvas calls the renderer any time it needs to redraw the   content.
- `symbols`: A   that you use to supply SwiftUI views to   the canvas for use during drawing. Uniquely tag each view   using the   modifier, so that you can find them from   within your renderer using the    method.

## See Also

- [init(opaque: Bool, colorMode: ColorRenderingMode, rendersAsynchronously: Bool, renderer: (inout GraphicsContext, CGSize) -> Void)](canvas/init(opaque:colormode:rendersasynchronously:renderer:).md)
  Creates and configures a canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/canvas/init(opaque:colormode:rendersasynchronously:renderer:symbols:))*