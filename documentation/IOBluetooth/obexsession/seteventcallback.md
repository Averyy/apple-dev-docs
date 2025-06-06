# setEventCallback(_:)

**Framework**: IOBluetooth  
**Kind**: method

Sets the C-API callback used when the session recieves data.

**Availability**:
- macOS ?+

## Declaration

```swift
func setEventCallback(_ inEventCallback: OBEXSessionEventCallback!)
```

#### Discussion

This is really not intended for client sessions. Only subclasses would really be interested in using this. They should set these when their subclass object is created, because otherwise they will have no way of receiving the initial command data packet. This is a partner to setEventRefCon, described below.

## Parameters

- `inEventCallback`: Function to callback. Should be non-NULL, unless you are attempting to clear the callback, but doing that doesn’t make much sense.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/seteventcallback(_:))*