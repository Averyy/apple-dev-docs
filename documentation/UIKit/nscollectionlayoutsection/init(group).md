# init(group:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a section containing the specified group.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(group: NSCollectionLayoutGroup)
```

```objc
+ (instancetype) sectionWithGroup:(NSCollectionLayoutGroup *) group;
```

## See Also

### Creating a section
- [static func list(using: UICollectionLayoutListConfiguration, layoutEnvironment: any NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection](./list%28using,layoutenvironment%29.md)
  Creates a list section with the specified list configuration and layout environment.
- [class func orthogonalLayoutSectionForMediaItems() -> NSCollectionLayoutSection](./orthogonallayoutsectionformediaitems%28%29.md)
  Creates an orthogonally scrolling section with system default spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/init(group:))*