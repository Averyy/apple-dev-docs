# init(carName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes an intent to get the lock status of the named car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(carName: INSpeakableString?)
```

```objc
- (instancetype) initWithCarName:(INSpeakableString *) carName;
```

#### Return Value

A newly initialized `INGetCarLockStatusIntent` object.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, Siri creates instances when a user asks for the lock status of the car. However, you can use this method during testing to create intent objects to validate your intent-handling code paths.

## Parameters

- `carName`: A name that identifies the user’s car. If `nil`, the intent is instantiated with a [`carName`](./carname.md) property containing the string `myCar`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarlockstatusintent/init(carname:))*