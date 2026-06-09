# receiveData(_:fromApplication:session:)

**Framework**: Media Device  
**Kind**: method

Delivers data received from a remote application to the system for processing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func receiveData(_ data: Data, fromApplication applicationIdentifier: String, session: MediaOutputSession)
```

#### Discussion

Call this function when data has been received from a remote application.

## Parameters

- `data`: The data received from the remote application.
- `applicationIdentifier`: The identifier of the application that sent the data.
- `session`: The session associated with the received data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/receivedata(_:fromapplication:session:))*