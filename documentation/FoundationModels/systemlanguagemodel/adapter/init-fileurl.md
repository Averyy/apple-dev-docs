# init(fileURL:)

**Framework**: Foundation Models  
**Kind**: init

Creates an adapter from the file URL.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(fileURL: URL) throws
```

#### Discussion

> **Note**: An error of `AssetLoadingError` type when `fileURL` is invalid.

## See Also

- [Loading and using a custom adapter with Foundation Models](loading-and-using-a-custom-adapter-with-foundation-models.md)
  Specialize the behavior of the system language model by using a custom adapter you train.
- [com.apple.developer.foundation-model-adapter](../BundleResources/Entitlements/com.apple.developer.foundation-model-adapter.md)
  A Boolean value that indicates whether the app can enable custom adapters for the Foundation Models framework.
- [init(name: String) throws](systemlanguagemodel/adapter/init(name:).md)
  Creates an adapter downloaded from the background assets framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter/init(fileurl:))*