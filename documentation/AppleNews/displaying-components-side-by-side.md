# Displaying Components Side By Side

**Framework**: Applenews

Configure a side-by-side, horizontal arrangement of components for your article.

#### Overview

In Apple News Format, you can display child components of [`Container`](https://developer.apple.com/documentation/applenewsformat/container), [`Chapter`](https://developer.apple.com/documentation/applenewsformat/chapter), [`Section`](https://developer.apple.com/documentation/applenewsformat/section), and [`Aside`](https://developer.apple.com/documentation/applenewsformat/aside), side by side and horizontally by using the `contentDisplay` type [`HorizontalStackDisplay`](https://developer.apple.com/documentation/applenewsformat/horizontalstackdisplay). The child components are sized to match the `minimumWidth` and `maximumWidth` values defined in the [`ComponentLayout`](https://developer.apple.com/documentation/applenewsformat/componentlayout) object of these components. To redistribute the empty space inside a horizontal stack collection, use the [`FlexibleSpacer`](https://developer.apple.com/documentation/applenewsformat/flexiblespacer) object. This object provides flexible space between components in a container only when its `contentDisplay` value is set to `horizontal_stack`.

> **Note**: In versions of iOS before iOS 12, child components are vertically stacked if the container’s `contentDisplay` property is defined as the new `horizontal_stack` type.

## See Also

- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Adding a Scene to a Chapter or a Section Header](adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
- [Creating an Article Link](creating-an-article-link.md)
  Link to an article by using the article-linking container component.
- [object Header](../applenewsformat/header.md)
  The component for defining the top area of an article, chapter, or section.
- [object Container](../applenewsformat/container.md)
  Properties shared by all container types.
- [object Section](../applenewsformat/section.md)
  The component for organizing an article into sections.
- [object Chapter](../applenewsformat/chapter.md)
  The component for organizing an article into chapters.
- [object Aside](../applenewsformat/aside.md)
  The component for setting apart content that is not directly related to the article, such as promotional content.
- [object CollectionDisplay](../applenewsformat/collectiondisplay.md)
  An object used in any container component type to define how the collection of child components is presented.
- [object HorizontalStackDisplay](../applenewsformat/horizontalstackdisplay.md)
  The object for displaying components side by side in a Container component.
- [object FlexibleSpacer](../applenewsformat/flexiblespacer.md)
  The component for redistributing empty space inside a horizontal stack collection.
- [object Divider](../applenewsformat/divider.md)
  The component for defining a horizontal line to visually divide parts of your article.
- [object ArticleLink](../applenewsformat/articlelink.md)
  The container component for creating a link to an article.
- [type SupportedArticleIdentifier](../applenewsformat/supportedarticleidentifier.md)
  The patterns supported for article identifiers in UUID format.
- [type PublisherArticleIdentifier](../applenewsformat/publisherarticleidentifier.md)
  The identifier provided by the publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleNews/displaying-components-side-by-side)*