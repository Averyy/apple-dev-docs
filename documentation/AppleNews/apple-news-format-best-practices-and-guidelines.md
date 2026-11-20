# Apple News Format Best Practices and Guidelines

**Framework**: Apple News  
**Role**: Article

Create and design engaging Apple News Format articles using these guidelines and best practices.

## Overview

Use this guide to deliver the best experience for people reading your content in Apple News. It contains useful tips and links to [Apple News Format](../AppleNewsFormat/AppleNewsFormat.md) and [Apple News API](../AppleNewsAPI/AppleNewsAPI.md) documentation.

## Article content

- All articles must have a [`Title`](../AppleNewsFormat/title.md). Provide a title that’s between 80 and 110 characters for optimum readability.
- Include author names using the [`Author`](../AppleNewsFormat/author.md) or [`Byline`](../AppleNewsFormat/byline.md) components. To display author names in feeds, use the `authors` property in the [`Metadata`](../AppleNewsFormat/metadata.md) component.
- Use the [`Byline`](../AppleNewsFormat/byline.md) component to include the date and time of publication. Specify your local time zone.
- Make sure opinion articles are labeled clearly. Add terms such as `Opinion:` or `Comment:` at the start of the `title` property in the [`ArticleDocument`](../AppleNewsFormat/articledocument.md).
- Use the [`Body`](../AppleNewsFormat/body.md) component to deliver the complete text of your articles, as they appear in your Owned and Operated (O&O) platforms. Don’t truncate articles or require people to leave the Apple News app to read the full story.
- Map other content elements such as images, videos, or embeds to their corresponding Apple News Format  [Components](./components.md).
- Include a thumbnail image and canonical URL as part of your article  [`Metadata`](../AppleNewsFormat/metadata.md) whenever possible.

## Presentation and delivery

- Make sure your Apple News articles are consistent with their web or print design. Use the same fonts (if your font licenses allow), [`TextStyle`](../AppleNewsFormat/textstyle.md), and [article structure](./planning-the-layout-for-your-article.md) to achieve parity with your O&O platforms.
- Check how your content looks in iOS, iPadOS, and macOS. Use your O&O platforms as a reference.
- Check how your content looks in [Dark Mode](./supporting-dark-mode-for-your-article.md) and make any necessary adjustments.
- Use the `allowAutoplacedAds` property in the [`Container`](../AppleNewsFormat/container.md) component to prevent ads from appearing in unwanted places, such as within promotional modules.
- Make sure images are under 20 MB and article bundles don’t exceed 450 MB. For additional asset specifications, see [Preparing Image, Video, Audio, Music, and ARKit Assets](./preparing-image-video-audio-music-and-arkit-assets.md).
- If you publish archived content, set the `datePublished` property in the [`Metadata`](../AppleNewsFormat/metadata.md) component to the original publication date.

## Credits and disclaimers

- For AI-generated content, including images, video, and audio, set `contentGenerationType` to `AI` in the  [`Metadata`](../AppleNewsFormat/metadata.md) component.
- For syndicated content, set `contentGenerationType` to `syndicated` in the [`Metadata`](../AppleNewsFormat/metadata.md) component.
- To identify sponsored articles, set the `isSponsored` property to `true` in [Create Article Metadata Fields](../AppleNewsAPI/create-article-metadata-fields.md).
- Make sure all disclaimers available on your O&O platforms are included in your Apple News articles.

## Promotional modules

- Don’t place generic banners or branding messages within the first screen. Apple News automatically brands articles with channel names.
- Use the [`Aside`](../AppleNewsFormat/aside.md) component to create any promotional module not directly related to the article.
- You can include in-article modules to promote and support your publication, such as calls for channel follows, newsletter sign-ups, or donations, but they must not appear until after the first screen or exceed 50 percent of the [viewport height](./specifying-measurements-for-components.md) in total. Follow buttons must use the `following` property in the [`Condition`](../AppleNewsFormat/condition.md) component so they are not shown to existing channel followers. App download modules should take people to the App Store.
- You can include in-article recirculation units, but these must not exceed 50 percent of the [viewport height](./specifying-measurements-for-components.md). They must look distinct from the Apple News end-of-article recirculation units and must appear after the first screen or before the last screen. You can also consider [promoting articles](https://support.apple.com/en-gb/guide/news-publisher/apd678c01b8c/icloud) or using the [`LinkedArticle`](../AppleNewsFormat/linkedarticle.md) object.
- Modules that promote other commercial products and services, advertising, or sponsored content are prohibited.

For more information on any of these items, contact your Apple News representative or [submit your feedback here](https://www.apple.com/feedback/apple-news/).

## See Also

### Essentials
- [JSON Concepts and Article Structure](./json-concepts-and-article-structure.md)
  Understand basic JSON concepts and become familiar with the structure of an Apple News Format article.
- [Creating an Article: Main Steps](./creating-an-article-main-steps.md)
  Plan the design for your article and create it in Apple News Format.
- [object ArticleDocument](../AppleNewsFormat/articledocument.md)
  The root object of an Apple News article, that contains required properties, metadata, content, layout, and styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/apple-news-format-best-practices-and-guidelines)*