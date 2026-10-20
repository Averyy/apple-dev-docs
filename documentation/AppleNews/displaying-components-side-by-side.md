# Displaying Components Side By Side

**Framework**: Apple News  
**Role**: Article

Configure a side-by-side, horizontal arrangement of components for your article.

#### Overview

In Apple News Format, you can display child components of [`Container`](https://developer.apple.com/documentation/applenewsformat/container), [`Chapter`](https://developer.apple.com/documentation/applenewsformat/chapter), [`Section`](https://developer.apple.com/documentation/applenewsformat/section), and [`Aside`](https://developer.apple.com/documentation/applenewsformat/aside), side by side and horizontally by using the `contentDisplay` type [`HorizontalStackDisplay`](https://developer.apple.com/documentation/applenewsformat/horizontalstackdisplay). The child components are sized to match the `minimumWidth` and `maximumWidth` values defined in the [`ComponentLayout`](https://developer.apple.com/documentation/applenewsformat/componentlayout) object of these components. To redistribute the empty space inside a horizontal stack collection, use the [`FlexibleSpacer`](https://developer.apple.com/documentation/applenewsformat/flexiblespacer) object. This object provides flexible space between components in a container only when its `contentDisplay` value is set to `horizontal_stack`.

> **Note**: In versions of iOS before iOS 12, child components are vertically stacked if the container’s `contentDisplay` property is defined as the new `horizontal_stack` type.

## See Also

### Article Structure
- [Nesting Components in an Article](./nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Adding a Scene to a Chapter or a Section Header](./adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
- [Creating an Article Link](./creating-an-article-link.md)
  Link to an article by using the article-linking container component.
- [object Header](https://developer.apple.com/documentation/applenewsformat/header)
  The component for defining the top area of an article, chapter, or section.
- [object Container](https://developer.apple.com/documentation/applenewsformat/container)
  Properties shared by all container types.
- [object Section](https://developer.apple.com/documentation/applenewsformat/section)
  The component for organizing an article into sections.
- [object Chapter](https://developer.apple.com/documentation/applenewsformat/chapter)
  The component for organizing an article into chapters.
- [object Aside](https://developer.apple.com/documentation/applenewsformat/aside)
  The component for setting apart content that is not directly related to the article, such as promotional content.
- [object CollectionDisplay](https://developer.apple.com/documentation/applenewsformat/collectiondisplay)
  An object used in any container component type to define how the collection of child components is presented.
- [object HorizontalStackDisplay](https://developer.apple.com/documentation/applenewsformat/horizontalstackdisplay)
  The object for displaying components side by side in a Container component.
- [object FlexibleSpacer](https://developer.apple.com/documentation/applenewsformat/flexiblespacer)
  The component for redistributing empty space inside a horizontal stack collection.
- [object Divider](https://developer.apple.com/documentation/applenewsformat/divider)
  The component for defining a horizontal line to visually divide parts of your article.
- [object ArticleLink](https://developer.apple.com/documentation/applenewsformat/articlelink)
  The container component for creating a link to an article.
- [type SupportedArticleIdentifier](https://developer.apple.com/documentation/applenewsformat/supportedarticleidentifier)
  The patterns supported for article identifiers in UUID format.
- [type PublisherArticleIdentifier](https://developer.apple.com/documentation/applenewsformat/publisherarticleidentifier)
  The identifier provided by the publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/displaying-components-side-by-side)*