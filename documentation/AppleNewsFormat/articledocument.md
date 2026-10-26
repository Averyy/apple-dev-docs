# ArticleDocument

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The root object of an Apple News article, that contains required properties, metadata, content, layout, and styles.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ArticleDocument
```

## Mentions

- [Changing the Appearance of Your Article Tile in Feeds](../AppleNews/changing-the-appearance-of-your-article-tile-in-feeds.md)
- [Adding Components](../AppleNews/adding-components.md)
- [Creating an Article: Main Steps](../AppleNews/creating-an-article-main-steps.md)
- [Enhancing Your Articles with Styles](../AppleNews/enhancing-your-articles-with-styles.md)
- [JSON Concepts and Article Structure](../AppleNews/json-concepts-and-article-structure.md)

#### Discussion

Every Apple News Format document must have the same filename: `article.json`. An `article.json` file must contain the `ArticleDocument` object. This is the object that is sent in [`Create an Article`](../AppleNewsAPI/post-channels-_channelid_-articles.md) and [`Update an Article`](../AppleNewsAPI/post-articles-_articleid_.md) requests.

> ⚠️ **Warning**:  Every Apple News Format document must contain all items marked as required in the preceding Properties list. Apple News API and [News Preview](https://developer.apple.com/news-preview/) display errors if you omit any required properties. See [`Create an Article`](../AppleNewsAPI/post-channels-_channelid_-articles.md) and [`Update an Article`](../AppleNewsAPI/post-articles-_articleid_.md).

In JSON, the order of properties in an object is not important; however, as you create your JSON document, you may find it useful to follow the order shown in the example that follows.

To view this example in News Preview, copy the example code to a file named `article.json` and put a file named `image.jpg` in the same folder. (You can use any JPEG, GIF, or PNG file.)

##### Example

```json
{
 "version": "1.7",
 "identifier": "SampleArticle",
 "language": "en",
 "title": "Apple News",
 "layout": {
   "columns": 20,
   "width": 1024,
   "margin": 60,
   "gutter": 20
 },
 "documentStyle": {
   "backgroundColor": "#F7F7F7"
 },
 "textFormat": "none",
 "components": [
   {
     "role": "title",
     "text": "Apple News App",
     "textStyle": "title"
   },
   {
     "role": "body",
     "text": "The Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
   },
   {
     "role": "photo",
     "URL": "bundle://image.jpg"
   }
 ],
 "componentTextStyles": {
   "default": {
     "fontName": "Helvetica",
     "fontSize": 13,
     "linkStyle": {
       "textColor": "#428bca"
     }
   },
   "title": {
     "fontName": "Helvetica-Bold",
     "fontSize": 30,
     "hyphenation": false
   },
   "default-body": {
     "fontName": "Helvetica",
     "fontSize": 13
   }
 }
}
```

## Topics

### Objects
- [object ArticleDocument.componentLayouts](./articledocument/componentlayouts-data.dictionary.md)
  An object containing component layout objects that components in the article can refer to.
- [object ArticleDocument.componentStyles](./articledocument/componentstyles-data.dictionary.md)
  An object containing component style objects that components in the article can refer to.
- [object ArticleDocument.componentTextStyles](./articledocument/componenttextstyles-data.dictionary.md)
  An object containing component text style defaults as well as component text styles that components in the article can use.
- [object ArticleDocument.textStyles](./articledocument/textstyles-data.dictionary.md)
  An object containing text style objects that components within this document can refer to inline in text.
- [object ArticleDocument.colorScheme](./articledocument/colorscheme-data.dictionary.md)
  The object that contains information about the color scheme of the document, including Dark Mode behavior.

## Properties

- `components` ([Component]) *(required)*: An array of components that form the content of this article. Components have different roles and types, such as [`Photo`](./photo.md) and [`Music`](./music.md).
- `componentTextStyles` (ArticleDocument.componentTextStyles) *(required)*: The component text styles that components in this document can refer to. Each `article.json` file must have, at minimum, a default component text style named `default`. You can also set defaults by component role. See [Defining and Applying Text Styles](../AppleNews/defining-and-applying-text-styles.md).
- `identifier` (string) *(required)*: A unique, publisher-provided identifier for this article. This identifier must remain constant; you can’t change it when you update the article. See [`PublisherArticleIdentifier`](./publisherarticleidentifier.md).

  This identifier can include the following:

  - Up to 64 characters
  - Uppercase and lowercase letters
  - Numbers
  - Hyphens
  - Underscores
- `language` (string) *(required)*: A code that indicates the language of the article. Use the [IANA.org language subtag registry](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) to find the appropriate code; example, `en` for example English, or the more specific `en-GB` for English (U.K.) or `en-US` for English (U.S.).

  The following is a list of language codes for territories where Apple News is available:

  - `en-US`: English (United States)
  - `en-GB`: English (United Kingdom)
  - `en-AU`: English (Australia)
  - `en-CA`: English (Canada)
  - `fr-CA`: French (Canada)
- `layout` (Layout) *(required)*: The article’s column system. Apple News Format layouts make it possible to recreate print design on iPhone, iPad, Mac, and Apple Vision Pro. Apple News Format uses the layout information to calculate relative positioning and size for these devices. See [Planning the Layout for Your Article](../AppleNews/planning-the-layout-for-your-article.md).
- `title` (string) *(required)*: The article title or headline. Use plain text; formatted text (HTML or Markdown) isn’t supported.
- `version` (string) *(required)*: The version of Apple News Format you use in the JSON document.

  The value of the `version` property must not be earlier than the version number of any property that you use anywhere in the article.

  See [Apple News Format Version History](../AppleNews/apple-news-format-version-history.md).
- `advertisingSettings` (AdvertisingSettings) *(deprecated)*: An advertisement to be inserted at a position that is both possible and optimal. You can specify what `bannerType` you want to have automatically inserted.

  Note. This property is deprecated. Use the [`AdvertisementAutoPlacement`](./advertisementautoplacement.md) object instead.
- `autoplacement` (AutoPlacement) *(deprecated)*: The metadata, appearance, and placement of advertising and related content components within Apple News Format articles.
- `colorScheme` (ArticleDocument.colorScheme): The c`olorScheme` object that you use for automatic Dark Mode behavior.
- `componentLayouts` (ArticleDocument.componentLayouts): The article-level `ComponentLayout` objects that you can refer to by their key within the `ComponentLayouts` object. See [Positioning the Content in Your Article](../AppleNews/positioning-the-content-in-your-article.md).
- `componentStyles` (ArticleDocument.componentStyles): The component styles that you can refer to by components within this document. See [Enhancing Your Articles with Styles](../AppleNews/enhancing-your-articles-with-styles.md).
- `documentStyle` (DocumentStyle): An object containing the background color of the article.
- `metadata` (Metadata): The article’s metadata, such as publication date, ad campaign data, and other information that isn’t part of the core article content.
- `subtitle` (string) *(deprecated)*: The article subtitle. Should be plain text; formatted text (HTML or Markdown) isn’t supported.
- `textFormat` (string): The global text format to apply to [`Text`](./text.md) components and [`FormattedText`](./formattedtext.md) objects.

  If you don’t specify the `textFormat` property, the `format` of `Text` components and `formattedText` objects defaults to `none`.

  If you specify the `textFormat` property, the `format` of `Text` components and `formattedText` objects defaults to the value of this property.

  To override the `textFormat` value, use the `format` property in the `Text` component or the `formattedText` object.

  **Allowed Values**: `markdown`, `html`, `none`
- `textStyles` (ArticleDocument.textStyles): The `TextStyle` objects available to use inline for text in `Text` components. See [Using HTML with Apple News Format](../AppleNews/using-html-with-apple-news-format.md), [Using Markdown with Apple News Format](../AppleNews/using-markdown-with-apple-news-format.md), and [`InlineTextStyle`](./inlinetextstyle.md).

## See Also

### Essentials
- [JSON Concepts and Article Structure](../AppleNews/json-concepts-and-article-structure.md)
  Understand basic JSON concepts and become familiar with the structure of an Apple News Format article.
- [Creating an Article: Main Steps](../AppleNews/creating-an-article-main-steps.md)
  Plan the design for your article and create it in Apple News Format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/articledocument)*