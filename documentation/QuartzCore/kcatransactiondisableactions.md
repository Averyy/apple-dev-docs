# kCATransactionDisableActions

**Framework**: Core Animation  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates whether implicit actions for property changes made within the transaction group are suppressed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let kCATransactionDisableActions: String
```

```c
extern NSString * const kCATransactionDisableActions;
```

#### Discussion

If [`true`](../Swift/true.md), implicit actions for property changes made within the transaction group are suppressed.  The value for this key must be an instance of [`NSNumber`](../Foundation/nsnumber.md).

## See Also

### Constants
- [let kCATransactionAnimationDuration: String](./kcatransactionanimationduration.md)
  Duration, in seconds, for animations triggered within the transaction group.
- [let kCATransactionAnimationTimingFunction: String](./kcatransactionanimationtimingfunction.md)
- [let kCATransactionCompletionBlock: String](./kcatransactioncompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/kcatransactiondisableactions)*