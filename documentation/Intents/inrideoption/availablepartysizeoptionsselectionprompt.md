# availablePartySizeOptionsSelectionPrompt

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The localized text to display for selecting party size options.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var availablePartySizeOptionsSelectionPrompt: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * availablePartySizeOptionsSelectionPrompt;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * availablePartySizeOptionsSelectionPrompt;
```

## Mentions

- [Generating a List of Ride Options](../../SiriKit/generating-a-list-of-ride-options.md)

## Discussion

Use this property to customize the text that Siri and Maps display to the user for party size selection. Display the text you provide as an option for the user to tap in the Siri or Maps interface. When tapped, display the party size options from the [`availablePartySizeOptions`](./availablepartysizeoptions.md) property so that the user can select one.

## See Also

### Specifying the Ride Information
- [var name: String](./name.md)
  The name of this ride option.
- [var estimatedPickupDate: Date](./estimatedpickupdate.md)
  The date and time when a ride of this type could be at the user’s location.
- [var disclaimerMessage: String?](./disclaimermessage.md)
  A localized disclaimer message to display to the user before confirming the ride.
- [var availablePartySizeOptions: [INRidePartySizeOption]?](./availablepartysizeoptions.md)
  An array of size options for the user to choose from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/availablepartysizeoptionsselectionprompt)*