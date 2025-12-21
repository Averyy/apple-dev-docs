# provider(_:execute:)

**Framework**: CallKit  
**Kind**: method

Called when a transaction is executed by a call controller.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
optional func provider(_ provider: CXProvider, execute transaction: CXTransaction) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the `transaction` was handled; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Most delegates should not need to provide an implementation for this method. However, a delegate can implement this method to customize how transactions are handled. This method returns [`true`](https://developer.apple.com/documentation/Swift/true) to indicate that the custom implementation handled the transaction and returns [`false`](https://developer.apple.com/documentation/Swift/false) to have the provider execute the transaction normally—as if the delegate did not implement this method. For example, given a transaction consisting of a [`CXSetHeldCallAction`](cxsetheldcallaction.md) object and a [`CXSetGroupCallAction`](cxsetgroupcallaction.md) object, the delegate may override this method to inject a 30 second wait and play hold music to the caller.

## Parameters

- `provider`: The telephony provider.
- `transaction`: Contains the upcoming actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxproviderdelegate/provider(_:execute:))*