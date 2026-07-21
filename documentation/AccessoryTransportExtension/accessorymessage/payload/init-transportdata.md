# init(transport:data:)

**Framework**: Accessory Transport Extension  
**Kind**: init

Initializes a payload with data and a transport preference.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
init(transport: AccessoryTransport = .bluetooth, data: Data)
```

#### Discussion

If the specified transport method isn’t available, the system chooses any available transport method.

## Parameters

- `transport`: The preferred transport method for the payload. The default is Bluetooth.
- `data`: The payload content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/payload/init(transport:data:))*