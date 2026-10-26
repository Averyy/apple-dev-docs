# name

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of this ride option.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var name: String { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite) NSString * name;
```

*macOS*

```objc
@property (atomic, copy, readwrite) NSString * name;
```

#### Discussion

Siri displays this string to the user during the ride selection process and when confirming the ride. The [`init(name:estimatedPickupDate:)`](./init%28name,estimatedpickupdate%29.md) method sets this property at initialization time.

## See Also

### Specifying the Ride Information
- [var estimatedPickupDate: Date](./estimatedpickupdate.md)
  The date and time when a ride of this type could be at the user’s location.
- [var disclaimerMessage: String?](./disclaimermessage.md)
  A localized disclaimer message to display to the user before confirming the ride.
- [var availablePartySizeOptions: [INRidePartySizeOption]?](./availablepartysizeoptions.md)
  An array of size options for the user to choose from.
- [var availablePartySizeOptionsSelectionPrompt: String?](./availablepartysizeoptionsselectionprompt.md)
  The localized text to display for selecting party size options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/name)*