# gain

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The amount of volume reduction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var gain: Double { get }
```

```objc
@property (nonatomic, readonly) double gain;
```

#### Discussion

When source and target sounds play simultaneously, the value of this property determines the amount that the listener can hear the target sound.  A value of `0` results in full attenuation, and `1` results in no attenuation. The framework clamps the value to the range between `0` and `1`.

## See Also

### Configuring Volume Reduction
- [var identifier: String](./identifier.md)
  A unique value for the ducker.
- [var isActive: Bool](./isactive.md)
  A Boolean value that determines whether the ducker reduces sound.
- [var attackTime: Double](./attacktime.md)
  The amount of time for sound reduction to reach maximum strength.
- [var attackCurve: PHASECurveType](./attackcurve.md)
  A mathematical curve that shapes transition progress as sound reduction begins.
- [var releaseTime: Double](./releasetime.md)
  The amount of time to transition from maximum sound reduction to no reduction.
- [var releaseCurve: PHASECurveType](./releasecurve.md)
  A mathematical curve that shapes transition progress as sound reduction ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseducker/gain)*