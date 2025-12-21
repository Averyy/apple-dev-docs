# addListener(forProperties:dispatchQueue:)

**Framework**: Core Audio  
**Kind**: method

Registers for notifications to be received on the property listener delegates when the given properties change.

**Availability**:
- Mac Catalyst ?+
- macOS 15.0+

## Declaration

```swift
func addListener(forProperties properties: [AudioObjectPropertyAddress], dispatchQueue: dispatch_queue_t? = nil) throws
```

#### Discussion

The AudioHardwareObject’s delegates property must contain at least one delegate for listeners to be called.

## Parameters

- `properties`: An array of AudioObjectPropertyAddresses indicating which   properties the listener should notify about.
- `dispatchQueue`: The dispatch queue on which the delegates will be called.   All delegate calls will be dispatched asynchronously save for those dispatched from the   IO context (of which kAudioDevicePropertyDeviceIsRunning and   kAudioDeviceProcessorOverload are the only examples) which will be dispatched   synchronously. Note that this dispatch queue will be retained until a matching call to   removePropertyListener is made. If this value is nil, then the delegates will be directly   called.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudio/audiohardwareobject/addlistener(forproperties:dispatchqueue:))*