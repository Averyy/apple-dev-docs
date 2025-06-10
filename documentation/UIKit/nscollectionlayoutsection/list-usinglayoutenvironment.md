# list(using:layoutEnvironment:)

**Framework**: UIKit  
**Kind**: method

Creates a list section with the specified list configuration and layout environment.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func list(using configuration: UICollectionLayoutListConfiguration, layoutEnvironment: any NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection
```

## See Also

- [convenience init(group: NSCollectionLayoutGroup)](nscollectionlayoutsection/init(group:).md)
  Creates a section containing the specified group.
- [class func orthogonalLayoutSectionForMediaItems() -> NSCollectionLayoutSection](nscollectionlayoutsection/orthogonallayoutsectionformediaitems.md)
  Creates an orthogonally scrolling section with system default spacing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/list(using:layoutenvironment:))*