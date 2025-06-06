# Fill Modes

**Framework**: Core Animation

These constants determine how the timed object behaves once its active duration has completed. They are used with the [`fillMode`](camediatiming/fillmode.md) property.

## Topics

### Constants
- [static let removed: CAMediaTimingFillMode](camediatimingfillmode/removed.md)
  The receiver is removed from the presentation when the animation is completed.
- [static let forwards: CAMediaTimingFillMode](camediatimingfillmode/forwards.md)
  The receiver remains visible in its final state when the animation is completed.
- [static let backwards: CAMediaTimingFillMode](camediatimingfillmode/backwards.md)
  The receiver clamps values before zero to zero when the animation is completed.
- [static let both: CAMediaTimingFillMode](camediatimingfillmode/both.md)
  The receiver clamps values at both ends of the object’s time space


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/fill-modes)*