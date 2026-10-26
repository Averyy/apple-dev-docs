# init(name:estimatedPickupDate:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes and returns a ride option object with the specified name and pickup information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(name: String, estimatedPickupDate: Date)
```

```objc
- (instancetype) initWithName:(NSString *) name estimatedPickupDate:(NSDate *) estimatedPickupDate;
```

#### Return Value

An initialized ride option object or `nil` if the object could not be initialized.

#### Discussion

After initializing the object, fill in the other properties of the newly created object before adding it to your response object.

## Parameters

- `name`: The name of the ride option as a user-readable string. The system displays this string to the user during the ride selection process and when confirming the ride. Use this string to provide a unique description of the ride being offered.
- `estimatedPickupDate`: The estimated time of arrival for the ride at the user’s location. This information is presented to the user during the ride selection process.

## See Also

### Initializing a Ride Option
- [init?(coder: NSCoder)](./init%28coder%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrideoption/init(name:estimatedpickupdate:))*