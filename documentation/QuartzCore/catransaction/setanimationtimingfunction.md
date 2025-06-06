# setAnimationTimingFunction(_:)

**Framework**: Core Animation  
**Kind**: method

Sets the timing function used for all animations within this transaction group.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?)
```

#### Discussion

This is a convenience method that sets the [`CAMediaTimingFunction`](camediatimingfunction.md) for the [`value(forKey:)`](catransaction/value(forkey:).md) value of  the  [`kCATransactionAnimationTimingFunction`](kcatransactionanimationtimingfunction.md) key.

## Parameters

- `function`: An instance of  .

## See Also

- [class func animationDuration() -> CFTimeInterval](catransaction/animationduration.md)
  Returns the animation duration used by all animations within this transaction group.
- [class func setAnimationDuration(CFTimeInterval)](catransaction/setanimationduration(_:).md)
  Sets the animation duration used by all animations within this transaction group.
- [class func animationTimingFunction() -> CAMediaTimingFunction?](catransaction/animationtimingfunction.md)
  Returns the timing function used for all animations within this transaction group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/setanimationtimingfunction(_:))*