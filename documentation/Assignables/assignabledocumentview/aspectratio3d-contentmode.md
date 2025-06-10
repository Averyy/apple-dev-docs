# aspectRatio3D(_:contentMode:)

**Framework**: Assignables  
**Kind**: method

Constrains this view’s dimensions to the specified 3D aspect ratio.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func aspectRatio3D(_ aspectRatio: Size3D? = nil, contentMode: ContentMode) -> some View
```

#### Return Value

A view that constrains this view’s dimensions to `aspectRatio`, using `contentMode` as its scaling algorithm.

#### Discussion

If this view is resizable, the resulting view will have `aspectRatio` as its aspect ratio. In this example, the Model3D has a 2 : 3 : 1 width to height to depth ratio, and scales to fit its frame:

```None
Model3D(named: "Sphere") { resolved in
    let ratio3D = Size3D(width: 2, height: 3, depth: 1)
    resolved
        .resizable()
        .aspectRatio3D(ratio3D, contentMode: .fit)
} placeholder: {
    ProgressView()
}
.frame(width: 200, height: 200)
.frame(depth: 200)
.border(Color(white: 0.75))
```

## Parameters

- `aspectRatio`: The ratio of width to height to depth to use for   the resulting view. If   is  ,   the resulting view maintains this view’s aspect ratio.
- `contentMode`: A flag indicating whether this view should fit or   fill the parent context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/aspectratio3d(_:contentmode:))*