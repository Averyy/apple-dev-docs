# scaledToFit3D()

**Framework**: MusicKit  
**Kind**: method

Scales this view to fit its parent.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
nonisolated
func scaledToFit3D() -> some View
```

#### Return Value

A view that scales this view to fit its parent, maintaining this view’s aspect ratio.

#### Discussion

This view’s 3D aspect ratio is maintained as the view scales. This method is equivalent to calling `aspectRatio3D(nil, contentMode: .fit)`.

```swift
Model3D(named: "Plane") { resolved in
    resolved
        .resizable()
        .scaledToFit3D()
} placeholder: {
    ProgressView()
}
.frame(width: 400, height: 400)
.frame(depth: 200)
.border(Color(white: 0.75))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/scaledtofit3d())*