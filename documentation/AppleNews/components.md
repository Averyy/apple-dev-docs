# Components

**Framework**: Apple News

Understand the types of components that can make up an article.

#### Overview

Components are some of the main objects you use to build your article, along with layouts and styles. Components hold the content of your article and are always in an array called `components`.

Each component in your article has a function that is expressed by a property called `role`. For example, the value of the `role` property might be `title`, `body`, `pullquote`, or `heading`. A component’s role determines what type of component it is. That is, when a component’s `role` is `body`, that type of component is referred to as a `body` component.  See [`JSON Concepts and Article Structure`](json-concepts-and-article-structure.md).

The following table gives you an overview of the components you can use to create an article in Apple News Format.

|  |  |
| --- | --- |
| Text | [`Body`](https://developer.apple.com/documentation/applenewsformat/body), [`Title`](https://developer.apple.com/documentation/applenewsformat/title), [`Heading`](https://developer.apple.com/documentation/applenewsformat/heading) (heading1, heading2, heading3, heading4, heading5, heading6), [`ArticleTitle`](https://developer.apple.com/documentation/applenewsformat/articletitle), [`Intro`](https://developer.apple.com/documentation/applenewsformat/intro), [`Caption`](https://developer.apple.com/documentation/applenewsformat/caption), [`Author`](https://developer.apple.com/documentation/applenewsformat/author), [`Byline`](https://developer.apple.com/documentation/applenewsformat/byline), [`Illustrator`](https://developer.apple.com/documentation/applenewsformat/illustrator), [`Photographer`](https://developer.apple.com/documentation/applenewsformat/photographer), [`Quote`](https://developer.apple.com/documentation/applenewsformat/quote), [`PullQuote`](https://developer.apple.com/documentation/applenewsformat/pullquote) |
| Images | [`Image`](https://developer.apple.com/documentation/applenewsformat/image), [`Photo`](https://developer.apple.com/documentation/applenewsformat/photo), [`Figure`](https://developer.apple.com/documentation/applenewsformat/figure), [`Portrait`](https://developer.apple.com/documentation/applenewsformat/portrait), [`Logo`](https://developer.apple.com/documentation/applenewsformat/logo),  [`ArticleThumbnail`](https://developer.apple.com/documentation/applenewsformat/articlethumbnail) |
| Galleries and Mosaic | [`Gallery`](https://developer.apple.com/documentation/applenewsformat/gallery), [`Mosaic`](https://developer.apple.com/documentation/applenewsformat/mosaic) |
| Audio and Video | [`Audio`](https://developer.apple.com/documentation/applenewsformat/audio), [`EmbedWebVideo`](https://developer.apple.com/documentation/applenewsformat/embedwebvideo), [`Music`](https://developer.apple.com/documentation/applenewsformat/music), [`Podcast`](https://developer.apple.com/documentation/applenewsformat/podcast), [`Video`](https://developer.apple.com/documentation/applenewsformat/video) |
| Location | [`Map`](https://developer.apple.com/documentation/applenewsformat/map), [`Place`](https://developer.apple.com/documentation/applenewsformat/place) |
| Social Media | [`FacebookPost`](https://developer.apple.com/documentation/applenewsformat/facebookpost), [`Instagram`](https://developer.apple.com/documentation/applenewsformat/instagram), [`TikTok`](https://developer.apple.com/documentation/applenewsformat/tiktok), [`Tweet`](https://developer.apple.com/documentation/applenewsformat/tweet) |
| Tables | [`DataTable`](https://developer.apple.com/documentation/applenewsformat/datatable), [`HTMLTable`](https://developer.apple.com/documentation/applenewsformat/htmltable) |
| Advertisements | [`ReplicaAdvertisement`](https://developer.apple.com/documentation/applenewsformat/replicaadvertisement) |
| Article Structure | [`Container`](https://developer.apple.com/documentation/applenewsformat/container), [`Section`](https://developer.apple.com/documentation/applenewsformat/section), [`Chapter`](https://developer.apple.com/documentation/applenewsformat/chapter), [`Aside`](https://developer.apple.com/documentation/applenewsformat/aside), [`Header`](https://developer.apple.com/documentation/applenewsformat/header), [`Divider`](https://developer.apple.com/documentation/applenewsformat/divider), [`ArticleLink`](https://developer.apple.com/documentation/applenewsformat/articlelink), [`LinkButton`](https://developer.apple.com/documentation/applenewsformat/linkbutton) |
| Augmented Reality | [`ARKit`](https://developer.apple.com/documentation/applenewsformat/arkit) |

> **Note**: Choosing the component `role` that best describes your content is important for better voice-over and for facilitating Siri suggestions. For example, instead of styling text in a `body` component to make it look like a heading, use a `heading` component for that text instead.

## Topics

### First Steps
- [Adding Components](adding-components.md)
  Learn the basics for adding components to your article.
- [object Component](../applenewsformat/component.md)
  Properties shared by all component types.
### Text
- [Using HTML with Apple News Format](using-html-with-apple-news-format.md)
  Use HTML formatting for text components.
- [Using Markdown with Apple News Format](using-markdown-with-apple-news-format.md)
  Use Markdown formatting for text components.
- [object Body](../applenewsformat/body.md)
  The component for adding body text.
- [object Title](../applenewsformat/title.md)
  The component for adding an article title.
- [object Heading](../applenewsformat/heading.md)
  The text component for adding a heading.
- [object Intro](../applenewsformat/intro.md)
  The component for adding introductory text.
- [object Caption](../applenewsformat/caption.md)
  The component for adding caption text.
- [object Author](../applenewsformat/author.md)
  The component for adding the name of the author.
- [object Byline](../applenewsformat/byline.md)
  The component for adding the publication date or contributor credits, especially for articles with multiple contributors.
- [object Illustrator](../applenewsformat/illustrator.md)
  The component for adding illustrator credit.
- [object Photographer](../applenewsformat/photographer.md)
  The component for adding a photographer credit.
- [object Quote](../applenewsformat/quote.md)
  The component for including a quote.
- [object PullQuote](../applenewsformat/pullquote.md)
  The component for including a pull quote.
- [object Text](../applenewsformat/text.md)
  Properties shared by all text component types.
### Images
- [object Image](../applenewsformat/image.md)
  The component for displaying JPEG, WebP, PNG, or GIF images.
- [object Photo](../applenewsformat/photo.md)
  The component for including a photograph.
- [object Figure](../applenewsformat/figure.md)
  The component for including a figure.
- [object Portrait](../applenewsformat/portrait.md)
  The component for including an image of a person.
- [object Logo](../applenewsformat/logo.md)
  The component for including a logo image.
- [object ReplicaAdvertisement](../applenewsformat/replicaadvertisement.md)
  The component for delivering digital versions of print advertisements.
- [object CaptionDescriptor](../applenewsformat/captiondescriptor.md)
  The object you use in image components for displaying captions when the image is full-screen.
### Galleries and Mosaics
- [object Gallery](../applenewsformat/gallery.md)
  The component for displaying a sequence of images in a specific order as a horizontal strip.
- [object Mosaic](../applenewsformat/mosaic.md)
  The component for displaying a set of images as tiles in no particular order.
- [object GalleryItem](../applenewsformat/galleryitem.md)
  An object used in a gallery or mosaic component for displaying an individual image.
### Audio and Video
- [object Audio](../applenewsformat/audio.md)
  The component for adding a playable audio clip.
- [object Music](../applenewsformat/music.md)
  The component for adding a playable music file.
- [object Podcast](../applenewsformat/podcast.md)
  The component for adding a Podcast show or episode.
- [object Video](../applenewsformat/video.md)
  The component for adding a video.
- [object EmbedWebVideo](../applenewsformat/embedwebvideo.md)
  The component for adding a web video from Dailymotion, Vimeo, or YouTube.
### Location
- [object Map](../applenewsformat/map.md)
  The component for adding a map.
- [object MapItem](../applenewsformat/mapitem.md)
  An object used in a map component for specifying the location of a map pin.
- [object MapSpan](../applenewsformat/mapspan.md)
  An object used in a map or place component for defining the visible area of the map.
- [object Place](../applenewsformat/place.md)
  The component for adding a map with a specific point of interest.
### Social Media
- [object Instagram](../applenewsformat/instagram.md)
  The component for adding an Instagram post.
- [object FacebookPost](../applenewsformat/facebookpost.md)
  The component for adding a Facebook post.
- [object TikTok](../applenewsformat/tiktok.md)
  The component for adding a TikTok post.
- [object Tweet](../applenewsformat/tweet.md)
  The component for adding a Tweet that was posted to Twitter.
### Augmented Reality
- [object ARKit](../applenewsformat/arkit.md)
  The component for adding an augmented reality (AR) experience to your article.
### Tables
- [Tables in an Article](tables-in-an-article.md)
  Add a JSON or HTML data table, and understand  the options for changing the look of your table.
### Advertisements
- [object BannerAdvertisement](../applenewsformat/banneradvertisement.md)
  The component for adding a full-width banner ad.
- [object MediumRectangleAdvertisement](../applenewsformat/mediumrectangleadvertisement.md)
  The component for adding a medium, fixed-size rectangle ad.
### Article Structure
- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Adding a Scene to a Chapter or a Section Header](adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
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
- [object ArticleTitle](../applenewsformat/articletitle.md)
  The component for displaying an article title in the ArticleLink component.
- [object ArticleThumbnail](../applenewsformat/articlethumbnail.md)
  The component for displaying a thumbnail image with an article link.
- [object LinkButton](../applenewsformat/linkbutton.md)
  The component for opening a link in a button.
### Animations
- [About Component Animations](about-component-animations.md)
  Learn how to affect the way in which components come into view.
- [object ComponentAnimation](../applenewsformat/componentanimation.md)
  Properties that all types of animations share.
- [object AppearAnimation](../applenewsformat/appearanimation.md)
  An animation type whereby a component appears on the screen.
- [object FadeInAnimation](../applenewsformat/fadeinanimation.md)
  The animation whereby a component fades into view.
- [object MoveInAnimation](../applenewsformat/moveinanimation.md)
  The animation whereby a component moves in from the side of the screen.
- [object ScaleFadeAnimation](../applenewsformat/scalefadeanimation.md)
  The animation in which a component scales up and fades into view.
### Behaviors
- [About Component Behaviors](about-component-behaviors.md)
  Learn how to affect components’ reactions to device motion and scrolling.
- [object Behavior](../applenewsformat/behavior.md)
  Properties shared by all the behaviors you can use to affect how components react to device motion and scrolling.
- [object BackgroundMotion](../applenewsformat/backgroundmotion.md)
  The behavior whereby the background of a component moves in the opposite direction from the motion of the device.
- [object BackgroundParallax](../applenewsformat/backgroundparallax.md)
  The behavior whereby the background of a component moves slightly slower than a person’s scroll speed.
- [object Motion](../applenewsformat/motion.md)
  The behavior whereby a component reacts to the motion of the person’s device.
- [object Parallax](../applenewsformat/parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object Springy](../applenewsformat/springy.md)
  The behavior whereby a component acts as if it’s on a short spring.
### Links
- [object LinkAddition](../applenewsformat/linkaddition.md)
  The addition object for defining links in text components that don’t use HTML or Markdown formatting.
- [object ComponentLink](../applenewsformat/componentlink.md)
  The component addition object for making a component interactive and opening a link to another location in News.
- [object Addition](../applenewsformat/addition.md)
  Properties that all addition types share.
- [object ComponentAddition](../applenewsformat/componentaddition.md)
  Properties that all types of component additions share.
- [type SupportedURLs](../applenewsformat/supportedurls.md)
  Links that go to Apple News, other Apple apps, and external sites.
- [type SupportedInternalURLs](../applenewsformat/supportedinternalurls.md)
  Links that go to Apple News and other Apple apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/components)*