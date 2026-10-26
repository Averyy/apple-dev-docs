# Article

**Framework**: AppleNewsAPI  
**Kind**: dictionary  
**Role**: Object

See the fields the article endpoints returned.

**Availability**:
- Apple News API 1.0+

## Declaration

```
object Article
```

## Mentions

- [Publishing an Article](../AppleNews/publishing-an-article.md)

## Properties

- `accessoryText` (string) *(deprecated)*: Text that appears alongside article headlines — author name, channel name, subtitle, and so on.

  Maximum length: 100 characters.

  Default value: `metadata.authors` from the Apple News Format article.
- `createdAt` (date-time): The date and time the article was created.
- `document` (string): The content of the article, as an Apple News Format document.
- `id` (uuid): The unique identifier of the article.
- `isCandidateToBeFeatured` (boolean): A Boolean value that indicates whether this article should be considered for featuring in Apple News.

  Default value: `false`
- `isPreview` (boolean): A Boolean value that indicates whether this article should be public (live) or should be a preview that’s only visible to members of your channel. Set `isPreview` to `false` to publish the article immediately and make it visible to all News users.

  If your channel hasn’t been approved to publish articles in Apple News Format, setting `isPreview` to `false` results in an `ONLY_PREVIEW_ALLOWED` error.

  Default value: `true` if your channel hasn’t yet been approved to publish articles in Apple News Format; `false` if your channel has been approved.
- `isSponsored` (boolean): A Boolean value that indicates whether this article consists of sponsored content for promotional purposes. You must mark sponsored content as such; channels that don’t follow this policy may be suspended.

  When using `isSponsored`, if you don’t want the sponsored article to appear in your channel’s feed, set sections to `[]` (an empty array).

  Default value: `false`
- `links` (ArticleLinksResponse): The URL of the channel in which the article appears.
- `maturityRating` (string): A string value that indicates the viewing audience for the content. The types of audiences or ratings are `KIDS`, `MATURE`, and `GENERAL,` or `null` if unspecified. A `MATURE` rating indicates explicit content that’s only appropriate for a specific audience.

  Default value: `null`

  **Allowed Values**: `KIDS`, `MATURE`, `GENERAL`
- `modifiedAt` (date-time): The date and time this article was last modified.
- `revision` (string): The current revision token for the article.

  You must send the latest revision when issuing a request to [`Update an Article`](./post-articles-_articleid_.md).

  The value of this field must match the latest revision from an earlier Create, Read, or Update Article call. This field prevents multiple users from updating an article simultaneously, which results in data loss.

  Required: Yes
- `shareUrl` (string): The URL to the article within the News app.
- `state` (string): The current state of the article, which can be one of the following:

  - `PROCESSING`: The article has been published and is processing.
  - `LIVE`: The article has been published, has finished processing, and is visible in the News app.
  - `PROCESSING_UPDATE`: A previous version of the article is visible in the News app, and an update is currently in processing.
  - `TAKEN_DOWN`: The article was previously visible in the News app, but was taken down.
  - `FAILED_PROCESSING`: The article failed during processing and isn’t visible in the News app.
  - `FAILED_PROCESSING_UPDATE`: A previous version of the article is visible in the News app, but an update failed during processing.
  - `DUPLICATE`. The article is a duplicate of another article and isn’t visible in the News app.

  **Allowed Values**: `PROCESSING`, `LIVE`, `PROCESSING_UPDATE`, `TAKEN_DOWN`, `FAILED_PROCESSING`, `FAILED_PROCESSING_UPDATE`, `DUPLICATE`
- `title` (string): The title of the article, as specified in the Apple News Format document.
- `type` (string): The article.
- `warnings` ([Warning]): A list of warning messages indicating nonfatal problems with the article.

## Relationships

### Inherited By
- [ArticleResponse](./articleresponse.md)

## See Also

### Articles
- [Create an Article](./post-channels-_channelid_-articles.md)
  Publish an article to your channel.
- [Read Article Information](./get-articles-_articleid_.md)
  Retrieve information about an article, such as the revision number and maturity rating.
- [Search Articles in a Channel](./get-channels-_channelid_-articles.md)
  See a list of all articles in a channel that match the specified search criteria.
- [Search Articles in a Section](./get-sections-_sectionid_-articles.md)
  See a list of all articles in a section that match the specified search criteria.
- [Update an Article](./post-articles-_articleid_.md)
  Update an existing article in your channel.
- [Delete an Article](./delete-articles-_articleid_.md)
  Delete the specified article from your channel.
- [object Create Article Metadata Fields](./create-article-metadata-fields.md)
  See the optional metadata fields for the Create an Article Request.
- [object ArticleLinksRequest](./articlelinksrequest.md)
  See the required field for the Create an Article request.
- [object Update Article Metadata Fields](./update-article-metadata-fields.md)
  See the metadata fields for the Update an Article request.
- [object ArticleResponse](./articleresponse.md)
  See which objects make up the Create an Article, Read an Article, and Update an Article responses.
- [object ArticleLinksResponse](./articlelinksresponse.md)
  See the links the article endpoints returned.
- [object SearchResponse](./searchresponse.md)
  See the fields the search article endpoints returned.
- [object Meta](./meta.md)
  See the object that wraps the throttling information that’s returned for the Create an Article and Read an Article endpoints.
- [object Throttling](./throttling.md)
  See the object that wraps the throttling information that’s returned for the Create an Article and Update an Article endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsapi/article)*