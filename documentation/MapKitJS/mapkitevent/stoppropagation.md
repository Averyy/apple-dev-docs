# stopPropagation()

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Stops further propagation of the event.

**Availability**:
- MapKit JS 5.0+ - Deprecated in 6.0

> **Deprecated**: Removed in MapKit JS 6.0.0. Use standard `Event` instead.

## Declaration

```
stopPropagation(): void;
```

## Discussion

Unlike a DOM `Event`, a [`MapKitEvent`](../mapkitevent.md) doesn’t go through bubbling or capturing phases. When the propagation stops, the system doesn’t dispatch the event to any event listeners that the framework hasn’t called yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkitevent/stoppropagation)*