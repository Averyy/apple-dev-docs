# init(_:size3D:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new window placement with an optional position and 3D size. Depth is ignored on scenes that don’t support it.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(_ position: WindowPlacement.Position? = nil, size3D: Size3D? = nil)
```

#### Discussion

Any values not provided will use use the default values for the `Scene` that this placement is being applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowplacement/init(_:size3d:))*