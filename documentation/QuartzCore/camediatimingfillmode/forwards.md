# forwards

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

The receiver remains visible in its final state when the animation is completed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let forwards: CAMediaTimingFillMode
```

```c
extern CAMediaTimingFillMode const kCAFillModeForwards;
```

## See Also

### Constants
- [static let removed: CAMediaTimingFillMode](./removed.md)
  The receiver is removed from the presentation when the animation is completed.
- [static let backwards: CAMediaTimingFillMode](./backwards.md)
  The receiver clamps values before zero to zero when the animation is completed.
- [static let both: CAMediaTimingFillMode](./both.md)
  The receiver clamps values at both ends of the object’s time space
- [kCAFillModeFrozen](../kcafillmodefrozen.md)
  The mode was deprecated before OS X v10.5 shipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfillmode/forwards)*