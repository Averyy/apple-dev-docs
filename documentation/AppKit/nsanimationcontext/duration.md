# duration

**Framework**: AppKit  
**Kind**: property

The duration used by animations created as a result of setting new values for an animatable property.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var duration: TimeInterval { get set }
```

#### Discussion

Any animations that occur as a result of setting the values of animatable properties in the current context will run for this duration.

## See Also

- [var timingFunction: CAMediaTimingFunction?](nsanimationcontext/timingfunction.md)
  The timing function used for all animations within this animation proxy group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationcontext/duration)*