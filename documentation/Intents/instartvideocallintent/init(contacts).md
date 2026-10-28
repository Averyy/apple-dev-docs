# init(contacts:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the start video call intent object with the specified contacts.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
init(contacts: [INPerson]?)
```

```objc
- (instancetype) initWithContacts:(NSArray<INPerson *> *) contacts;
```

## Return Value

An initialized intent or `nil` if the object could not be created.

## Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when the user asks to place a video call to another user. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `contacts`: An array of [`INPerson`](../inperson.md) objects representing the users to call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintent/init(contacts:))*