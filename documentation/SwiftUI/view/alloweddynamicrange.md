# allowedDynamicRange(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a new view configured with the specified allowed dynamic range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func allowedDynamicRange(_ range: Image.DynamicRange?) -> some View
```

#### Return Value

A new view.

#### Discussion

The following example enables HDR rendering within a view hierarchy:

```swift
MyView().allowedDynamicRange(.high)
```

## Parameters

- `range`: The requested dynamic range, or nil to   restore the default allowed range.

## See Also

- [func backgroundStyle<S>(S) -> some View](view/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [func foregroundStyle<S>(S) -> some View](view/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](view/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/alloweddynamicrange(_:))*