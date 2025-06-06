# init(xpConnectionBlock:uniqueIdentifier:)

**Framework**: Matter  
**Kind**: init

A controller created from this way will connect to a remote instance of an MTRDeviceController loaded in an XPC Service

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
init(xpConnectionBlock xpcConnectionBlock: @escaping () -> NSXPCConnection, uniqueIdentifier: UUID)
```

## Parameters

- `xpcConnectionBlock`: The XPC Connection block that will return an NSXPCConnection to the intended listener.
- `uniqueIdentifier`: The unique id to assign to the controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcdevicecontrollerparameters/init(xpconnectionblock:uniqueidentifier:))*