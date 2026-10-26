# carName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A name that identifies the user’s car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var carName: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * carName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * carName;
```

#### Discussion

Use this property to identify the correct car. If Siri does not detect a car name, it sets this property to `myCar`.

Apps should register the names, makes, and models of cars as user vocabulary or global vocabulary. For example, an auto manufacturer could register the makes and models of the supported cars as global vocabulary, while an app may register a user’s nickname for a car as user vocabulary. Registering the car names helps the system identify those cars when users speak the car names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintent/carname)*