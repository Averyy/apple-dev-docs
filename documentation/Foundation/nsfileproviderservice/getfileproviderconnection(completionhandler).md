# getFileProviderConnection(completionHandler:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Asynchronously returns the service’s connection object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func getFileProviderConnection(completionHandler: @escaping @Sendable (NSXPCConnection?, (any Error)?) -> Void)
```

```swift
func fileProviderConnection() async throws -> NSXPCConnection
```

```objc
- (void) getFileProviderConnectionWithCompletionHandler:(void (^)(NSXPCConnection *connection, NSError *error)) completionHandler;
```

## Parameters

- `completionHandler`: A block that is called on an anonymous background queue. The system passes this block the following parameters:

  - **`connection`**: An [`NSXPCConnection`](../nsxpcconnection.md) object for the service, or `nil` if an error occurs.
  - **`error`**: If an error occurs, this property contains an object that describes the error; otherwise, it is set to `nil`.

## See Also

### Accessing the Service
- [var name: NSFileProviderServiceName](./name.md)
  The File Provider service’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileproviderservice/getfileproviderconnection(completionhandler:))*