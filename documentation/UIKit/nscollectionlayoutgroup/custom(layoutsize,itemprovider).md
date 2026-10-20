# custom(layoutSize:itemProvider:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a group of the specified size, with an item provider that creates a custom arrangement for those items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func custom(layoutSize: NSCollectionLayoutSize, itemProvider: @escaping NSCollectionLayoutGroupCustomItemProvider) -> Self
```

```objc
+ (instancetype) customGroupWithLayoutSize:(NSCollectionLayoutSize *) layoutSize itemProvider:(NSCollectionLayoutGroupCustomItemProvider) itemProvider;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutgroup/custom(layoutsize:itemprovider:))*