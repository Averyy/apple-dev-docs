# estimatedPickupDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date and time when a ride of this type could be at the user’s location.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var estimatedPickupDate: Date { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite) NSDate * estimatedPickupDate;
```

*macOS*

```objc
@property (atomic, copy, readwrite) NSDate * estimatedPickupDate;
```

#### Discussion

Use this property to specify the time at which you could pick up the user using a ride of this type. Always try to specify a date and time that is as close to the current time as possible. The [`init(name:estimatedPickupDate:)`](./init%28name,estimatedpickupdate%29.md) method sets this property at initialization time.

## See Also

### Specifying the Ride Information
- [var name: String](./name.md)
  The name of this ride option.
- [var disclaimerMessage: String?](./disclaimermessage.md)
  A localized disclaimer message to display to the user before confirming the ride.
- [var availablePartySizeOptions: [INRidePartySizeOption]?](./availablepartysizeoptions.md)
  An array of size options for the user to choose from.
- [var availablePartySizeOptionsSelectionPrompt: String?](./availablepartysizeoptionsselectionprompt.md)
  The localized text to display for selecting party size options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/estimatedpickupdate)*