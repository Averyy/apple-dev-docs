# animationTimingFunction

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Returns the timing function that SceneKit uses for all animations within this transaction group.

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
@NSCopying
class var animationTimingFunction: CAMediaTimingFunction? { get set }
```

```objc
@property (class, nonatomic, copy, nullable) CAMediaTimingFunction * animationTimingFunction;
```

## Return Value

The media timing function for the transaction’s animations.

## Discussion

Media timing functions, also known as *animation curves*, define the relationship between the elapsed time of an animation and its effect on a property. For example, the [`easeInEaseOut`](../../QuartzCore/camediatimingfunctionname/easeineaseout.md) function creates an effect that begins slowly, speeds up, and then finishes slowly.

## See Also

### Overriding Animation Duration and Timing
- [class var animationDuration: CFTimeInterval](./animationduration.md)
  Returns the duration, in seconds, of all animations within the current transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/animationtimingfunction)*