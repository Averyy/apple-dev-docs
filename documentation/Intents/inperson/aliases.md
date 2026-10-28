# aliases

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The additional handles that Siri may use to identify the person.

## Declaration

```swift
var aliases: [INPersonHandle]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPersonHandle *> * aliases;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPersonHandle *> * aliases;
```

## Discussion

Each [`INPersonHandle`](../inpersonhandle.md) in this property represents another way of identifying the user to your app. Person handles contain information such as phone numbers or email addresses that are unique to the user.

## See Also

### Accessing the person’s identity
- [var personHandle: INPersonHandle?](./personhandle.md)
  The unique handle that your app assigns to the person.
- [var image: INImage?](./image.md)
  An image of the person.
- [var isMe: Bool](./isme.md)
  A Boolean value indicating whether the person is the user of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/aliases)*