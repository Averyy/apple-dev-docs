# fulfill(withDateEnded:)

**Framework**: CallKit  
**Kind**: method  
**Role**: Instance Method

Reports the successful execution of the action at the specified time.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func fulfill(withDateEnded dateEnded: Date)
```

```objc
- (void) fulfillWithDateEnded:(NSDate *) dateEnded;
```

#### Discussion

Use this method instead of [`fulfill()`](../cxaction/fulfill%28%29.md) to note a time other than the current time that the call ended.

## Parameters

- `dateEnded`: The time that the call was ended. A call is considered ended when the user disconnects or all other callers disconnect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxendcallaction/fulfill(withdateended:))*