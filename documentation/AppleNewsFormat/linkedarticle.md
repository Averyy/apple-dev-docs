# LinkedArticle

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

A relationship between your article and another Apple News article.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object LinkedArticle
```

## Mentions

- [Creating an Article: Main Steps](../AppleNews/creating-an-article-main-steps.md)

## Discussion

You can control lists of links that people see in articles by using the `links` array in [`Metadata`](./metadata.md). If you are linking to a sponsored article, ensure that the [`Create an Article`](../AppleNewsAPI/post-channels-_channelid_-articles.md) request uses the `isSponsored` flag.

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
      ],
      "author": [
        "John Appleseed"
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

## Properties

- `relationship` (string) *(required)*: The type of relationship between the article and the linked document.

  Valid values:

  - `related`. The linked article is an article on the same topic, part of the same dossier, or provides more information about the subjects discussed.
  - `promoted`. The linked article isn’t directly related, but deserves additional promotion because the article covers another important topic. This value also puts the article at the top of the channel feed.

  **Allowed Values**: `related`, `promoted`
- `URL` (uri) *(required)*: The URL for the link, which can be either an Apple News link, like `https://apple.news/[article_id]`, or a link to an article on your website, if the website link matches the `canonicalURL` metadata property of the linked article. For more information about `canonicalURL`, see [`Metadata`](./metadata.md).

## See Also

### Article Metadata
- [object Metadata](./metadata.md)
  Information about your article, including author name, creation date, publication date, keywords, and excerpt.
- [object Issue](./issue.md)
  The object for defining information about an issue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/linkedarticle)*