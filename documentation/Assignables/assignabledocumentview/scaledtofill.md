# scaledToFill()

**Framework**: Assignables  
**Kind**: method

Scales this view to fill its parent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func scaledToFill() -> some View
```

#### Return Value

A view that scales this view to fill its parent, maintaining this view’s aspect ratio.

#### Discussion

Use `scaledToFill()` to scale this view to fill its parent, while maintaining the view’s aspect ratio as the view scales:

```None
Circle()
    .fill(Color.pink)
    .scaledToFill()
    .frame(width: 300, height: 150)
    .border(Color(white: 0.75))
```

This method is equivalent to calling `View/aspectRatio(_:contentMode:)` with a `nil` aspectRatio and a content mode of `ContentMode/fill`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/scaledtofill())*