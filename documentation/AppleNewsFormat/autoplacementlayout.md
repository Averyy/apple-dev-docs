# AutoPlacementLayout

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the margin above and below advertising components.

**Availability**:
- Apple News Format 1.9+ - Deprecated in 1.25

## Declaration

```
object AutoPlacementLayout
```

## Mentions

- [Apple News Format Release Notes](../AppleNews/apple-news-format-release-notes.md)

#### Discussion

Use the `AutoPlacementLayout` object to define the margins for ad components that are inserted automatically. This object is different from the [`ComponentLayout`](./componentlayout.md) object and supports only one property, `margin`.

This object can be used in [`AdvertisementAutoPlacement`](./advertisementautoplacement.md).

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

- `margin` ((Margin | integer)) *(deprecated)*: The top and bottom margin in points, or in any other unit of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `Margin`, `integer`

## See Also

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
- [object AdvertisingLayout](./advertisinglayout.md)
  The object for defining the margin above and below advertising components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/autoplacementlayout)*