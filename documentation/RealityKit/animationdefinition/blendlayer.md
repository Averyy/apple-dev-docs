# blendLayer

**Framework**: RealityKit  
**Kind**: property  
**Required**: Yes

The order in which the framework composites the animation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var blendLayer: Int32 { get set }
```

#### Discussion

The framework applies multiple animations on the same target in ascending order of this property’s value. Animations in a lower layer run before animations in a higher layer. Animations that share the same value apply in the order that they execute.

## See Also

- [var name: String](animationdefinition/name.md)
  A textual name for the animation.
- [var bindTarget: BindTarget](animationdefinition/bindtarget.md)
  A textual name that identifies the particular property that animates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationdefinition/blendlayer)*