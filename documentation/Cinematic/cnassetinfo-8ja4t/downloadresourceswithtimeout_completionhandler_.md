# downloadResourcesWithTimeout:completionHandler:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Downloads the resources required to render cinematic effects for the given asset Resources are device-wide and are cached once downloaded

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```objc
- (NSProgress *) downloadResourcesWithTimeout:(NSTimeInterval) downloadTimeout completionHandler:(void (^)(CNAssetInfo *newAssetInfo, NSError *error)) completionHandler;
```

## Return Value

A \c NSProgress tracking the download.

## Parameters

- `downloadTimeout`: Maximum seconds to wait before timeout. Pass \c defaultResourceDownloadTimeout for the system default.
- `completionHandler`: Called on completion; On success, \c newAssetInfo is a refreshed instance with the downloaded resources available or self if the resources are already available; \c error is non-nil on failure


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-8ja4t/downloadresourceswithtimeout:completionhandler:)*