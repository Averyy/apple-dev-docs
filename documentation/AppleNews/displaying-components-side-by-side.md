# Displaying Components Side By Side

**Framework**: Apple News  
**Role**: Article

Configure a side-by-side, horizontal arrangement of components for your article.

## Overview

In Apple News Format, you can display child components of [`Container`](../AppleNewsFormat/container.md), [`Chapter`](../AppleNewsFormat/chapter.md), [`Section`](../AppleNewsFormat/section.md), and [`Aside`](../AppleNewsFormat/aside.md), side by side and horizontally by using the `contentDisplay` type [`HorizontalStackDisplay`](../AppleNewsFormat/horizontalstackdisplay.md). The child components are sized to match the `minimumWidth` and `maximumWidth` values defined in the [`ComponentLayout`](../AppleNewsFormat/componentlayout.md) object of these components. To redistribute the empty space inside a horizontal stack collection, use the [`FlexibleSpacer`](../AppleNewsFormat/flexiblespacer.md) object. This object provides flexible space between components in a container only when its `contentDisplay` value is set to `horizontal_stack`.

> **Note**: In versions of iOS before iOS 12, child components are vertically stacked if the container’s `contentDisplay` property is defined as the new `horizontal_stack` type.

## See Also

### Article Structure
- [Nesting Components in an Article](./nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Adding a Scene to a Chapter or a Section Header](./adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
- [Creating an Article Link](./creating-an-article-link.md)
  Link to an article by using the article-linking container component.
- [object Header](../AppleNewsFormat/header.md)
  The component for defining the top area of an article, chapter, or section.
- [object Container](../AppleNewsFormat/container.md)
  Properties shared by all container types.
- [object Section](../AppleNewsFormat/section.md)
  The component for organizing an article into sections.
- [object Chapter](../AppleNewsFormat/chapter.md)
  The component for organizing an article into chapters.
- [object Aside](../AppleNewsFormat/aside.md)
  The component for setting apart content that is not directly related to the article, such as promotional content.
- [object CollectionDisplay](../AppleNewsFormat/collectiondisplay.md)
  An object used in any container component type to define how the collection of child components is presented.
- [object HorizontalStackDisplay](../AppleNewsFormat/horizontalstackdisplay.md)
  The object for displaying components side by side in a Container component.
- [object FlexibleSpacer](../AppleNewsFormat/flexiblespacer.md)
  The component for redistributing empty space inside a horizontal stack collection.
- [object Divider](../AppleNewsFormat/divider.md)
  The component for defining a horizontal line to visually divide parts of your article.
- [object ArticleLink](../AppleNewsFormat/articlelink.md)
  The container component for creating a link to an article.
- [type SupportedArticleIdentifier](../AppleNewsFormat/supportedarticleidentifier.md)
  The patterns supported for article identifiers in UUID format.
- [type PublisherArticleIdentifier](../AppleNewsFormat/publisherarticleidentifier.md)
  The identifier provided by the publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/displaying-components-side-by-side)*