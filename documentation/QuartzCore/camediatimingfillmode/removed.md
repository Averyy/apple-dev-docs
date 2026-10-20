# removed

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

The receiver is removed from the presentation when the animation is completed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let removed: CAMediaTimingFillMode
```

```c
extern CAMediaTimingFillMode const kCAFillModeRemoved;
```

## See Also

### Constants
- [static let forwards: CAMediaTimingFillMode](./forwards.md)
  The receiver remains visible in its final state when the animation is completed.
- [static let backwards: CAMediaTimingFillMode](./backwards.md)
  The receiver clamps values before zero to zero when the animation is completed.
- [static let both: CAMediaTimingFillMode](./both.md)
  The receiver clamps values at both ends of the object’s time space


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfillmode/removed)*