# setEventRefCon(_:)

**Framework**: IOBluetooth  
**Kind**: method

Sets the C-API callback refCon used when the session recieves data.

**Availability**:
- macOS ?+

## Declaration

```swift
func setEventRefCon(_ inRefCon: UnsafeMutableRawPointer!)
```

#### Discussion

This is really not intended for client sessions. Only subclasses would really be interested in using this. They should set these when their subclass object is created, because otherwise they will have no context in their callback.

## Parameters

- `inRefCon`: User’s refCon that will get passed when their event callback is invoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obexsession/seteventrefcon(_:))*