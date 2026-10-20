# init(sectionProvider:configuration:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a compositional layout object with a section provider and an additional configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(sectionProvider: @escaping UICollectionViewCompositionalLayoutSectionProvider, configuration: UICollectionViewCompositionalLayoutConfiguration)
```

```objc
- (instancetype) initWithSectionProvider:(UICollectionViewCompositionalLayoutSectionProvider) sectionProvider configuration:(UICollectionViewCompositionalLayoutConfiguration *) configuration;
```

## See Also

### Observing data in collection view layouts
- [typealias UICollectionViewCompositionalLayoutSectionProvider](../uicollectionviewcompositionallayoutsectionprovider.md)
  A closure that creates and returns each of the layout’s sections.
- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider)](./init%28sectionprovider%29.md)
  Creates a compositional layout object with a section provider to supply the layout’s sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayout/init(sectionprovider:configuration:))*