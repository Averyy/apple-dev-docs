# ObservationIgnored()

**Framework**: Observation  
**Kind**: macro

Disables observation tracking of a property.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@attached
(accessor) macro ObservationIgnored()
```

#### Overview

By default, an object can observe any property of an observable type that is accessible to the observing object. To prevent observation of an accessible property, attach the `ObservationIgnored` macro to the property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/observation/observationignored())*