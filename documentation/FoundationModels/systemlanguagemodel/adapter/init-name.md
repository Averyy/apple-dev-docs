# init(name:)

**Framework**: Foundation Models  
**Kind**: init

Creates an adapter downloaded from the background assets framework.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(name: String) throws
```

#### Discussion

> **Note**: An error of `AssetLoadingError` type when there are no compatible asset packs with this adapter name downloaded.

## See Also

- [init(fileURL: URL) throws](systemlanguagemodel/adapter/init(fileurl:).md)
  Creates an adapter from the file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/init(name:))*