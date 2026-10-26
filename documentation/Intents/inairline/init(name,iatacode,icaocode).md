# init(name:iataCode:icaoCode:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a new airline object with the specified contents and attributes.

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

A new airline object or `nil` if the initializer is unable to create the object.

## Parameters

- `name`: The name of the airline.
- `iataCode`: The two-letter International Air Transport Association (IATA) code for the airline.
- `icaoCode`: The three-letter International Civil Aviation Organization (ICAO) code for the airline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inairline/init(name:iatacode:icaocode:))*