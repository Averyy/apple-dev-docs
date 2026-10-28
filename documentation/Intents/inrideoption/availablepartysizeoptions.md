# availablePartySizeOptions

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of size options for the user to choose from.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var availablePartySizeOptions: [INRidePartySizeOption]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INRidePartySizeOption *> * availablePartySizeOptions;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INRidePartySizeOption *> * availablePartySizeOptions;
```

## Mentions

- [Generating a List of Ride Options](../../SiriKit/generating-a-list-of-ride-options.md)

## Discussion

Use this property to specify the carrying capacities for vehicles of this type and any capacity-based pricing information.

## See Also

### Specifying the Ride Information
- [var name: String](./name.md)
  The name of this ride option.
- [var estimatedPickupDate: Date](./estimatedpickupdate.md)
  The date and time when a ride of this type could be at the user’s location.
- [var disclaimerMessage: String?](./disclaimermessage.md)
  A localized disclaimer message to display to the user before confirming the ride.
- [var availablePartySizeOptionsSelectionPrompt: String?](./availablepartysizeoptionsselectionprompt.md)
  The localized text to display for selecting party size options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/availablepartysizeoptions)*