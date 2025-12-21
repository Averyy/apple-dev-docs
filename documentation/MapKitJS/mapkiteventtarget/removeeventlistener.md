# removeEventListener(eventType, listener, thisObject)

**Framework**: MapKit JS  
**Kind**: method

Unsubscribes a listener function from an event type.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
removeEventListener(
        eventType?: string,
        listener?: MapKitEventListener,
        thisObject?: object | null,
    ): boolean;
```

## Mentions

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)

#### Discussion

Unlike a DOM `EventTarget`, a [`MapKitEventTarget`](mapkiteventtarget.md) doesn’t go through bubbling or capturing phases. The system also interprets the second and the third parameters differently from the DOM’s `EventTarget`.

## Parameters

- `type`: The type of event, for example, a  .
- `listener`: The callback function to remove. Not setting this parameter removes all listeners of the specified type.
- `thisObject`: An object MapKit JS sets as the   keyword on the   function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkiteventtarget/removeeventlistener)*