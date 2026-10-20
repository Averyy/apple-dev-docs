# init(section:configuration:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a compositional layout object with a single section and an additional configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(section: NSCollectionLayoutSection, configuration: UICollectionViewCompositionalLayoutConfiguration)
```

```objc
- (instancetype) initWithSection:(NSCollectionLayoutSection *) section configuration:(UICollectionViewCompositionalLayoutConfiguration *) configuration;
```

## See Also

### Creating a layout
- [init(section: NSCollectionLayoutSection)](./init%28section%29.md)
  Creates a compositional layout object with a single section.
- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider)](./init%28sectionprovider%29.md)
  Creates a compositional layout object with a section provider to supply the layout’s sections.
- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider, configuration: UICollectionViewCompositionalLayoutConfiguration)](./init%28sectionprovider,configuration%29.md)
  Creates a compositional layout object with a section provider and an additional configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayout/init(section:configuration:))*