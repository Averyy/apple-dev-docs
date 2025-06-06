# Adding a Scene to a Chapter or a Section Header

**Framework**: Apple News

Add a scene to your article to create special effects.

#### Overview

Apple News Format provides animations (see [`About Component Animations`](about-component-animations.md)) and behaviors (see [`About Component Behaviors`](about-component-behaviors.md)) to use with individual components in your article, but you can also use a  — a combination of animations and behaviors — to control how a section or chapter of your article comes into view.

A scene combines animations and behaviors to create special effects that you can use with the headers in `section` and `chapter` components. Apple News Format has two scenes you can use to add interest to your article:

- [`FadingStickyHeader`](https://developer.apple.com/documentation/applenewsformat/fadingstickyheader). Causes the header to briefly “stick” to the top of the screen and then fade to a defined color.
- [`ParallaxScaleHeader`](https://developer.apple.com/documentation/applenewsformat/parallaxscaleheader). Causes the header to zoom out and scroll more slowly than the user is scrolling, giving the impression of a parallax effect.

To add a scene, do the following:

1. In  the components array of your [`Section`](https://developer.apple.com/documentation/applenewsformat/section) or [`Chapter`](https://developer.apple.com/documentation/applenewsformat/chapter), add a [`Header`](https://developer.apple.com/documentation/applenewsformat/header).
2. In the `scene` property of the section or chapter component, specify which scene you want to use (`fading_sticky_header` or `parallax_scale`). See the example code in [`FadingStickyHeader`](https://developer.apple.com/documentation/applenewsformat/fadingstickyheader).

## Topics

### Scene Types
- [object Scene](../applenewsformat/scene.md)
  A combination of animations and behaviors to use in sections and chapters that have headers.
- [object FadingStickyHeader](../applenewsformat/fadingstickyheader.md)
  The scene that briefly keeps a header at the top of the screen as the person scrolls through the article.
- [object ParallaxScaleHeader](../applenewsformat/parallaxscaleheader.md)
  The scene that gives the impression of a parallax effect by zooming out and scrolling slightly more slowly than the person’s action.

## See Also

- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Creating an Article Link](creating-an-article-link.md)
  Link to an article by using the article-linking container component.
- [Displaying Components Side By Side](displaying-components-side-by-side.md)
  Configure a side-by-side, horizontal arrangement of components for your article.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-a-scene-to-a-chapter-or-a-section-header)*