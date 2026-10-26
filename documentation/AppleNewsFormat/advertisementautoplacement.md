# AdvertisementAutoPlacement

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the automatic placement of advertisements.

**Availability**:
- Apple News Format 1.9+ - Deprecated in 1.25

## Declaration

```
object AdvertisementAutoPlacement
```

## Mentions

- [Apple News Format Release Notes](../AppleNews/apple-news-format-release-notes.md)

#### Discussion

Use the `AdvertisementAutoPlacement` object to insert dynamic advertisements between [`Body`](./body.md), [`Chapter`](./chapter.md), [`Section`](../AppleNewsAPI/section.md), or [`Container`](./container.md) components in an article.

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

- `bannerType` (string) *(deprecated)*: A specific banner type that should be automatically inserted based on the `frequency` value. If advertisement placement is enabled, only banners of the defined size type are inserted.

  **Default**: `any`; **Allowed Values**: `any`, `standard`, `double_height`, `large`
- `conditional` ((ConditionalAutoPlacement | [ConditionalAutoPlacement])) *(deprecated)*: An instance or array of automatic placement properties that can be applied conditionally, and the conditions that cause them to take effect.

  **Allowed Types**: `ConditionalAutoPlacement`, `[ConditionalAutoPlacement]`
- `distanceFromMedia` ((SupportedUnits | number)) *(deprecated)*: The minimum required distance between automatically inserted advertisement components and media, such as [`Video`](./video.md) and [`Photo`](./photo.md). Advertisements will show next to media if `distanceFromMedia` is not specified. To maintain a minimum distance of half a screen height from your media content, use a value of around `10vh`. For more information, see [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Default**: `0`; **Allowed Types**: `SupportedUnits`, `number`
- `enabled` (boolean) *(deprecated)*: A Boolean that defines whether placement of advertisements is enabled.

  **Default**: `false`
- `frequency` (integer) *(deprecated)*: A number from `0` to `10`, defining the frequency for automatically inserting ads into articles.

  Setting this value to `1` automatically inserts a dynamic advertisement in the first possible location below the screen bounds.

  Setting this value to `2` inserts a dynamic advertisement in the first possible location below the screen bounds, and another between the first dynamic advertisement and the end of the article.

  Increasing the frequency value increases the frequency of dynamic advertisements below the first screen bounds.

  Setting this value to `0,` or omitting it, results in no advertisements.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `10`
- `layout` (AutoPlacementLayout) *(deprecated)*: The layout properties for automatically inserted components.

## Relationships

### Inherits From
- [AutoPlacement](./autoplacement.md)

## See Also

### Dynamic Advertising
- [Managing Advertisements in Your Channel](../AppleNews/managing-advertisements-in-your-channel.md)
  Set the layout and frequency of ads automatically inserted in an article.
- [object AutoPlacement](./autoplacement.md)
  The object for automatically placing components within Apple News Format articles.
- [object AdvertisingSettings](./advertisingsettings.md)
  The object for defining properties that affect the frequency and placement with which banner advertisements and medium rectangle advertisements are automatically placed in your article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/advertisementautoplacement)*