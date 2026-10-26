# Components

**Framework**: Apple News  
**Role**: API Collection

Understand the types of components that can make up an article.

#### Overview

Components are some of the main objects you use to build your article, along with layouts and styles. Components hold the content of your article and are always in an array called `components`.

Each component in your article has a function that is expressed by a property called `role`. For example, the value of the `role` property might be `title`, `body`, `pullquote`, or `heading`. A component’s role determines what type of component it is. That is, when a component’s `role` is `body`, that type of component is referred to as a `body` component.  See [JSON Concepts and Article Structure](./json-concepts-and-article-structure.md).

The following table gives you an overview of the components you can use to create an article in Apple News Format.

| **Component category** | **Component types** |
| --- | --- |
| Text | [`Body`](../AppleNewsFormat/body.md), [`Title`](../AppleNewsFormat/title.md), [`Heading`](../AppleNewsFormat/heading.md) (heading1, heading2, heading3, heading4, heading5, heading6), [`ArticleTitle`](../AppleNewsFormat/articletitle.md), [`Intro`](../AppleNewsFormat/intro.md), [`Caption`](../AppleNewsFormat/caption.md), [`Author`](../AppleNewsFormat/author.md), [`Byline`](../AppleNewsFormat/byline.md), [`Illustrator`](../AppleNewsFormat/illustrator.md), [`Photographer`](../AppleNewsFormat/photographer.md), [`Quote`](../AppleNewsFormat/quote.md), [`PullQuote`](../AppleNewsFormat/pullquote.md) |
| Images | [`Image`](../AppleNewsFormat/image.md), [`Photo`](../AppleNewsFormat/photo.md), [`Figure`](../AppleNewsFormat/figure.md), [`Portrait`](../AppleNewsFormat/portrait.md), [`Logo`](../AppleNewsFormat/logo.md),  [`ArticleThumbnail`](../AppleNewsFormat/articlethumbnail.md) |
| Galleries and Mosaic | [`Gallery`](../AppleNewsFormat/gallery.md), [`Mosaic`](../AppleNewsFormat/mosaic.md) |
| Audio and Video | [`Audio`](../AppleNewsFormat/audio.md), [`EmbedWebVideo`](../AppleNewsFormat/embedwebvideo.md), [`Music`](../AppleNewsFormat/music.md), [`Podcast`](../AppleNewsFormat/podcast.md), [`Video`](../AppleNewsFormat/video.md) |
| Location | [`Map`](../AppleNewsFormat/map.md), [`Place`](../AppleNewsFormat/place.md) |
| Social Media | [`FacebookPost`](../AppleNewsFormat/facebookpost.md), [`Instagram`](../AppleNewsFormat/instagram.md), [`TikTok`](../AppleNewsFormat/tiktok.md), [`Tweet`](../AppleNewsFormat/tweet.md) |
| Tables | [`DataTable`](../AppleNewsFormat/datatable.md), [`HTMLTable`](../AppleNewsFormat/htmltable.md) |
| Advertisements | [`ReplicaAdvertisement`](../AppleNewsFormat/replicaadvertisement.md) |
| Article Structure | [`Container`](../AppleNewsFormat/container.md), [`Section`](../AppleNewsFormat/section.md), [`Chapter`](../AppleNewsFormat/chapter.md), [`Aside`](../AppleNewsFormat/aside.md), [`Header`](../AppleNewsFormat/header.md), [`Divider`](../AppleNewsFormat/divider.md), [`ArticleLink`](../AppleNewsFormat/articlelink.md), [`LinkButton`](../AppleNewsFormat/linkbutton.md) |
| Augmented Reality | [`ARKit`](../AppleNewsFormat/arkit.md) |

> **Note**: Choosing the component `role` that best describes your content is important for better voice-over and for facilitating Siri suggestions. For example, instead of styling text in a `body` component to make it look like a heading, use a `heading` component for that text instead.

## Topics

### First Steps
- [Adding Components](./adding-components.md)
  Learn the basics for adding components to your article.
- [object Component](../AppleNewsFormat/component.md)
  Properties shared by all component types.
### Text
- [Using HTML with Apple News Format](./using-html-with-apple-news-format.md)
  Use HTML formatting for text components.
- [Using Markdown with Apple News Format](./using-markdown-with-apple-news-format.md)
  Use Markdown formatting for text components.
- [object Body](../AppleNewsFormat/body.md)
  The component for adding body text.
- [object Title](../AppleNewsFormat/title.md)
  The component for adding an article title.
- [object Heading](../AppleNewsFormat/heading.md)
  The text component for adding a heading.
- [object Intro](../AppleNewsFormat/intro.md)
  The component for adding introductory text.
- [object Caption](../AppleNewsFormat/caption.md)
  The component for adding caption text.
- [object Author](../AppleNewsFormat/author.md)
  The component for adding the name of the author.
- [object Byline](../AppleNewsFormat/byline.md)
  The component for adding the publication date or contributor credits, especially for articles with multiple contributors.
- [object Illustrator](../AppleNewsFormat/illustrator.md)
  The component for adding illustrator credit.
- [object Photographer](../AppleNewsFormat/photographer.md)
  The component for adding a photographer credit.
- [object Quote](../AppleNewsFormat/quote.md)
  The component for including a quote.
- [object PullQuote](../AppleNewsFormat/pullquote.md)
  The component for including a pull quote.
- [object Text](../AppleNewsFormat/text.md)
  Properties shared by all text component types.
### Images
- [object Image](../AppleNewsFormat/image.md)
  The component for displaying JPEG, WebP, PNG, or GIF images.
- [object Photo](../AppleNewsFormat/photo.md)
  The component for including a photograph.
- [object Figure](../AppleNewsFormat/figure.md)
  The component for including a figure.
- [object Portrait](../AppleNewsFormat/portrait.md)
  The component for including an image of a person.
- [object Logo](../AppleNewsFormat/logo.md)
  The component for including a logo image.
- [object ReplicaAdvertisement](../AppleNewsFormat/replicaadvertisement.md)
  The component for delivering digital versions of print advertisements.
- [object CaptionDescriptor](../AppleNewsFormat/captiondescriptor.md)
  The object you use in image components for displaying captions when the image is full-screen.
### Galleries and Mosaics
- [object Gallery](../AppleNewsFormat/gallery.md)
  The component for displaying a sequence of images in a specific order as a horizontal strip.
- [object Mosaic](../AppleNewsFormat/mosaic.md)
  The component for displaying a set of images as tiles in no particular order.
- [object GalleryItem](../AppleNewsFormat/galleryitem.md)
  An object used in a gallery or mosaic component for displaying an individual image.
### Audio and Video
- [object Audio](../AppleNewsFormat/audio.md)
  The component for adding a playable audio clip.
- [object Music](../AppleNewsFormat/music.md)
  The component for adding a playable music file.
- [object Podcast](../AppleNewsFormat/podcast.md)
  The component for adding a Podcast show or episode.
- [object Video](../AppleNewsFormat/video.md)
  The component for adding a video.
- [object EmbedWebVideo](../AppleNewsFormat/embedwebvideo.md)
  The component for adding a web video from Dailymotion, Vimeo, or YouTube.
### Location
- [object Map](../AppleNewsFormat/map.md)
  The component for adding a map.
- [object MapItem](../AppleNewsFormat/mapitem.md)
  An object used in a map component for specifying the location of a map pin.
- [object MapSpan](../AppleNewsFormat/mapspan.md)
  An object used in a map or place component for defining the visible area of the map.
- [object Place](../AppleNewsFormat/place.md)
  The component for adding a map with a specific point of interest.
### Social Media
- [object Instagram](../AppleNewsFormat/instagram.md)
  The component for adding an Instagram post.
- [object FacebookPost](../AppleNewsFormat/facebookpost.md)
  The component for adding a Facebook post.
- [object TikTok](../AppleNewsFormat/tiktok.md)
  The component for adding a TikTok post.
- [object Tweet](../AppleNewsFormat/tweet.md)
  The component for adding a Tweet that was posted to Twitter.
### Augmented Reality
- [object ARKit](../AppleNewsFormat/arkit.md)
  The component for adding an augmented reality (AR) experience to your article.
### Tables
- [Tables in an Article](./tables-in-an-article.md)
  Add a JSON or HTML data table, and understand  the options for changing the look of your table.
### Advertisements
- [object BannerAdvertisement](../AppleNewsFormat/banneradvertisement.md)
  The component for adding a full-width banner ad.
- [object MediumRectangleAdvertisement](../AppleNewsFormat/mediumrectangleadvertisement.md)
  The component for adding a medium, fixed-size rectangle ad.
### Article Structure
- [Nesting Components in an Article](./nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
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
- [object ArticleTitle](../AppleNewsFormat/articletitle.md)
  The component for displaying an article title in the ArticleLink component.
- [object ArticleThumbnail](../AppleNewsFormat/articlethumbnail.md)
  The component for displaying a thumbnail image with an article link.
- [object LinkButton](../AppleNewsFormat/linkbutton.md)
  The component for opening a link in a button.
### Animations
- [About Component Animations](./about-component-animations.md)
  Learn how to affect the way in which components come into view.
- [object ComponentAnimation](../AppleNewsFormat/componentanimation.md)
  Properties that all types of animations share.
- [object AppearAnimation](../AppleNewsFormat/appearanimation.md)
  An animation type whereby a component appears on the screen.
- [object FadeInAnimation](../AppleNewsFormat/fadeinanimation.md)
  The animation whereby a component fades into view.
- [object MoveInAnimation](../AppleNewsFormat/moveinanimation.md)
  The animation whereby a component moves in from the side of the screen.
- [object ScaleFadeAnimation](../AppleNewsFormat/scalefadeanimation.md)
  The animation in which a component scales up and fades into view.
### Behaviors
- [About Component Behaviors](./about-component-behaviors.md)
  Learn how to affect components’ reactions to device motion and scrolling.
- [object Behavior](../AppleNewsFormat/behavior.md)
  Properties shared by all the behaviors you can use to affect how components react to device motion and scrolling.
- [object BackgroundMotion](../AppleNewsFormat/backgroundmotion.md)
  The behavior whereby the background of a component moves in the opposite direction from the motion of the device.
- [object BackgroundParallax](../AppleNewsFormat/backgroundparallax.md)
  The behavior whereby the background of a component moves slightly slower than a person’s scroll speed.
- [object Motion](../AppleNewsFormat/motion.md)
  The behavior whereby a component reacts to the motion of the person’s device.
- [object Parallax](../AppleNewsFormat/parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object Springy](../AppleNewsFormat/springy.md)
  The behavior whereby a component acts as if it’s on a short spring.
### Links
- [object LinkAddition](../AppleNewsFormat/linkaddition.md)
  The addition object for defining links in text components that don’t use HTML or Markdown formatting.
- [object ComponentLink](../AppleNewsFormat/componentlink.md)
  The component addition object for making a component interactive and opening a link to another location in News.
- [object Addition](../AppleNewsFormat/addition.md)
  Properties that all addition types share.
- [object ComponentAddition](../AppleNewsFormat/componentaddition.md)
  Properties that all types of component additions share.
- [type SupportedURLs](../AppleNewsFormat/supportedurls.md)
  Links that go to Apple News, other Apple apps, and external sites.
- [type SupportedInternalURLs](../AppleNewsFormat/supportedinternalurls.md)
  Links that go to Apple News and other Apple apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/components)*