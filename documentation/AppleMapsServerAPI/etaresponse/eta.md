# EtaResponse.Eta

**Framework**: Apple Maps Server API  
**Kind**: dictionary

An object that contains details about an estimated time of arrival (ETA).

**Availability**:
- Apple Maps Server API 1.2+

## Declaration

```swift
object EtaResponse.Eta
```

## Properties

- `destination` (Location): The destination as a [`Location`](location.md).
- `distanceMeters` (integer): The distance in meters to the destination.
- `expectedTravelTimeSeconds` (integer): The estimated travel time in seconds, including delays due to traffic.
- `staticTravelTimeSeconds` (integer): The expected travel time, in seconds, without traffic.
- `transportType` (string): A string that represents the mode of transportation for this ETA, which is one of:


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemapsserverapi/etaresponse/eta)*