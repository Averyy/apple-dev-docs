# send(data:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends data to the data provider extension.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
func send(data: Data) async throws
```

## Discussion

Your app defines the data format. Send data only after the system calls [`sessionStarted(_:)`](../accessoryfeatureruntimesessionhandler/sessionstarted%28_%29.md).

## Parameters

- `data`: The data to send.

## Default Implementations

### AccessoryFeatureRuntimeSession Implementations
- [func send(data: Data) async throws](./send%28data%29-ut41.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureruntimesession/send(data:))*