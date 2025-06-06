# init(url:)

**Framework**: Core ML  
**Kind**: init

Constructs a ModelAsset from a compiled model URL.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
convenience init(url compiledModelURL: URL) throws
```

#### Return Value

A model asset or nil if there is an error.

## Parameters

- `compiledModelURL`: Location on the disk where the model asset is present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelasset/init(url:))*