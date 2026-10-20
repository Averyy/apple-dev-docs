# previewParametersProvider

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that provides the preview parameters for a drag item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var previewParametersProvider: ((UICollectionViewCell) -> UIDragPreviewParameters?)? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIDragPreviewParameters * (^previewParametersProvider)(UICollectionViewCell *);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropplaceholder/previewparametersprovider)*