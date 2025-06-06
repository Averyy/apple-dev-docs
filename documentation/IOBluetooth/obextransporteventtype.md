# OBEXTransportEventType

**Framework**: IOBluetooth  
**Kind**: typealias

**Availability**:
- macOS ?+

## Declaration

```swift
typealias OBEXTransportEventType = UInt32
```

#### Discussion

Pass these types in the OBEXTransportEvent, and then pass the struct on to the session object once you have filled it out. This is how you can communicate with the session when events happen - if data is received, the type will be ‘kOBEXTransportEventTypeDataReceived’. if an error has occurred on your transport, like the remote target died, you can send a status event with a non-zero value. Since session objects will receive this status code on their event handlers, you should try to pass a useful status/error code, such as an IOReturn value.

## See Also

- [struct OBEXTransportEvent](obextransportevent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/obextransporteventtype)*