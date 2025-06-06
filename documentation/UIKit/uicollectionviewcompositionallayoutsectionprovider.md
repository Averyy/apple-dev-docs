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

A section provider is also invoked in response to system events such as changes in device orientation, system font size, and size classes from iPad multitasking. You can use this opportunity to adapt the layout to different layout environments by inspecting information about the current layout environment ([`NSCollectionLayoutEnvironment`](nscollectionlayoutenvironment.md)) and using that information to configure each section.

For example, the following code shows a section provider that creates a two-column layout when the width of the section’s container is less than 800 points, and a four-column layout otherwise.

In iOS 18 and later, UIKit supports automatic trait tracking inside this closure for traits from the `traitCollection` of the `layoutEnvironment` parameter. For more information, see [`Automatic trait tracking`](automatic-trait-tracking.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcompositionallayoutsectionprovider)*