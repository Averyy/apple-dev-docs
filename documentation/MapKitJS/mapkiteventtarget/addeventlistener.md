# addEventListener(eventType, listener, thisObject)

**Framework**: MapKit JS  
**Kind**: method

Subscribes a listener function to an event type.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
addEventListener(
        eventType: string,
        listener: MapKitEventListener,
        thisObject?: object | null,
    ): boolean;
```

## Mentions

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)

#### Discussion

Unlike a DOM `EventTarget`, a [`MapKitEventTarget`](mapkiteventtarget.md) doesn’t go through bubbling or capturing phases. The system also interprets the third parameter differently from the DOM’s `EventTarget`.

## Parameters

- `type`: The type of event, for example, a  .
- `listener`: The callback function to invoke. MapKit JS passes   an   as its sole argument.
- `thisObject`: An object MapKit JS sets as the   keyword on the   function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkiteventtarget/addeventlistener)*