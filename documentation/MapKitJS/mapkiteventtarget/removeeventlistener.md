# removeEventListener(eventType, listener, thisObject)

**Framework**: MapKit JS  
**Kind**: method  
**Role**: Instance Method

Unsubscribes a listener function from an event type.

**Availability**:
- MapKit JS 5.0+ - Deprecated in 6.0

> **Deprecated**: Removed in MapKit JS 6.0.0. Use standard `EventTarget` instead.

## Declaration

```
removeEventListener(
        eventType?: string,
        listener?: MapKitEventListener,
        thisObject?: object | null,
    ): boolean;
```

## Discussion

Unlike a DOM `EventTarget`, a [`MapKitEventTarget`](../mapkiteventtarget.md) doesn’t go through bubbling or capturing phases. The system also interprets the second and the third parameters differently from the DOM’s `EventTarget`.

## Parameters

- `type`: The type of event, for example, a `"configuration-change"`.
- `listener`: The callback function to remove. Not setting this parameter removes all listeners of the specified type.
- `thisObject`: An object MapKit JS sets as the `this` keyword on the `listener` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkiteventtarget/removeeventlistener)*