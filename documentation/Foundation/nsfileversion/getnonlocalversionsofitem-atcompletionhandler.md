# getNonlocalVersionsOfItem(at:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Asynchronously returns an array of NSFileVersions associated with the file located by the given URL, or nil if there is no such file or another error occurs.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func nonlocalVersionsOfItem(at url: URL) async throws -> [NSFileVersion]
```

#### Discussion

Versions returned by this method do not initially have their contents stored locally on the device, so a download may be required before you are able to access them. File attributes are accessible via -[NSURL getPromisedItemResourceValue:forKey:error:]. You can request a download by performing a coordinated read with NSFileCoordinator on the URL property of the resulting NSFileVersions.

When a version is successfully downloaded, its contents are cached locally, and the version will no longer be returned by this method. The version will be returned by +otherVersionsOfItemAtURL: instead, but will retain the same persistentIdentifier value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/getnonlocalversionsofitem(at:completionhandler:))*