# DataDetector.Match.SemanticDetails.FlightNumber

**Framework**: DataDetection  
**Kind**: struct  
**Role**: Structure

The values the framework returns that represent an airline code and a flight number.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct FlightNumber
```

#### Discussion

The values the data detector returns represent the International Air Transport Association (IATA) code of the airline and the flight number.

## Parameters

- `FlightNumber`: A [`DataDetector.Match.SemanticDetails.FlightNumber`](./flightnumber.md) structure.

## Topics

### Characteristics of a flight number
- [let airlineCode: String](./flightnumber/airlinecode.md)
  A value that represents the International Air Transport Association (IATA) code of an airline.
- [let flightNumber: Int](./flightnumber/flightnumber.md)
  A value that represent the flight number, excluding the airline code.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/semanticdetails/flightnumber)*