# supportedServiceSources(for:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Asks the File Provider extension for an array of custom communication channels.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func supportedServiceSources(for itemIdentifier: NSFileProviderItemIdentifier, completionHandler: @escaping ([any NSFileProviderServiceSource]?, (any Error)?) -> Void) -> Progress
```

#### Return Value

An item that tracks the progress of the

#### Discussion

The system calls this method when an app requests a list of supported services. Return an array of services for the specified file. An application with access to the file can request the supported services by calling the [`FileManager`](https://developer.apple.com/documentation/Foundation/FileManager) class’s [`getFileProviderServicesForItem(at:completionHandler:)`](https://developer.apple.com/documentation/foundation/filemanager/2915262-getfileproviderservicesforitem) method. For more information, see [`NSFileProviderService`](https://developer.apple.com/documentation/Foundation/NSFileProviderService).

## Parameters

- `itemIdentifier`: The item’s identifier.
- `completionHandler`: A block that you call after gathering the service sources. You pass the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderservicing/supportedservicesources(for:completionhandler:))*