# getKnownFolderLocations(_:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Requests suitable locations for known folders.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func getKnownFolderLocations(_ knownFolders: NSFileProviderKnownFolders, completionHandler: @escaping @Sendable (NSFileProviderKnownFolderLocations?, (any Error)?) -> Void)
```

```swift
func knownFolderLocations(_ knownFolders: NSFileProviderKnownFolders) async throws -> NSFileProviderKnownFolderLocations
```

```objc
- (void) getKnownFolderLocations:(NSFileProviderKnownFolders) knownFolders completionHandler:(void (^)(NSFileProviderKnownFolderLocations *, NSError *)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderknownfoldersupporting/getknownfolderlocations(_:completionhandler:))*