# animationDuration

**Framework**: SceneKit  
**Kind**: property

Returns the duration, in seconds, of all animations within the current transaction.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class var animationDuration: CFTimeInterval { get set }
```

## Mentions

- [Animating SceneKit Content](animating-scenekit-content.md)

#### Return Value

The animation duration, in seconds.

#### Discussion

The default duration is zero for transactions automatically created by SceneKit, and `0.25` for animations you create using the [`begin()`](scntransaction/begin().md) method.

## See Also

- [class var animationTimingFunction: CAMediaTimingFunction?](scntransaction/animationtimingfunction.md)
  Returns the timing function that SceneKit uses for all animations within this transaction group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/animationduration)*