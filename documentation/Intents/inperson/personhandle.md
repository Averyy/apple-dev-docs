# personHandle

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique handle that your app assigns to the person.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var personHandle: INPersonHandle? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPersonHandle * personHandle;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPersonHandle * personHandle;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

#### Discussion

The value of this property is an object that uniquely identifies the user to your app. For example, you might provide a handle containing an email address, a phone number, or an account name associated with the user. Siri might show this information when asking the user to choose from among several people with similar names.

## See Also

### Accessing the person’s identity
- [var image: INImage?](./image.md)
  An image of the person.
- [var isMe: Bool](./isme.md)
  A Boolean value indicating whether the person is the user of the device.
- [var aliases: [INPersonHandle]?](./aliases.md)
  The additional handles that Siri may use to identify the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/personhandle)*