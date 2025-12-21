# LookAroundErrorEvent

**Framework**: MapKit JS  
**Kind**: typealias

A custom event object that contains information about the error when starting a Look Around view.

**Availability**:
- MapKit JS 5.79+

## Declaration

```swift
type LookAroundErrorEvent = CustomEvent<{
    type: LookAroundErrorType;
    message: string;
}>;
```

#### Discussion

The event object describes the error with a [`LookAroundErrorType`](lookarounderrortype.md) value and a message.

## See Also

- [const LookAroundErrorType](lookarounderrortype.md)
  Values that describes errors than can occur when starting a Look Around view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/lookarounderrorevent)*