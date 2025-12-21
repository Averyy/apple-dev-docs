# stopPropagation()

**Framework**: MapKit JS  
**Kind**: method

Stops further propagation of the event.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
stopPropagation(): void;
```

#### Discussion

Unlike a DOM `Event`, a [`MapKitEvent`](mapkitevent.md) doesn’t go through bubbling or capturing phases. When the propagation stops, the system doesn’t dispatch the event to any event listeners that the framework hasn’t called yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkitevent/stoppropagation)*