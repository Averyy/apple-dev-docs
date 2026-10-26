# originalResourceChoice

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The original resource used as the basis for rendering this asset’s derivatives.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var originalResourceChoice: PHAsset.OriginalResourceChoice { get }
```

```objc
@property (nonatomic, assign, readonly) PHOriginalResourceChoice originalResourceChoice;
```

#### Discussion

This value is only meaningful for assets that have a RAW alternate, such as RAW+JPEG assets, where it indicates whether the RAW or the compressed resource serves as the unadjusted base. For all other assets the value is [`PHAsset.OriginalResourceChoice.compressed`](./originalresourcechoice-swift.enum/compressed.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phasset/originalresourcechoice-swift.property)*