# custom(layoutSize:itemProvider:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a group of the specified size, with an item provider that creates a custom arrangement for those items.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func custom(layoutSize: NSCollectionLayoutSize, itemProvider: @escaping NSCollectionLayoutGroupCustomItemProvider) -> Self
```

```objc
+ (instancetype) customGroupWithLayoutSize:(NSCollectionLayoutSize *) layoutSize itemProvider:(NSCollectionLayoutGroupCustomItemProvider) itemProvider;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutgroup/custom(layoutsize:itemprovider:))*