# init(carName:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a car power intent with the provided car name.

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

A newly initialized `INGetCarPowerLevelStatusIntent` object.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, Siri creates instances when the user asks for the car’s power level. However, you can use this method during testing to create intent objects to validate your intent-handling code paths.

## Parameters

- `carName`: A name that identifies the user’s car. If `nil`, the intent is instantiated with a [`carName`](./carname.md) property containing the string `myCar`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarpowerlevelstatusintent/init(carname:))*