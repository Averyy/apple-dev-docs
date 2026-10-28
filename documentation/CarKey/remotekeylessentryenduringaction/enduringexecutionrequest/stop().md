# stop()

**Framework**: CarKey  
**Kind**: method  
**Role**: Instance Method

Sends a request to stop a previously started action.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.3+ - Deprecated in 15.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`perform(_:continuationStrategy:)`](../../carkeyremotecontrolsession/perform%28_,continuationstrategy%29.md) instead.

## Declaration

```swift
final func stop() throws
```

## Discussion

This method sends the cancellation request asynchronously to the vehicle. If you call the results method again, the method delivers the results of the cancellation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/remotekeylessentryenduringaction/enduringexecutionrequest/stop())*