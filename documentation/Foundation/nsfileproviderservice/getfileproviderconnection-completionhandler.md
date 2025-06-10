# getFileProviderConnection(completionHandler:)

**Framework**: Foundation  
**Kind**: method

Asynchronously returns the service’s connection object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func fileProviderConnection() async throws -> NSXPCConnection
```

## Parameters

- `completionHandler`: A block that is called on an anonymous background queue. The system passes this block the following parameters:

## See Also

- [var name: NSFileProviderServiceName](nsfileproviderservice/name.md)
  The File Provider service’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileproviderservice/getfileproviderconnection(completionhandler:))*