# init(_:width:height:depth:)

**Framework**: SwiftUI  
**Kind**: init

Creates a new window placement with an optional position and 3D size. Depth is ignored on scenes or platforms that don’t support it.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
init(_ position: WindowPlacement.Position? = nil, width: CGFloat? = nil, height: CGFloat? = nil, depth: CGFloat? = nil)
```

#### Discussion

Any values not provided will use use the default values for the `Scene` that this placement is being applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowplacement/init(_:width:height:depth:))*