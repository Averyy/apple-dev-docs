# init(send:receive:components:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated `NSPortMessage` object to send given data on a given port and to receiver replies on another given port.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init(send sendPort: Port?, receive replyPort: Port?, components: [Any]?)
```

#### Return Value

An `NSPortMessage` object initialized to send `components` on `sendPort` and to receiver replies on `receivePort`.

#### Discussion

An `NSPortMessage` object initialized with this method has a message identifier of 0.

This is the designated initializer for `NSPortMessage`.

## Parameters

- `sendPort`: The port on which the message is sent.
- `replyPort`: The port on which replies to the message arrive.
- `components`: The data to send in the message.   should contain only   and   objects, and the contents of the   objects should be in network byte order.

## See Also

- [var msgid: UInt32](portmessage/msgid.md)
  Returns the identifier for the receiver.
- [Distributed Objects Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DistrObjects/DistrObjects.html#//apple_ref/doc/uid/10000102i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/portmessage/init(send:receive:components:))*