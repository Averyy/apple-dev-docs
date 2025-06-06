# fulfill(withDateConnected:)

**Framework**: CallKit  
**Kind**: method

Reports the successful execution of the action at the specified time.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func fulfill(withDateConnected dateConnected: Date)
```

#### Discussion

Use this method instead of [`fulfill()`](cxaction/fulfill().md) to note a time other than the current time that the call connected.

## Parameters

- `dateConnected`: The time that the call was connected. A call is considered connected when both caller and callee can start communicating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxanswercallaction/fulfill(withdateconnected:))*