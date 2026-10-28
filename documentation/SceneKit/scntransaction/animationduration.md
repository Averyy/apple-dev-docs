# animationDuration

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Returns the duration, in seconds, of all animations within the current transaction.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class var animationDuration: CFTimeInterval { get set }
```

```objc
@property (class, nonatomic) CFTimeInterval animationDuration;
```

## Mentions

- [Animating SceneKit Content](../animating-scenekit-content.md)

## Return Value

The animation duration, in seconds.

## Discussion

The default duration is zero for transactions automatically created by SceneKit, and `0.25` for animations you create using the [`begin()`](./begin%28%29.md) method.

## See Also

### Overriding Animation Duration and Timing
- [class var animationTimingFunction: CAMediaTimingFunction?](./animationtimingfunction.md)
  Returns the timing function that SceneKit uses for all animations within this transaction group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/animationduration)*