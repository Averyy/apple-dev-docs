# fulfill(withDateStarted:)

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
func fulfill(withDateStarted dateStarted: Date)
```

#### Discussion

Use this method instead of [`fulfill()`](cxaction/fulfill().md) to note a time other than the current time that the call started.

## Parameters

- `dateStarted`: The time that the call was started. A call is considered started when its invitation has been sent to the remote callee.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxstartcallaction/fulfill(withdatestarted:))*