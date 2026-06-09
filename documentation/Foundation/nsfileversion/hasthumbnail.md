# hasThumbnail

**Framework**: Foundation  
**Kind**: property

Whether the version has a thumbnail image available. Thumbnails for versions from +getNonlocalVersionsOfItemAtURL:completionHandler: may not immediately be available. As soon as it becomes available, this property will change from NO to YES. You can use KVO to be notified of this change. If a thumbnail is available, you can access it using NSURLThumbnailKey or NSURLThumbnailDictionaryKey.

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
var hasThumbnail: Bool { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfileversion/hasthumbnail)*