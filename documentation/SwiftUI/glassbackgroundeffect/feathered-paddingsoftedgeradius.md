# feathered(padding:softEdgeRadius:)

**Framework**: SwiftUI  
**Kind**: method

A feathered background effect with custom padding and soft edge radius.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
static func feathered(padding length: CGFloat, softEdgeRadius: CGFloat? = nil) -> FeatheredGlassBackgroundEffect
```

#### Return Value

A feathered background effect.

## Parameters

- `softEdgeRadius`: When a blur is clipped, the radial size of the   blur’s edge. If you set the value to  , SwiftUI uses a default   amount. The default value of this parameter is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glassbackgroundeffect/feathered(padding:softedgeradius:))*