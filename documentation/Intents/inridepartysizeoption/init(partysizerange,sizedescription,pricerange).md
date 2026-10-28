# init(partySizeRange:sizeDescription:priceRange:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the object with the specified party size and price ranges.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(partySizeRange: NSRange, sizeDescription: String, priceRange: INPriceRange?)
```

```objc
- (instancetype) initWithPartySizeRange:(NSRange) partySizeRange sizeDescription:(NSString *) sizeDescription priceRange:(INPriceRange *) priceRange;
```

## Return Value

An initialized party size option object or `nil` if the object could not be created.

## Parameters

- `partySizeRange`: The party size for which the specified pricing applies. The `location` value of the range contains the minimum number of people. Adding the `location` and `length` values results in the maximum number of people. For example, a range value of (1, 0) represents a single person and a range value of (1, 2) represents 1 to 3 people.
- `sizeDescription`: The user-visible description of the party size. Use this parameter to specify a localized string that conveys the party size information to the current user. For example, for a range of 1 to 3 people, you might specify the string “1 to 3 passengers”.
- `priceRange`: The price range for a party of this size. Include this information when the number of passengers affects the price of the ride. Specify `nil` if the party size does not affect the price of the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inridepartysizeoption/init(partysizerange:sizedescription:pricerange:))*