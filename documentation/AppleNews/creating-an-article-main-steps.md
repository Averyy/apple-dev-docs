# Creating an Article: Main Steps

**Framework**: Apple News  
**Role**: Article

Plan the design for your article and create it in Apple News Format.

## Overview

When you create an article in Apple News Format, you start by creating a JSON document file. The file contains code that specifies the layout for your article, provides the content, and customizes the look. The system processes the JSON file and renders it as an article in Apple News.

Your article in Apple News must contain the following:

- A headline for the article. Use the [`Title`](../AppleNewsFormat/title.md) component.
- An author for the article. Use the [`Author`](../AppleNewsFormat/author.md) component to include the name of one of the authors of the article. Alternatively, you can use the [`Byline`](../AppleNewsFormat/byline.md) component for adding contributors to your article.
- The publication date of the article. Use either the [`Metadata`](../AppleNewsFormat/metadata.md), `datePublished` property or the [`Byline`](../AppleNewsFormat/byline.md) component.
- The complete text of the article, as it appears in either print or on the publisher’s website. Use the [`Body`](../AppleNewsFormat/body.md) component. Don’t truncate articles or require people to leave the Apple News app to read the full story.

You can also include a thumbnail URL to use in the article tile. See the [`Metadata`](../AppleNewsFormat/metadata.md), `thumbnailURL` property.

Avoid using generic banners or branding messages at the top of articles, because the system automatically brands articles with channel names. Redundant branding pushes down the article’s content, forcing people to scroll to view it.

You can include in-article modules to promote and support your publication, like channel follow buttons, newsletter sign-up calls, donations, and other campaigns, but they must not appear until after the first screen.

You can include in-article recirculation units, but these must not exceed 50 percent of the [viewport height](./specifying-measurements-for-components.md). They must look distinct from the Apple News end-of-article recirculation units and must appear after the first screen or before the last screen. You can also consider [promoting articles](https://support.apple.com/en-gb/guide/news-publisher/apd678c01b8c/icloud) or using the  [`LinkedArticle`](../AppleNewsFormat/linkedarticle.md) object.

Modules that promote other products and services, advertising, or commercial content are prohibited.

The following figure shows the basic tasks associated with creating an article.

![Flow diagram showing the steps to publish an article to Apple News. ](https://developer.apple.com/tutorials/images/com.apple.applenews/media-3975561@2x.png)

### Main Steps

> **Note**:  Before you start, download [News Preview](https://developer.apple.com/news-preview/) and follow the instructions to choose the devices you want to preview on. Then, as you create your article, you can drag your `article.json` file to the News Preview window to see how your content will look in Apple News.

1. **Create an** `article.json` **document file**. All article document files must have the name `article.json.` Start by adding the [`ArticleDocument`](../AppleNewsFormat/articledocument.md) object and its required properties, or download this [sample file](https://developer.apple.com/news-publisher/download/Apple_News_Starter_Article.zip). You can use any text editor to edit the code in your `article.json` file. See [Choose a Text Editor](./setting-up-the-introductory-tutorial.md#Choose-a-Text-Editor). Create a unique folder to hold the `article.json` file and any other files you’ll publish with this article, such as image files.
2. **Plan the layout of your article**. Decide how many layout columns your design needs. See [Planning the Layout for Your Article](./planning-the-layout-for-your-article.md).
3. **Add components that contain your article’s content**. The content of your article — the text, photos, and other information — is contained in an array of components in your `article.json` file. Each component has a specific function — for example, a title, a caption, body text, or a video. For an overview of the different kinds of components you can have in your article, see [Components](./components.md); to learn how to add components, see [Adding Components](./adding-components.md).
4. **Position the components in your article**. Use the [`ComponentLayout`](../AppleNewsFormat/componentlayout.md) object to specify where each component will appear horizontally in your article document. See [Positioning the Content in Your Article](./positioning-the-content-in-your-article.md).
5. **Customize the appearance of your article**. Include styles, animations, behaviors, and other effects. See [Enhancing Your Articles with Styles](./enhancing-your-articles-with-styles.md) and [About Component Animations](./about-component-animations.md).
6. **Add the metadata for your article**. See [`Metadata`](../AppleNewsFormat/metadata.md).

Once your article is finished, you can publish it to Apple News. See [`Create an Article`](../AppleNewsAPI/post-channels-_channelid_-articles.md).

## See Also

### Essentials
- [JSON Concepts and Article Structure](./json-concepts-and-article-structure.md)
  Understand basic JSON concepts and become familiar with the structure of an Apple News Format article.
- [object ArticleDocument](../AppleNewsFormat/articledocument.md)
  The root object of an Apple News article, that contains required properties, metadata, content, layout, and styles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-an-article-main-steps)*