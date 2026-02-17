# startNavigationSession(for:)

**Framework**: CarPlay  
**Kind**: method

Begins navigational guidance for a trip.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func startNavigationSession(for trip: CPTrip) -> CPNavigationSession
```

#### Return Value

A navigation session for the specified trip.

#### Discussion

Keep a reference to the navigation session to perform guidance updates.

## Parameters

- `trip`: The trip to provide guidance for.

## See Also

- [class CPNavigationSession](cpnavigationsession.md)
  An object that represents an active route guidance session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/startnavigationsession(for:))*