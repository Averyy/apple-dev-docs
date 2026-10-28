# supportedServiceSources(for:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the File Provider extension for an array of custom communication channels.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func supportedServiceSources(for itemIdentifier: NSFileProviderItemIdentifier, completionHandler: @escaping ([any NSFileProviderServiceSource]?, (any Error)?) -> Void) -> Progress
```

```objc
- (NSProgress *) supportedServiceSourcesForItemIdentifier:(NSFileProviderItemIdentifier) itemIdentifier completionHandler:(void (^)(NSArray<id<NSFileProviderServiceSource>> *, NSError *)) completionHandler;
```

## Return Value

An item that tracks the progress of the

## Discussion

The system calls this method when an app requests a list of supported services. Return an array of services for the specified file. An application with access to the file can request the supported services by calling the [`FileManager`](../../Foundation/filemanager.md) class’s [`getFileProviderServicesForItem(at:completionHandler:)`](../../Foundation/filemanager/getfileproviderservicesforitem%28at,completionhandler%29.md) method. For more information, see [`NSFileProviderService`](../../Foundation/nsfileproviderservice.md).

## Parameters

- `itemIdentifier`: The item’s identifier.
- `completionHandler`: A block that you call after gathering the service sources. You pass the following parameters:

  - **serviceSources**: An array of service sources that lets you communicate with the host app.
  - **error**: If an error occurs, this object contains information about the error; otherwise, it’s `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderservicing/supportedservicesources(for:completionhandler:))*