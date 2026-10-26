# Changing the Appearance of Your Article Tile in Feeds

**Framework**: Apple News  
**Role**: Article

Change the information that News displays about your published article.

#### Overview

Every article you publish has an article tile that provides information about the article. The article tile appears in feeds, such as the Today feed, channel feeds, and topic feeds.

Your article tile can incorporate information from your [`ArticleDocument`](https://developer.apple.com/documentation/applenewsformat/articledocument) properties, your article [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata), your [`Create an Article`](https://developer.apple.com/documentation/applenewsapi/post-channels-_channelid_-articles) request, and your channel name.

![A labeled screenshot of an article with a thumbnail image on the left. On the right is a title, followed by an excerpt, published date, and authors.](https://developer.apple.com/tutorials/images/com.apple.applenews/media-4099657@2x.png)

To change the different parts of your article tile, modify the following properties:

- `thumbnailURL`, `videoURL`. Use the `thumbnailURL` property in the article’s [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object to specify the image you want to use in the article tile. Optionally specify the `videoURL` property. When you provide both `thumbnailURL` and `videoURL`, Apple News displays the `videoURL` in the article tile. See [Preparing Image, Video, Audio, Music, and ARKit Assets](./preparing-image-video-audio-music-and-arkit-assets.md).
- `title`. Use the `title` property in the  [`ArticleDocument`](https://developer.apple.com/documentation/applenewsformat/articledocument) object to specify the article’s title.
- `datePublished,dateModified`. Use the `datePublished` or `dateModified` property in the article’s [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object to specify the date the article was published or most recently modified (after publication).
- `authors`. Use the `authors` property in the article’s [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object to specify the author of the article. This text appears below the headline in your article tile.
- `excerpt`. Use the `excerpt` property in the article’s [`Metadata`](https://developer.apple.com/documentation/applenewsformat/metadata) object to specify the summary or the subheadline. Although it’s optional, try to include an excerpt for all of your articles and keep within the recommended 80–300 character range. This text may appear in the article tile in feeds or when an article is shared. Don’t use HTML tags or Markdown syntax for this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/changing-the-appearance-of-your-article-tile-in-feeds)*