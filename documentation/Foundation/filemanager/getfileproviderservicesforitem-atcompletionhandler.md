# getFileProviderServicesForItem(at:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Returns the services provided by the File Provider extension that manages the item at the given URL.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func fileProviderServicesForItem(at url: URL) async throws -> [NSFileProviderServiceName : NSFileProviderService]
```

#### Discussion

Use the returned services to perform custom actions defined by the services’ protocol.

To access the service:

1. Use the desired service’s name to get the [`NSFileProviderService`](nsfileproviderservice.md) object for the service. This object can only be used to operate on the item specified by the `url` parameter.
2. Get the [`NSXPCConnection`](nsxpcconnection.md) object from the service.
3. Set the connection’s [`remoteObjectInterface`](nsxpcconnection/remoteobjectinterface.md) property, using the service’s protocol.
4. (Optional) Provide any additional configuration for the connection.
5. Call [`resume()`](nsxpcconnection/resume().md) on the connection.
6. Get the proxy from the connection’s [`remoteObjectProxy`](nsxpcconnection/remoteobjectproxy.md) property.
7. Call the custom action methods on the proxy object.

The listing below shows a sample implementation for accessing a File Provider service’s remote proxy object.

```swift
// Get the list of services available for an item at the given URL.
FileManager.default.getFileProviderServicesForItem(at: url) { (services, error) in
    
    // Check to see if an error occurred.
    guard error == nil else {
        // Handle the error here...
        return
    }
    
    if let desiredService = services?[desiredServiceName] {
        
        // The named service is available for the item at the provided URL.
        // To use the service, get the connection object.
        desiredService.getFileProviderConnection(completionHandler: { (connectionOrNil, connectionError) in
            
            guard connectionError == nil else {
                // Handle the error here...
                return
            }
            
            guard let connection = connectionOrNil else {
                // No connection object found.
                return
            }
            
            // Set the remote interface.
            connection.remoteObjectInterface = NSXPCInterface(with: DesiredProtocol.self)
            
            // Start the connection.
            connection.resume()
            
            // Get the proxy object.
            let rawProxy = connection.remoteObjectProxyWithErrorHandler({ (errorAccessingRemoteObject) in
                // Handle the error here...
            })
            
            // Cast the proxy object to the interface's protocol.
            guard let proxy = rawProxy as? DesiredProtocol else {
                // If the interface is set up properly, this should never fail.
                fatalError("*** Unable to cast \(rawProxy) to a DesiredProtocol instance ***")
            }
            
            // You can now use the proxy to call the service's custom actions.
            
        })
    }
}
```

For more information, see [`Defining the Service’s Protocol`](nsfileproviderservice#Defining-the-Services-Protocol.md).

## Parameters

- `url`: The file URL of a document or directory.
- `completionHandler`: A block that is called on an anonymous background queue. The system passes this block the following parameters:

## See Also

- [class NSFileProviderService](nsfileproviderservice.md)
  A service that provides a custom communication channel between your app and a File Provider extension.
- [struct NSFileProviderServiceName](nsfileproviderservicename.md)
  The name used to identify a File Provider service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filemanager/getfileproviderservicesforitem(at:completionhandler:))*