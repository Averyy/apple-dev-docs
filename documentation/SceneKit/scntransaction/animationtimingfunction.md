# animationTimingFunction

**Framework**: SceneKit  
**Kind**: property

Returns the timing function that SceneKit uses for all animations within this transaction group.

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
@NSCopying
class var animationTimingFunction: CAMediaTimingFunction? { get set }
```

#### Return Value

The media timing function for the transaction’s animations.

#### Discussion

Media timing functions, also known as , define the relationship between the elapsed time of an animation and its effect on a property. For example, the [`easeInEaseOut`](https://developer.apple.com/documentation/QuartzCore/CAMediaTimingFunctionName/easeInEaseOut) function creates an effect that begins slowly, speeds up, and then finishes slowly.

## See Also

- [class var animationDuration: CFTimeInterval](scntransaction/animationduration.md)
  Returns the duration, in seconds, of all animations within the current transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntransaction/animationtimingfunction)*