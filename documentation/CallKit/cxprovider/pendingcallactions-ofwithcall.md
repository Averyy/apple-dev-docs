# pendingCallActions(of:withCall:)

**Framework**: CallKit  
**Kind**: method

Returns all call actions in any pending transactions of the specified class for the specified call identifier that are incomplete.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func pendingCallActions(of callActionClass: AnyClass, withCall callUUID: UUID) -> [CXCallAction]
```

#### Return Value

An array of call actions of the specified class for the specified call identifier.

## Parameters

- `callActionClass`: The desired   subclass of returned actions.
- `callUUID`: The desired call identifier for returned actions.

## See Also

- [var pendingTransactions: [CXTransaction]](cxprovider/pendingtransactions.md)
  Incomplete transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxprovider/pendingcallactions(of:withcall:))*