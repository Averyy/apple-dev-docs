# downloadResourcesForVersions:timeout:completionHandler:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Type Method

Downloads the resources required to render cinematic effects on assets Resources are device-wide and are cached once downloaded

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```objc
+ (NSProgress *) downloadResourcesForVersions:(NSSet<NSNumber *> *) resourceVersions timeout:(NSTimeInterval) downloadTimeout completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Return Value

A \c NSProgress tracking the download.

## Parameters

- `resourceVersions`: Resource version(s) to download. Pass an empty set to download all available resources
- `downloadTimeout`: Maximum seconds to wait before timeout. Pass \c defaultResourceDownloadTimeout for the system default.
- `completionHandler`: Called on completion; \c error is \c nil on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-8ja4t/downloadresourcesforversions:timeout:completionhandler:)*