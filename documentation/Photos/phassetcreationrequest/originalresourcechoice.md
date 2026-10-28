# originalResourceChoice

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The original resource to use as the unadjusted base for rendering derivatives of the new asset.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var originalResourceChoice: PHAsset.OriginalResourceChoice { get set }
```

```objc
@property (nonatomic, assign, readwrite) PHOriginalResourceChoice originalResourceChoice;
```

## Discussion

This property applies to RAW+JPEG assets only, where it selects whether the RAW or the compressed resource serves as the original. Setting it on assets that have only a single original resource is an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcreationrequest/originalresourcechoice)*