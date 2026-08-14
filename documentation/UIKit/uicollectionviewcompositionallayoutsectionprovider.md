# UICollectionViewCompositionalLayoutSectionProvider

**Framework**: UIKit  
**Kind**: typealias

A closure that creates and returns each of the layout’s sections.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias UICollectionViewCompositionalLayoutSectionProvider = (Int, any NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection?
```

#### Discussion

You use a section provider to create a compositional layout ([`UICollectionViewCompositionalLayout`](uicollectionviewcompositionallayout.md)) that has multiple sections with different layouts. The section provider keeps track of the index of the section that it’s currently creating, so you can configure each section differently.

For example, the following code shows a section provider that creates a two-column layout in the first section, and a four-column layout in each section after the first section.

**Swift**:

```swift
func createPerSectionLayout() -> UICollectionViewLayout {
    let layout = UICollectionViewCompositionalLayout { (sectionIndex: Int,
        layoutEnvironment: NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection? in
        
        let columns = sectionIndex == 0 ? 2 : 4
        
        let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                             heightDimension: .fractionalHeight(1.0))
        let item = NSCollectionLayoutItem(layoutSize: itemSize)
        
        let groupSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                              heightDimension: .absolute(44))
        let group = NSCollectionLayoutGroup.horizontal(layoutSize: groupSize,
                                                          subitem: item,
                                                            count: columns)
        
        let section = NSCollectionLayoutSection(group: group)
        return section
    }
    return layout
}
```

**Objective-C**:

```objc
UICollectionViewCompositionalLayout *layout = [[UICollectionViewCompositionalLayout alloc] initWithSectionProvider:^NSCollectionLayoutSection *(NSInteger sectionIndex, id<NSCollectionLayoutEnvironment> layoutEnvironment) {
    
    NSInteger columns = (sectionIndex == 0) ? 2 : 4;
    
    NSCollectionLayoutSize *itemSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension fractionalWidthDimension:1.0] heightDimension:[NSCollectionLayoutDimension fractionalHeightDimension:1.0]];
    
    NSCollectionLayoutItem *item = [NSCollectionLayoutItem itemWithLayoutSize:itemSize];

    NSCollectionLayoutSize *groupSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension fractionalWidthDimension:1.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:44.0]];

    NSCollectionLayoutGroup *group = [NSCollectionLayoutGroup horizontalGroupWithLayoutSize:groupSize subitem:item count:columns];
            
    NSCollectionLayoutSection *section = [NSCollectionLayoutSection sectionWithGroup:group];
    return section;
}];

return layout;
```

A section provider is also invoked in response to system events such as changes in device orientation, system font size, and size classes from iPad multitasking. You can use this opportunity to adapt the layout to different layout environments by inspecting information about the current layout environment ([`NSCollectionLayoutEnvironment`](nscollectionlayoutenvironment.md)) and using that information to configure each section.

For example, the following code shows a section provider that creates a two-column layout when the width of the section’s container is less than 800 points, and a four-column layout otherwise.

**Swift**:

```swift
func createAdaptiveLayout() -> UICollectionViewLayout {
    let layout = UICollectionViewCompositionalLayout { (sectionIndex: Int,
        layoutEnvironment: NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection in

        let columns = layoutEnvironment.container.effectiveContentSize.width < 800 ? 2 : 4
        
        let itemSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                             heightDimension: .fractionalHeight(1.0))
        let item = NSCollectionLayoutItem(layoutSize: itemSize)
        
        let groupSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(1.0),
                                              heightDimension: .absolute(44))
        let group = NSCollectionLayoutGroup.horizontal(layoutSize: groupSize,
                                                          subitem: item,
                                                            count: columns)
        
        let section = NSCollectionLayoutSection(group: group)
        return section
    }
    return layout
}
```

**Objective-C**:

```objc
UICollectionViewCompositionalLayout *layout = [[UICollectionViewCompositionalLayout alloc] initWithSectionProvider:^NSCollectionLayoutSection *(NSInteger sectionIndex, id<NSCollectionLayoutEnvironment> layoutEnvironment) {    
    NSInteger columns = (layoutEnvironment.container.effectiveContentSize.width < 800) ? 2 : 4;
    
    NSCollectionLayoutSize *itemSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension fractionalWidthDimension:1.0] heightDimension:[NSCollectionLayoutDimension fractionalHeightDimension:1.0]];
    
    NSCollectionLayoutItem *item = [NSCollectionLayoutItem itemWithLayoutSize:itemSize];

    NSCollectionLayoutSize *groupSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension fractionalWidthDimension:1.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:44.0]];

    NSCollectionLayoutGroup *group = [NSCollectionLayoutGroup horizontalGroupWithLayoutSize:groupSize subitem:item count:columns];
            
    NSCollectionLayoutSection *section = [NSCollectionLayoutSection sectionWithGroup:group];
    return section;
}];

return layout;
```

UIKit supports automatic trait tracking inside this closure for traits from the `traitCollection` of the `layoutEnvironment` parameter. For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).

In iOS 27 and later, UIKit supports automatic observation tracking inside this closure when reading properties on objects that use the [`Observable`](https://developer.apple.com/documentation/observation/observable) macro. For more information, see [`Automatic observation tracking`](automatic-observation-tracking.md).

## See Also

- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider)](uicollectionviewcompositionallayout/init(sectionprovider:).md)
  Creates a compositional layout object with a section provider to supply the layout’s sections.
- [init(sectionProvider: UICollectionViewCompositionalLayoutSectionProvider, configuration: UICollectionViewCompositionalLayoutConfiguration)](uicollectionviewcompositionallayout/init(sectionprovider:configuration:).md)
  Creates a compositional layout object with a section provider and an additional configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayoutsectionprovider)*