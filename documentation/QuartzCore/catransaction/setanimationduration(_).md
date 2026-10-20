# setAnimationDuration(_:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (void) setAnimationDuration:(CFTimeInterval) dur;
```

#### Discussion

You can also set the animation duration for a specific transaction object by calling the [`setValue(_:forKey:)`](./setvalue%28_,forkey%29.md) method of that object and specifying the [`kCATransactionAnimationDuration`](../kcatransactionanimationduration.md) key.

## Parameters

- `dur`: An interval of time used as the duration.

## See Also

### Overriding Animation Duration and Timing
- [class func animationDuration() -> CFTimeInterval](./animationduration%28%29.md)
  Returns the animation duration used by all animations within this transaction group.
- [class func animationTimingFunction() -> CAMediaTimingFunction?](./animationtimingfunction%28%29.md)
  Returns the timing function used for all animations within this transaction group.
- [class func setAnimationTimingFunction(CAMediaTimingFunction?)](./setanimationtimingfunction%28_%29.md)
  Sets the timing function used for all animations within this transaction group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransaction/setanimationduration(_:))*