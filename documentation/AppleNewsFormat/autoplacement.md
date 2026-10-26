# AutoPlacement

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for automatically placing components within Apple News Format articles.

**Availability**:
- Apple News Format 1.9+ - Deprecated in 1.25

## Declaration

```
object AutoPlacement
```

## Mentions

- [Apple News Format Release Notes](../AppleNews/apple-news-format-release-notes.md)

#### Discussion

Use the `AutoPlacement` object to define the metadata, appearance, and placement of advertising components within Apple News Format articles.

##### Example

```json
{
  "version": "1.9",
  "identifier": "SampleArticle",
  "language": "en",
  "title": "Apple News",
  "layout": {
    "columns": 20,
    "width": 1024,
    "margin": 60,
    "gutter": 20
  },
  "autoplacement": {
    "advertisement": {
      "enabled": true,
      "bannerType": "any",
      "distanceFromMedia": "10vh",
      "frequency": 10,
      "layout": {
        "margin": 10
      }
    }
  },
  …
}
```

## Properties

- `advertisement` (AdvertisementAutoPlacement) *(deprecated)*: The automatic placement of advertisement components. By default, no advertising is automatically inserted.

## Relationships

### Inherited By
- [AdvertisementAutoPlacement](./advertisementautoplacement.md)

## See Also

### Dynamic Advertising
- [Managing Advertisements in Your Channel](../AppleNews/managing-advertisements-in-your-channel.md)
  Set the layout and frequency of ads automatically inserted in an article.
- [object AdvertisementAutoPlacement](./advertisementautoplacement.md)
  The object for defining the automatic placement of advertisements.
- [object AdvertisingSettings](./advertisingsettings.md)
  The object for defining properties that affect the frequency and placement with which banner advertisements and medium rectangle advertisements are automatically placed in your article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/autoplacement)*