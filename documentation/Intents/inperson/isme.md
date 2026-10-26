# isMe

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the person is the user of the device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var isMe: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) BOOL isMe;
```

*macOS*

```objc
@property (atomic, assign, readonly) BOOL isMe;
```

#### Discussion

It’s essential that you set [`isMe`](./isme.md) to [`true`](../../Swift/true.md) for the current device user when creating an [`INPerson`](../inperson.md) object for use with [Messaging](../../SiriKit/messaging.md) intents. For example, if the sender of an outgoing message is also the user of the device, set [`isMe`](./isme.md) to [`true`](../../Swift/true.md). Similarly, when creating the recipient array for an incoming message—which should include the current device user—set [`isMe`](./isme.md) to [`true`](../../Swift/true.md) for the person in the recipient list that is the current device user, and set [`isMe`](./isme.md) to [`false`](../../Swift/false.md) for all other recipients.

To set [`isMe`](./isme.md), call the [`init(personHandle:nameComponents:displayName:image:contactIdentifier:customIdentifier:isMe:)`](./init%28personhandle,namecomponents,displayname,image,contactidentifier,customidentifier,isme%29.md) method when creating the [`INPerson`](../inperson.md) object.

## See Also

### Accessing the person’s identity
- [var personHandle: INPersonHandle?](./personhandle.md)
  The unique handle that your app assigns to the person.
- [var image: INImage?](./image.md)
  An image of the person.
- [var aliases: [INPersonHandle]?](./aliases.md)
  The additional handles that Siri may use to identify the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/isme)*