# defaultValue(in:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Calculates a default value for the corresponding guide in the specified context.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func defaultValue(in context: ViewDimensions3D) -> CGFloat
```

#### Return Value

The offset of the guide from the origin in the view’s coordinate space.

#### Discussion

Implement this method when you create a type that conforms to the [`DepthAlignmentID`](depthalignmentid.md) protocol. Use the method to calculate the default offset of the corresponding alignment guide. SwiftUI interprets the value that you return as an offset in the coordinate space of the view that’s being laid out. For example, you can use the context to return a value that’s one-third of the height of the view:

```swift
private struct FirstThirdAlignment: DepthAlignmentID {
    static func defaultValue(in context: ViewDimensions3D) -> CGFloat {
        context.depth / 3
    }
}
```

You can override the default value that this method returns for a particular guide by adding the [`alignmentGuide(_:computeValue:)`](view/alignmentguide(_:computevalue:).md) view modifier to a particular view.

## Parameters

- `context`: The context of the view that you apply   the alignment guide to. The context gives you the view’s dimensions,   as well as the values of other alignment guides that apply to the   view, including both built-in and custom guides. You can use any of   these values, if helpful, to calculate the value for your custom   guide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/depthalignmentid/defaultvalue(in:))*