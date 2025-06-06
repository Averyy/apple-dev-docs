# pendingTransactions

**Framework**: CallKit  
**Kind**: property

Incomplete transactions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var pendingTransactions: [CXTransaction] { get }
```

## See Also

- [func pendingCallActions(of: AnyClass, withCall: UUID) -> [CXCallAction]](cxprovider/pendingcallactions(of:withcall:).md)
  Returns all call actions in any pending transactions of the specified class for the specified call identifier that are incomplete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/pendingtransactions)*