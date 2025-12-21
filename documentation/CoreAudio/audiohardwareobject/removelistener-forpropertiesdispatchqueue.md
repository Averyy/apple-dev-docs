# removeListener(forProperties:dispatchQueue:)

**Framework**: Core Audio  
**Kind**: method

Unregisters for receiving notifications when the given properties change.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func removeListener(forProperties properties: [AudioObjectPropertyAddress], dispatchQueue: dispatch_queue_t? = nil) throws
```

## Parameters

- `properties`: An array of AudioObjectPropertyAddress indicating from which   properties the listener should be removed.
- `dispatchQueue`: The dispatch queue on which the delegate was  dispatched to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject/removelistener(forproperties:dispatchqueue:))*