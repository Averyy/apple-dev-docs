# kCATransactionAnimationTimingFunction

**Framework**: Core Animation  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCATransactionAnimationTimingFunction: String
```

```c
extern NSString * const kCATransactionAnimationTimingFunction;
```

## Discussion

An instance of [`CAMediaTimingFunction`](./camediatimingfunction.md) that overrides the timing function for all animations triggered within the transaction group.

## See Also

### Constants
- [let kCATransactionAnimationDuration: String](./kcatransactionanimationduration.md)
  Duration, in seconds, for animations triggered within the transaction group.
- [let kCATransactionDisableActions: String](./kcatransactiondisableactions.md)
  A key whose value indicates whether implicit actions for property changes made within the transaction group are suppressed.
- [let kCATransactionCompletionBlock: String](./kcatransactioncompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/kcatransactionanimationtimingfunction)*