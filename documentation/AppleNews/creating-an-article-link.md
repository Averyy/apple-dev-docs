# Creating an Article Link

**Framework**: Apple News

Link to an article by using the article-linking container component.

#### Overview

Use the [`ArticleLink`](https://developer.apple.com/documentation/applenewsformat/articlelink) component to create a link to another Apple News Format article. To create a link, nest child components inside the `ArticleLink` component. You can use these child components to provide content, styling, and layout, like you do with any other Apple News Format component.

The two special components that you can use inside an `ArticleLink` container are [`ArticleThumbnail`](https://developer.apple.com/documentation/applenewsformat/articlethumbnail) and [`ArticleTitle`](https://developer.apple.com/documentation/applenewsformat/articletitle).  VoiceOver uses these components to make Apple News content more accessible. Apple News automatically populates their content; for example, if you define the `ArticleTitle` component without explicitly defining the `text` property,  Apple News uses the title of the linked article.

## See Also

- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Adding a Scene to a Chapter or a Section Header](adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-an-article-link)*