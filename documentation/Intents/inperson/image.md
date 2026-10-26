# image

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An image of the person.

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
var image: INImage? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INImage * image;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INImage * image;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

#### Discussion

Only show the person’s image to the user in appropriate situations. The value of this property is specified automatically at initialization time and can’t be changed later.

## See Also

### Accessing the person’s identity
- [var personHandle: INPersonHandle?](./personhandle.md)
  The unique handle that your app assigns to the person.
- [var isMe: Bool](./isme.md)
  A Boolean value indicating whether the person is the user of the device.
- [var aliases: [INPersonHandle]?](./aliases.md)
  The additional handles that Siri may use to identify the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/image)*