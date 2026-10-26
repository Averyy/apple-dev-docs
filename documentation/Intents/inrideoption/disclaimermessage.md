# disclaimerMessage

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A localized disclaimer message to display to the user before confirming the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var disclaimerMessage: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * disclaimerMessage;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * disclaimerMessage;
```

#### Discussion

Use this property to specify disclaimers about the ride you are offering. For example, you might use this property to present terms and conditions of the ride or to emphasize specific conditions such as when the user might share the ride with other users.

## See Also

### Specifying the Ride Information
- [var name: String](./name.md)
  The name of this ride option.
- [var estimatedPickupDate: Date](./estimatedpickupdate.md)
  The date and time when a ride of this type could be at the user’s location.
- [var availablePartySizeOptions: [INRidePartySizeOption]?](./availablepartysizeoptions.md)
  An array of size options for the user to choose from.
- [var availablePartySizeOptionsSelectionPrompt: String?](./availablepartysizeoptionsselectionprompt.md)
  The localized text to display for selecting party size options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/disclaimermessage)*