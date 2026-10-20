# instanceAlphaOffset

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines the offset added to the alpha component of the color for each replicated instance. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var instanceAlphaOffset: Float { get set }
```

```objc
@property float instanceAlphaOffset;
```

#### Discussion

The `instanceAlphaOffset` is added to the alpha color component of instance `k-1` to produce the modulation color of instance k.

Default is `0.0`.

## See Also

### Accessing Instance Color Values
- [var instanceColor: CGColor?](./instancecolor.md)
  Defines the color used to multiply the source object. Animatable.
- [var instanceRedOffset: Float](./instanceredoffset.md)
  Defines the offset added to the red component of the color for each replicated instance. Animatable.
- [var instanceGreenOffset: Float](./instancegreenoffset.md)
  Defines the offset added to the green component of the color for each replicated instance. Animatable.
- [var instanceBlueOffset: Float](./instanceblueoffset.md)
  Defines the offset added to the blue component of the color for each replicated instance. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instancealphaoffset)*