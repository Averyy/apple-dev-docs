# synchronize()

**Framework**: Foundation  
**Kind**: method

Synchronizes the in-memory keys and values with the ones stored in iCloud.

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

`true` if the in-memory and iCloud keys are synchronized, or `false` if an error occurred. For example, this method returns `false` if the app doesn’t have the required entitlements to access the iCloud key-value store.

#### Discussion

Call this method sparingly to synchronize the in-memory copy of the keys and values with the version stored in iCloud. Typically, you call this method only at launch or when your app returns to the foreground.

Most of the time, you don’t need to call this method directly. The system automatically synchronizes your app’s in-memory copy of the keys and values with the on-disk version at appropriate times. For example, it synchronizes them when your app moves to the background and when iCloud reports a change to a key or value. When you change keys and values locally, the system also synchronizes your changes automatically after a short delay.

Don’t rely on keys and values being available on the person’s other devices immediately. This method doesn’t force the system to write new keys and values to iCloud. Instead, it notifies iCloud that new keys and values are available. iCloud determines the best time to retrieve those keys and synchronize them with the person’s other devices. Typically, iCloud limits updates to several times per minute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/synchronize())*