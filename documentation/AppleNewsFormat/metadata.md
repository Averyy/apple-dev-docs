# Metadata

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

Information about your article, including author name, creation date, publication date, keywords, and excerpt.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Metadata
```

## Mentions

- [Changing the Appearance of Your Article Tile in Feeds](../AppleNews/changing-the-appearance-of-your-article-tile-in-feeds.md)
- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)
- [Creating an Article: Main Steps](../AppleNews/creating-an-article-main-steps.md)
- [Apple News Format Release Notes](../AppleNews/apple-news-format-release-notes.md)
- [Apple News API Release Notes](../AppleNews/apple-news-api-release-notes.md)

## Discussion

For best results, include as many properties as you can even though they aren’t required.

### Example

```json
{
  "metadata": {
    "excerpt": "This is a sample sports article.",
    "thumbnailURL": "bundle://Football.jpg",
    "datePublished": "2018-09-09T14:45:45+00:00",
    "dateCreated": "2018-09-08T12:41:00+00:00",
    "dateModified": "2018-09-10T12:41:00+00:00",
    "authors": [
      "Anne Johnson"
    ],
    "campaignData": {
      "sport": [
        "football"
      ],
      "event": [
        "Football"
      ]
    },
    "generatorName": "Generator",
    "generatorVersion": "1.0",
    "canonicalURL": "https://example.com/articles/2015/original-article.html",
    "links": [
      {
        "URL": "https://apple.news/AT6kNQslCQy6EE4bF8hpOoQ",
        "relationship": "related"
      }
    ]
  }
}
```

## Topics

### Object
- [object Metadata.campaignData](./metadata/campaigndata-data.dictionary.md)
  Custom key-value pairs you can use in advertisement campaigns.

## Properties

- `authors` ([string]): The authors of this article. The value may or may not be the same string provided in the [`Author`](./author.md) or [`Byline`](./byline.md) component.

  Note the following:

  - Include an author name or an array of author names formatted in title case. For example, Maria Ruiz.
  - Provide author names for your articles instead of team names. Only provide a team name, such as `News` `Staff`, for special cases.
  - Don’t include a website link, email ID, or Twitter handles, or use additional words such as *By*, *and*, *As told to*, or *Illustrated by*.

  Note that the `byline` or `author` component in the article body don’t have these same requirements.

  This value appears in the article tile in channel feeds and section feeds.
- `campaignData` (Metadata.campaignData): A set of key-value pairs, where the value is an array of at least one item that you can leverage to target your advertising campaigns to specific articles or groups of articles. See [Set up targeting](https://support.apple.com/guide/adguide/set-up-targeting-apd8725b40b2/1.0/icloud/1.0) in the [Advertising Guide for News Publishers](https://developer.apple.com/library/content/documentation/General/Conceptual/News_Advertising/index.html#//apple_ref/doc/uid/TP40016664-CH1-SW1).
- `canonicalURL` (uri): The canonical URL of a web version of this article. If this Apple  News Format document corresponds to a web version of this article, set this property to the URL of the web article. You can use this property to point to one version of the article as well as to redirect devices that don’t support News content.

  If you omit `canonicalURL`, devices that don’t support News can’t display the article.
- `contentGenerationType` (string): An optional string value that indicates the content creation source for the article.

  Valid values:

  - `AI`. The content of the article is AI-generated. See [AI-generated content in Apple News](https://support.apple.com/guide/news-publisher/ai-generated-content-apd8da39c6f2/1.0/icloud/1.0).
  - `syndicated`. The content of the article is produced by a syndication or wire service. See [Syndicated content in Apple News](https://support.apple.com/guide/news-publisher/syndicated-content-in-apple-news-apd647c8345e/icloud).

  **Allowed Values**: `AI`, `syndicated`
- `dateCreated` (date-time): The UTC date in ISO 8601 format (`YYYY-MM-DDTHH:mm:ss±ZZ:ZZ`) on which this article was created. This value may or may not be the same as `datePublished`.
- `dateModified` (date-time): The UTC date in ISO 8601 format (`YYYY-MM-DDTHH:mm:ss±ZZ:ZZ`) on which this article was last modified after it was published.

  Apple News Format uses this date instead of `datePublished` in the article tile if it’s later than `datePublished` by less than 48 hours. `dateModified` doesn’t affect the feed order. See [Changing the Appearance of Your Article Tile in Feeds](../AppleNews/changing-the-appearance-of-your-article-tile-in-feeds.md).
- `datePublished` (date-time): The UTC date in ISO 8601 format (`YYYY-MM-DDTHH:mm:ss±ZZ:ZZ`) on which this article was first published. Apple News Format uses this date in the feed. Include this date when posting older content to make sure the articles don’t appear at the top of your feed.
- `excerpt` (string): A summary of your article. It can also be a subheadline or a quote.  Keep your excerpt within the recommended 80–300 character range.

  This text may appear in the article tile in feeds. It can also appear when someone shares an article.

  See [Changing the Appearance of Your Article Tile in Feeds](../AppleNews/changing-the-appearance-of-your-article-tile-in-feeds.md).

  Don’t use HTML tags or Markdown syntax for this property.

  Although this property is optional, it’s best to define it in all of your Apple News Format documents.
- `generatorIdentifier` (string): A unique identifier for the generator you use to create or provide this JSON document.
- `generatorName` (string): The name of the generator or system that you use to create the JSON document.
- `generatorVersion` (string): The version “number,” as a string, of the generator you use to create the JSON document.
- `issue` (Issue): The object for defining information about an issue.
- `keywords` ([string]): The keywords that describe this article. You can define up to 50 keywords.
- `links` ([LinkedArticle]): An array of links to other articles in Apple News.
- `thumbnailURL` (string): The URL of an image that can represent this article in a News feed view, such as the Today feed, channel feeds, and topic feeds. For best results, provide a high-resolution image. Apple News automatically scales the image down to the correct size.

  Supported image types are JPEG, (`.jpeg` or `.jpg`) WebP, GIF, or PNG.

  Apple News converts WebP and GIF images you provide as `thumbnailURL` to JPEG for use as an article thumbnail. Note that the system removes animations from WebP and GIF images.

  The minimum size of the image must be 300 px wide x 300 px high.

  The aspect ratio (width ÷ height) must be between 0.5 and 3.0.

  To improve the loading time of the article, use one of the images in the article as the thumbnail image. If you use the same images in both places and the image appears on the first screen of the article, the image moves with an animated effect from the feed to the article. See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).
- `videoURL` (uri): The URL for the video that represents this article. A glyph appears on the thumbnail of the article tile, allowing the video to be playable from feeds, such as the Today feed, channel feeds, and topic feeds.

  Use the same URL for the  `videoURL` that you use for one of the [`Video`](./video.md) components in the article. For the best results or continuous playback for an opened article with a `videoURL`, make sure that the `thumbnailURL` property in metadata uses the same image file as the video component’s `stillURL`.

  Video URL must begin with `http://` or preferably `https://`. The video must be in one of the supported HTTP Live Streaming (HLS) formats. Streaming using the M3U playlist format is highly recommended. See [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md).

  For more information about HLS, see [HTTP Live Streaming](https://developer.apple.com/streaming/).

## See Also

### Article Metadata
- [object LinkedArticle](./linkedarticle.md)
  A relationship between your article and another Apple News article.
- [object Issue](./issue.md)
  The object for defining information about an issue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/metadata)*