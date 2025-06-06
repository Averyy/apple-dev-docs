# instanceBlueOffset

**Framework**: Core Animation  
**Kind**: property

Defines the offset added to the blue component of the color for each replicated instance. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var instanceBlueOffset: Float { get set }
```

#### Discussion

The `instanceBlueOffset` is added to the blue color component of instance `k-1` to produce the modulation color of instance k.

Default is `0.0`.

## See Also

- [var instanceColor: CGColor?](careplicatorlayer/instancecolor.md)
  Defines the color used to multiply the source object. Animatable.
- [var instanceRedOffset: Float](careplicatorlayer/instanceredoffset.md)
  Defines the offset added to the red component of the color for each replicated instance. Animatable.
- [var instanceGreenOffset: Float](careplicatorlayer/instancegreenoffset.md)
  Defines the offset added to the green component of the color for each replicated instance. Animatable.
- [var instanceAlphaOffset: Float](careplicatorlayer/instancealphaoffset.md)
  Defines the offset added to the alpha component of the color for each replicated instance. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instanceblueoffset)*