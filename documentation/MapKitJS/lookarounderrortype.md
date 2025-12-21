# LookAroundErrorType

**Framework**: MapKit JS  
**Kind**: enum

Values that describes errors than can occur when starting a Look Around view.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
const LookAroundErrorType: Readonly<{
    readonly AvailabilityError: "availability-error";
    readonly BrowserError: "browser-error";
    readonly ServiceError: "service-error";
    readonly UnknownError: "unknown-error";
}>
```

## Topics

### Enumeration Cases
- [AvailabilityError](lookarounderrortype/availabilityerror.md)
  An error type that indicates the requested Look Around view isn’t available.
- [BrowserError](lookarounderrortype/browsererror.md)
  An error type that indicates the browser doesn’t support the Look Around experience.
- [ServiceError](lookarounderrortype/serviceerror.md)
  An error type that indicates the service supporting the Look Around view isn’t available.
- [UnknownError](lookarounderrortype/unknownerror.md)
  An error type that indicates the Look Around view encountered an unknown error.
### Type Aliases
- [type LookAroundErrorType](lookarounderrortype/lookarounderrortype.md)
  A type alias that represents the values of the Look Around error type.

## See Also

- [type LookAroundErrorEvent](lookarounderrorevent.md)
  A custom event object that contains information about the error when starting a Look Around view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/lookarounderrortype)*