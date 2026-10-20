# identifier

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A unique value for the ducker.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * identifier;
```

## See Also

### Configuring Volume Reduction
- [var gain: Double](./gain.md)
  The amount of volume reduction.
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

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseducker/identifier)*