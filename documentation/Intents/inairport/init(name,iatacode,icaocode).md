# init(name:iataCode:icaoCode:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new airport object with the specified contents and attributes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(name: String?, iataCode: String?, icaoCode: String?)
```

```objc
- (instancetype) initWithName:(NSString *) name iataCode:(NSString *) iataCode icaoCode:(NSString *) icaoCode;
```

#### Return Value

A new airport object or `nil` if the initializer is unable to create the object.

## Parameters

- `name`: The name of the airport.
- `iataCode`: The three-letter International Air Transport Association (IATA) code for the airport.
- `icaoCode`: The four-letter International Civil Aviation Organization (ICAO) code for the airport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inairport/init(name:iatacode:icaocode:))*