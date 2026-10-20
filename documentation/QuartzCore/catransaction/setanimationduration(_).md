# setAnimationDuration(_:)

**Framework**: Core Animation  
**Kind**: method

Sets the animation duration used by all animations within this transaction group.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func setAnimationDuration(_ dur: CFTimeInterval)
```

#### Discussion

You can also set the animation duration for a specific transaction object by calling the [`setValue(_:forKey:)`](catransaction/setvalue(_:forkey:).md) method of that object and specifying the [`kCATransactionAnimationDuration`](kcatransactionanimationduration.md) key.

## Parameters

- `dur`: An interval of time used as the duration.

## See Also

- [class func animationDuration() -> CFTimeInterval](catransaction/animationduration.md)
  Returns the animation duration used by all animations within this transaction group.
- [class func animationTimingFunction() -> CAMediaTimingFunction?](catransaction/animationtimingfunction.md)
  Returns the timing function used for all animations within this transaction group.
- [class func setAnimationTimingFunction(CAMediaTimingFunction?)](catransaction/setanimationtimingfunction(_:).md)
  Sets the timing function used for all animations within this transaction group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/setanimationduration(_:))*