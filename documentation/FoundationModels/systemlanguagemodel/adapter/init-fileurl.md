# init(fileURL:)

**Framework**: Foundation Models  
**Kind**: init

Creates an adapter from the file URL.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(fileURL: URL) throws
```

#### Discussion

> **Note**: An error of `AssetLoadingError` type when `fileURL` is invalid.

## See Also

- [init(name: String) throws](systemlanguagemodel/adapter/init(name:).md)
  Creates an adapter downloaded from the background assets framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/init(fileurl:))*