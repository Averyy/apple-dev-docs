# animationDuration()

**Framework**: Core Animation  
**Kind**: method

Returns the animation duration used by all animations within this transaction group.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func animationDuration() -> CFTimeInterval
```

#### Return Value

An interval of time used as the duration.

#### Discussion

You can retrieve the animation duration for a specific transaction by calling the [`value(forKey:)`](catransaction/value(forkey:).md) method of the transaction object and asking for the [`kCATransactionAnimationDuration`](kcatransactionanimationduration.md) key.

## See Also

- [class func setAnimationDuration(CFTimeInterval)](catransaction/setanimationduration(_:).md)
  Sets the animation duration used by all animations within this transaction group.
- [class func animationTimingFunction() -> CAMediaTimingFunction?](catransaction/animationtimingfunction.md)
  Returns the timing function used for all animations within this transaction group.
- [class func setAnimationTimingFunction(CAMediaTimingFunction?)](catransaction/setanimationtimingfunction(_:).md)
  Sets the timing function used for all animations within this transaction group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/animationduration())*