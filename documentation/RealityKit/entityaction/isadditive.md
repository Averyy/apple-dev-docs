# isAdditive

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

A Boolean value that determines whether this action additively blends with the prior stage.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var isAdditive: Bool { get }
```

#### Discussion

When `true`, the action’s animation output is relative to an absolute base value, and the animation system blends the result additively with the prior blend stage.

Apply actions additively by configuring them to produce animation offsets, such as delta values.

The default value is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityaction/isadditive)*