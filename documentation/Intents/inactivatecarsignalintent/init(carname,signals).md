# init(carName:signals:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes an intent to trigger audio or visual signals from the car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
init(carName: INSpeakableString?, signals: INCarSignalOptions = [])
```

```objc
- (instancetype) initWithCarName:(INSpeakableString *) carName signals:(INCarSignalOptions) signals;
```

#### Return Value

A newly initialized `INActivateCarSignalIntent` object.

#### Discussion

Normally, you do not create instances of this class yourself. Instead, Siri creates instances when the user asks for an audible or visual signal from the car. However, you can use this method during testing to create intent objects to validate your intent-handling code paths.

## Parameters

- `carName`: A name that identifies the user’s car. If `nil`, the intent is instantiated with a [`carName`](./carname.md) property containing the string `myCar`.
- `signals`: The set of signals to be activated. For a list of valid signals, see [`INCarSignalOptions`](../incarsignaloptions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintent/init(carname:signals:))*