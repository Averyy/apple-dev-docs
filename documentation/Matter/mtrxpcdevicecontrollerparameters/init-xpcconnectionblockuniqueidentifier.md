# init(xpcConnectionBlock:uniqueIdentifier:)

**Framework**: Matter  
**Kind**: init

A controller created from this way will connect to a remote instance of an MTRDeviceController loaded in an XPC Service

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(xpcConnectionBlock: @escaping () -> NSXPCConnection, uniqueIdentifier: UUID)
```

## Parameters

- `xpcConnectionBlock`: The XPC Connection block that will return an NSXPCConnection to the intended listener.
- `uniqueIdentifier`: The unique id to assign to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcdevicecontrollerparameters/init(xpcconnectionblock:uniqueidentifier:))*