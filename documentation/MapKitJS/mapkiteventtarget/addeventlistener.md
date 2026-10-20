# addEventListener(eventType, listener, thisObject)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Subscribes a listener function to an event type.

**Availability**:
- MapKit JS 5.0+ - Deprecated in 6.0

> **Deprecated**: Removed in MapKit JS 6.0.0. Use standard `EventTarget` instead.

## Declaration

```
addEventListener(
        eventType: string,
        listener: MapKitEventListener,
        thisObject?: object | null,
    ): boolean;
```

#### Discussion

Unlike a DOM `EventTarget`, a [`MapKitEventTarget`](../mapkiteventtarget.md) doesn’t go through bubbling or capturing phases. The system also interprets the third parameter differently from the DOM’s `EventTarget`.

## Parameters

- `type`: The type of event, for example, a `"configuration-change"`.
- `listener`: The callback function to invoke. MapKit JS passes `listener` an `Event` as its sole argument.
- `thisObject`: An object MapKit JS sets as the `this` keyword on the `listener` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkiteventtarget/addeventlistener)*