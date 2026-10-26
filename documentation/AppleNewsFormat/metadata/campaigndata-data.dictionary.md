# Metadata.campaignData

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

Custom key-value pairs you can use in advertisement campaigns.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Metadata.campaignData
```

#### Discussion

`Metadata.campaignData` is an object that contains custom key-value pairs, where the `key` is a string and the value is an array.

##### Example

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
      "ads": [
        "disableAds"
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

- `Any Key` ([*]): An array of custom strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/metadata/campaigndata-data.dictionary)*