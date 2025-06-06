# synchronize()

**Framework**: Foundation  
**Kind**: method

Explicitly synchronizes in-memory keys and values with those stored on disk.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func synchronize() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the in-memory and on-disk keys and values were synchronized, or [`false`](https://developer.apple.com/documentation/swift/false) if an error occurred. For example, this method returns [`false`](https://developer.apple.com/documentation/swift/false) if an app was not built with the proper entitlement requests.

#### Discussion

The only recommended time to call this method is upon app launch, or upon returning to the foreground, to ensure that the in-memory key-value store representation is up-to-date.

Changes you make to the key-value store are saved to memory. The system then synchronizes the in-memory keys and values with the local on-disk cache, automatically and at appropriate times. For example, it synchronizes the keys when your app is put into the background, when changes are received from iCloud, and when your app makes changes to a key but does not call the [`synchronize()`](nsubiquitouskeyvaluestore/synchronize().md) method for several seconds.

This method does not force new keys and values to be written to iCloud. Rather, it lets iCloud know that new keys and values are available to be uploaded. Do not rely on your keys and values being available on other devices immediately. The system controls when those keys and values are uploaded. The frequency of upload requests for key-value storage is limited to several per minute.

During synchronization between memory and disk, this method updates your in-memory set of keys and values with changes previously received from iCloud.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/synchronize())*