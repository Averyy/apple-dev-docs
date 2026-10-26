# Nesting Components in an Article

**Framework**: Apple News  
**Role**: Article

Use container components to create the component hierarchies you need for special article designs.

#### Overview

A *nested* component is a child of the parent component that contains it. The child component is positioned and rendered relative to that parent. The size of the child components determines the minimum size of a container component.

> 💡 **Tip**:  If you use an anchor to attach multiple children to the same side of their parent component, the children “stack” to create a cleanly aligned header. For information about using container components and anchors, see [Advanced Design Tutorial 2: Layout and Positioning](./apple-news-format-tutorials.md#Advanced-Design-Tutorial-2-Layout-and-Positioning).

Many design and layout effects require you to use hierarchies of nested components. For example, you can create a layering effect by nesting content (such as a `title`) inside a parent component that has a background [`Fill`](../AppleNewsFormat/fill.md). Any content displayed by the parent — as well as any content from its child components — is layered in front of the parent’s background fill, as shown in this example.

![Screenshot of an article with a header component that nests an image and a caption.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-4085703@2x.png)

Apple News Format has several container components that allow you to nest other components within them:

- [`Chapter`](../AppleNewsFormat/chapter.md)
- [`Header`](../AppleNewsFormat/header.md)
- [`Section`](../AppleNewsFormat/section.md)
- [`Container`](../AppleNewsFormat/container.md)

The [`Aside`](../AppleNewsFormat/aside.md) component also lets you nest other components, but generally contains content that isn’t directly related to your article.

The following example shows a section component with two child components (`title` and `photo`) defined in its components array.

```json
{
  "role": "section",
  "components": [
  {
     "role": "title",
     "text": "A Photo",
   },
  {
     "role": "photo",
     "URL": "bundle://.",
     }
    ]
}
```

All container components have a components property whose value is an array of components. In this array, the order of the components is the order in which they appear in your article.

## See Also

### Related Documentation
- [About Containers](./about-containers.md)
  Learn the basic Apple News Format container concepts required for the three advanced tutorials.
- [Creating a Layered Header](./creating-a-layered-header.md)
  Create a header with a caption that’s layered in front of an image.
- [Creating a Complex, Layered Header](./creating-a-complex-layered-header.md)
  Layer a title and heading in front of an image, with their colors optimized for legibility.
- [Creating a Floating Caption](./creating-a-floating-caption.md)
  Position a caption in the wide right margin of your article.
- [Creating an Inset Pull Quote](./creating-an-inset-pull-quote.md)
  Wrap article body text around an inset pull quote.
- [Creating an Inset Photo](./creating-an-inset-photo.md)
  Wrap article body text around an inset photo.
- [Creating a Sidebar](./creating-a-sidebar.md)
  Create a box with an HTML bulleted list in the margin.
### Article Structure
- [Adding a Scene to a Chapter or a Section Header](./adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
- [Creating an Article Link](./creating-an-article-link.md)
  Link to an article by using the article-linking container component.
- [Displaying Components Side By Side](./displaying-components-side-by-side.md)
  Configure a side-by-side, horizontal arrangement of components for your article.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/nesting-components-in-an-article)*