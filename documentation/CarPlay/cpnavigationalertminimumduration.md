# CPNavigationAlertMinimumDuration

**Framework**: CarPlay  
**Kind**: var  
**Role**: Global Variable

A constant that defines the minimum amount of time that an alert is visible.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var CPNavigationAlertMinimumDuration: TimeInterval { get }
```

```c
static const NSTimeInterval CPNavigationAlertMinimumDuration;
```

#### Discussion

The minimum duration is in effect when [`duration`](./cpnavigationalert/duration.md) is not zero.

## See Also

### Getting the Alert Duration
- [var duration: TimeInterval](./cpnavigationalert/duration.md)
  The amount of time, in seconds, that the alert is visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnavigationalertminimumduration)*