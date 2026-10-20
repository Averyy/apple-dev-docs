# init(sectionProvider:configuration:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a compositional layout object with a section provider and an additional configuration.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(sectionProvider: @escaping NSCollectionViewCompositionalLayoutSectionProvider, configuration: NSCollectionViewCompositionalLayoutConfiguration)
```

```objc
- (instancetype) initWithSectionProvider:(NSCollectionViewCompositionalLayoutSectionProvider) sectionProvider configuration:(NSCollectionViewCompositionalLayoutConfiguration *) configuration;
```

## See Also

### Creating a Layout
- [init(section: NSCollectionLayoutSection)](./init%28section%29.md)
  Creates a compositional layout object with a single section.
- [init(section: NSCollectionLayoutSection, configuration: NSCollectionViewCompositionalLayoutConfiguration)](./init%28section,configuration%29.md)
  Creates a compositional layout object with a single section and an additional configuration.
- [init(sectionProvider: NSCollectionViewCompositionalLayoutSectionProvider)](./init%28sectionprovider%29.md)
  Creates a compositional layout object with a section provider to supply the layout’s sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewcompositionallayout/init(sectionprovider:configuration:))*