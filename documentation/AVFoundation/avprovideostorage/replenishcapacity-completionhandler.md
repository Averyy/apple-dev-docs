# replenishCapacity(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Performs a best-effort attempt to restore Pro Video Storage to the initial capacity specified by the user in Settings app.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
func replenishCapacity() async throws -> Int
```

#### Discussion

If there is enough readily available free space on the file system, Pro Video Storage will be resized to [`initialCapacity`](avprovideostorage/initialcapacity.md). Otherwise, this method will attempt to resize it near that value.

Pro Video Storage is busy when the replenish operation starts and is no longer busy when the completion handler is called.

## Parameters

- `completionHandler`:  The completion handler is called on an arbitrary dispatch queue when the replenish operation finishes. The `remainingCapacity` parameter reflects the new size in bytes, which may be less than [`initialCapacity`](avprovideostorage/initialcapacity.md). If the operation fails, the `error` parameter is set and `remainingCapacity` is unchanged or -1 if there was a failure retrieving the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/replenishcapacity(completionhandler:))*