# scaledToFill3D()

**Framework**: SwiftUI  
**Kind**: method

Scales this view to fill its parent.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func scaledToFill3D() -> some View
```

#### Return Value

A view that scales this view to fit its parent, maintaining this view’s aspect ratio.

#### Discussion

This view’s 3D aspect ratio is maintained as the view scales. This method is equivalent to calling `aspectRatio3D(nil, contentMode: .fill)`.

```swift
Model3D(named: "Sphere") { resolved in
    resolved
        .resizable()
        .scaledToFill3D()
} placeholder: {
    ProgressView()
}
.frame(width: 300, height: 100)
.frame(depth: 300)
.border(Color(white: 0.75))
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scaledtofill3d())*