# Apple News Format

**Framework**: AppleNewsFormat  
**Kind**: module  
**Role**: Web Service

Get Apple News Format reference information, and create signature content for Apple News.

## Overview

Apple News Format is the JavaScript Object Notation (JSON) format you use to create articles for Apple News.

An article created in Apple News Format can include text, images, audio, video, embedded social media, photo galleries, data tables, and interactive maps. You can enhance your article with animations, behaviors, and customized styles that let you create a unique look for your content. Your finished article is processed and rendered in Apple News.

![Screenshot of an Apple News article on iPad.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-3596705@2x.png)

With Apple News Format, you only have to author your content once. News automatically optimizes your articles for iPhone, iPad, Mac, and Apple Vision Pro to give your readers the best experience for their device.

## Topics

### Release Notes
- [Apple News Format Release Notes](../AppleNews/apple-news-format-release-notes.md)
  Learn about new features that require iOS 26, iPadOS 26, and macOS 26.
- [Apple News Format Version History](../AppleNews/apple-news-format-version-history.md)
  Learn how Apple News Format versions map to iOS, iPadOS, macOS, and visionOS releases.
### Essentials
- [JSON Concepts and Article Structure](../AppleNews/json-concepts-and-article-structure.md)
  Understand basic JSON concepts and become familiar with the structure of an Apple News Format article.
- [Creating an Article: Main Steps](../AppleNews/creating-an-article-main-steps.md)
  Plan the design for your article and create it in Apple News Format.
- [object ArticleDocument](./articledocument.md)
  The root object of an Apple News article, that contains required properties, metadata, content, layout, and styles.
### Article Display
- [Changing the Appearance of Your Article Tile in Feeds](../AppleNews/changing-the-appearance-of-your-article-tile-in-feeds.md)
  Change the information that News displays about your published article.
### Article Metadata
- [object Metadata](./metadata.md)
  Information about your article, including author name, creation date, publication date, keywords, and excerpt.
- [object LinkedArticle](./linkedarticle.md)
  A relationship between your article and another Apple News article.
- [object Issue](./issue.md)
  The object for defining information about an issue.
### Article Layout
- [Planning the Layout for Your Article](../AppleNews/planning-the-layout-for-your-article.md)
  Define a layout that supports the look you want for your article.
- [Positioning the Content in Your Article](../AppleNews/positioning-the-content-in-your-article.md)
  Align article components with columns in your layout.
- [Wrapping Text Around a Component](../AppleNews/wrapping-text-around-a-component.md)
  Define the layout of a text component to wrap around another component.
- [object Layout](./layout.md)
  The object for defining columns, gutters, and margins for your article’s designed width.
- [object ComponentLayout](./componentlayout.md)
  The object for defining the positioning for a specific component within the article’s column system.
- [object Anchor](./anchor.md)
  The object for anchoring one component to another component in your article’s layout.
- [object Margin](./margin.md)
  The object for defining the space above and below a component.
- [object AutoPlacementLayout](./autoplacementlayout.md)
  The object for defining the margin above and below advertising components.
- [object AdvertisingLayout](./advertisinglayout.md)
  The object for defining the margin above and below advertising components.
### Article Content
- [Components](../AppleNews/components.md)
  Understand the types of components that can make up an article.
### Styles
- [Enhancing Your Articles with Styles](../AppleNews/enhancing-your-articles-with-styles.md)
  Improve the appearance of the text and components in your article by using Apple News Format styles.
- [Supporting Dark Mode for Your Article](../AppleNews/supporting-dark-mode-for-your-article.md)
  Update your article template so that your article adapts when Dark Mode is active.
- [object DocumentStyle](./documentstyle.md)
  The object for setting the background color for your article.
- [Text Styles](../AppleNews/text-styles.md)
  Learn about text styles and how to apply them to your text and text components.
- [Component Styles](../AppleNews/component-styles.md)
  Learn to use component styles to add borders, set background colors, and apply background images to components and to set the styling for tables.
- [Supported Color Names](../AppleNews/supported-color-names.md)
  Learn the color names supported in Apple News Format.
- [type Color](./color.md)
  The strings for defining colors in Apple News Format.
### Dynamic Advertising
- [Managing Advertisements in Your Channel](../AppleNews/managing-advertisements-in-your-channel.md)
  Set the layout and frequency of ads automatically inserted in an article.
- [object AutoPlacement](./autoplacement.md)
  The object for automatically placing components within Apple News Format articles.
- [object AdvertisementAutoPlacement](./advertisementautoplacement.md)
  The object for defining the automatic placement of advertisements.
- [object AdvertisingSettings](./advertisingsettings.md)
  The object for defining properties that affect the frequency and placement with which banner advertisements and medium rectangle advertisements are automatically placed in your article.
### Conditional Design Elements
- [object Condition](./condition.md)
  The object for defining a condition that, when met, causes conditional properties to go into effect.
- [object ConditionalComponent](./conditionalcomponent.md)
  The object for defining conditional properties for a component, and when the conditional properties are in effect.
- [object ConditionalComponentLayout](./conditionalcomponentlayout.md)
  The object for defining conditional properties for a component layout, and when the conditional properties are in effect.
- [object ConditionalAutoPlacement](./conditionalautoplacement.md)
  The object for defining conditional properties for an automatically placed component, and when the conditional properties are in effect.
- [object ConditionalSection](./conditionalsection.md)
  The object for defining conditional properties for a section component, and when the conditional properties are in effect.
- [object ConditionalDocumentStyle](./conditionaldocumentstyle.md)
  The object for defining conditional properties for a document style, and when the conditional properties are in effect.
- [object ConditionalText](./conditionaltext.md)
  The object for defining conditional properties for a text component, and when the conditional properties are in effect.
- [object ConditionalTextStyle](./conditionaltextstyle.md)
  The object for defining conditional properties for a text style, and when the conditional properties are in effect.
- [object ConditionalComponentTextStyle](./conditionalcomponenttextstyle.md)
  The object for defining conditional properties for a component text style, and when the conditional properties are in effect.
- [object ConditionalComponentStyle](./conditionalcomponentstyle.md)
  The object for defining conditional properties for a component style, and when the conditional properties are in effect.
- [object ConditionalContainer](./conditionalcontainer.md)
  The object for defining conditional properties for a container component, and when the conditional properties are in effect.
- [object ConditionalDivider](./conditionaldivider.md)
  The object for defining conditional properties for a divider component, and when the conditional properties are in effect.
- [object ConditionalButton](./conditionalbutton.md)
  The object for defining a button component’s conditional properties, and when the conditional properties are in effect.
### Component Measurements and Media Guidelines
- [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md)
  Specify the units of measure to use for margins, minimum heights, and other dimensions.
- [type SupportedUnits](./supportedunits.md)
  The units of measurement Apple News Format supports.
- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)
  Add media assets to your article.

## See Also

### Article Design and Creation
- [Apple News Format Tutorials](../AppleNews/apple-news-format-tutorials.md)
  Create a basic article and then add advanced design features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat)*