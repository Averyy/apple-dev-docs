# contentShape(_:eoFill:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Defines the content shape for hit testing.

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
func contentShape<S>(_ shape: S, eoFill: Bool = false) -> some View where S : Shape
```

## Return Value

A view that uses the given shape for hit testing.

## Parameters

- `shape`: The hit testing shape for the view.
- `eoFill`: A Boolean that indicates whether the shape is interpreted with the even-odd winding number rule.

## See Also

### Controlling hit testing
- [func allowsTightening(Bool) -> some View](./allowstightening%28_%29.md)
  Sets whether text in this view can compress the space between characters when necessary to fit text in a line.
- [func contentShape<S>(ContentShapeKinds, S, eoFill: Bool) -> some View](./contentshape%28_,_,eofill%29.md)
  Sets the content shape for this view.
- [struct ContentShapeKinds](../contentshapekinds.md)
  A kind for the content shape of a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contentshape(_:eofill:))*