# padding(_:_:)

**Framework**: FamilyControls  
**Kind**: method

Adds an equal padding amount to specific edges of this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func padding(_ edges: Edge.Set = .all, _ length: CGFloat? = nil) -> some View
```

#### Return Value

A view that’s padded by the specified amount on the specified edges.

#### Discussion

Use this modifier to add a specified amount of padding to one or more edges of the view. Indicate the edges to pad by naming either a single value from `Edge/Set`, or by specifying an [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) that contains edge values:

```swift
VStack {
    Text("Text padded by 20 points on the bottom and trailing edges.")
        .padding([.bottom, .trailing], 20)
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

The order in which you apply modifiers matters. The example above applies the padding before applying the border to ensure that the border encompasses the padded region:

You can omit either or both of the parameters. If you omit the `length`, SwiftUI uses a default amount of padding. If you omit the `edges`, SwiftUI applies the padding to all edges. Omit both to add a default padding all the way around a view. SwiftUI chooses a default amount of padding that’s appropriate for the platform and the presentation context.

```swift
VStack {
    Text("Text with default padding.")
        .padding()
        .border(.gray)
    Text("Unpadded text for comparison.")
        .border(.yellow)
}
```

The example above looks like this in iOS under typical conditions:

To control the amount of padding independently for each edge, use `View/padding(_:)-6pgqq`. To pad all outside edges of a view by a specified amount, use `View/padding(_:)-68shk`.

## Parameters

- `edges`: The set of edges to pad for this view. The default   is  .
- `length`: An amount, given in points, to pad this view on the   specified edges. If you set the value to  , SwiftUI uses   a platform-specific default amount. The default value of this   parameter is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityiconview/padding(_:_:))*