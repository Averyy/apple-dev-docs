# init(sectionProvider:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a compositional layout object with a section provider to supply the layout’s sections.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(sectionProvider: @escaping NSCollectionViewCompositionalLayoutSectionProvider)
```

```objc
- (instancetype) initWithSectionProvider:(NSCollectionViewCompositionalLayoutSectionProvider) sectionProvider;
```

## See Also

### Creating a Layout
- [init(section: NSCollectionLayoutSection)](./init%28section%29.md)
  Creates a compositional layout object with a single section.
- [init(section: NSCollectionLayoutSection, configuration: NSCollectionViewCompositionalLayoutConfiguration)](./init%28section,configuration%29.md)
  Creates a compositional layout object with a single section and an additional configuration.
- [init(sectionProvider: NSCollectionViewCompositionalLayoutSectionProvider, configuration: NSCollectionViewCompositionalLayoutConfiguration)](./init%28sectionprovider,configuration%29.md)
  Creates a compositional layout object with a section provider and an additional configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewcompositionallayout/init(sectionprovider:))*