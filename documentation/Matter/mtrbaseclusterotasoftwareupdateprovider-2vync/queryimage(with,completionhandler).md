# queryImage(with:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- tvOS 16.1+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.4

> **Deprecated**: Please use queryImageWithParams:completion:

## Declaration

```swift
func queryImage(with params: MTROtaSoftwareUpdateProviderClusterQueryImageParams, completionHandler: @escaping @Sendable (MTROtaSoftwareUpdateProviderClusterQueryImageResponseParams?, (any Error)?) -> Void)
```

```swift
func queryImage(with params: MTROtaSoftwareUpdateProviderClusterQueryImageParams) async throws -> MTROtaSoftwareUpdateProviderClusterQueryImageResponseParams
```

```objc
- (void) queryImageWithParams:(MTROtaSoftwareUpdateProviderClusterQueryImageParams *) params completionHandler:(void (^)(MTROtaSoftwareUpdateProviderClusterQueryImageResponseParams *data, NSError *error)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterotasoftwareupdateprovider-2vync/queryimage(with:completionhandler:))*