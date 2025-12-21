# send(before:)

**Framework**: Foundation  
**Kind**: method

Attempts to send the message before the specified date.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func send(before date: Date) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the operation is successful, otherwise [`false`](https://developer.apple.com/documentation/Swift/false) (for example, if the operation times out).

#### Discussion

If an error other than a time out occurs, this method could raise an `NSInvalidSendPortException`, `NSInvalidReceivePortException`, or an `NSPortSendException`, depending on the type of send port and the type of error.

If the message cannot be sent immediately, the sending thread blocks until either the message is sent or `aDate` is reached. Sent messages are queued to minimize blocking, but failure can occur if multiple messages are sent to a port faster than the port’s owner can receive them, causing the queue to fill up. Therefore, select a value for `aDate` that provides enough time for the message to be processed before the next message is sent. See the [`Port`](port.md) class specification for information on receiving a port message.

## Parameters

- `date`: The instant before which the message should be sent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/portmessage/send(before:))*