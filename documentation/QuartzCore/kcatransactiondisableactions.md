# kCATransactionDisableActions

**Framework**: Core Animation  
**Kind**: var

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

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), implicit actions for property changes made within the transaction group are suppressed.  The value for this key must be an instance of [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber).

## See Also

- [let kCATransactionAnimationDuration: String](kcatransactionanimationduration.md)
  Duration, in seconds, for animations triggered within the transaction group.
- [let kCATransactionAnimationTimingFunction: String](kcatransactionanimationtimingfunction.md)
- [let kCATransactionCompletionBlock: String](kcatransactioncompletionblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/kcatransactiondisableactions)*