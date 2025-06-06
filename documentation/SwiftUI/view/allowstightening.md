# allowsTightening(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets whether text in this view can compress the space between characters when necessary to fit text in a line.

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
nonisolated
func allowsTightening(_ flag: Bool) -> some View
```

#### Return Value

A view that can compress the space between characters when necessary to fit text in a line.

#### Discussion

Use `allowsTightening(_:)` to enable the compression of inter-character spacing of text in a view to try to fit the text in the view’s bounds.

In the example below, two identically configured text views show the effects of `allowsTightening(_:)` on the compression of the spacing between characters:

```swift
VStack {
    Text("This is a wide text element")
        .font(.body)
        .frame(width: 200, height: 50, alignment: .leading)
        .lineLimit(1)
        .allowsTightening(true)

    Text("This is a wide text element")
        .font(.body)
        .frame(width: 200, height: 50, alignment: .leading)
        .lineLimit(1)
        .allowsTightening(false)
}
```

![A screenshot showing the effect of enabling text tightening in a](https://docs-assets.developer.apple.com/published/7875ef8b31de58ae8d8efc6485da09b0/SwiftUI-view-allowsTightening%402x.png)

## Parameters

- `flag`: A Boolean value that indicates whether the space   between characters compresses when necessary.

## See Also

- [func contentShape<S>(S, eoFill: Bool) -> some View](view/contentshape(_:eofill:).md)
  Defines the content shape for hit testing.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](view/contentshape(_:_:eofill:).md)
  Sets the content shape for this view.
- [struct ContentShapeKinds](contentshapekinds.md)
  A kind for the content shape of a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/allowstightening(_:))*