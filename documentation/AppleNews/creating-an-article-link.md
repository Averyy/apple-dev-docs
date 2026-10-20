# Creating an Article Link

**Framework**: Apple News  
**Role**: Article

Link to an article by using the article-linking container component.

#### Overview

Use the [`ArticleLink`](https://developer.apple.com/documentation/applenewsformat/articlelink) component to create a link to another Apple News Format article. To create a link, nest child components inside the `ArticleLink` component. You can use these child components to provide content, styling, and layout, like you do with any other Apple News Format component.

The two special components that you can use inside an `ArticleLink` container are [`ArticleThumbnail`](https://developer.apple.com/documentation/applenewsformat/articlethumbnail) and [`ArticleTitle`](https://developer.apple.com/documentation/applenewsformat/articletitle).  VoiceOver uses these components to make Apple News content more accessible. Apple News automatically populates their content; for example, if you define the `ArticleTitle` component without explicitly defining the `text` property,  Apple News uses the title of the linked article.

## See Also

### Article Structure
- [Nesting Components in an Article](./nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Adding a Scene to a Chapter or a Section Header](./adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
- [Displaying Components Side By Side](./displaying-components-side-by-side.md)
  Configure a side-by-side, horizontal arrangement of components for your article.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-an-article-link)*