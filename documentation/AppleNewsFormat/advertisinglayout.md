# AdvertisingLayout

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the margin above and below advertising components.

**Availability**:
- Apple News Format 1.7+ - Deprecated in 1.7

> **Deprecated**: Use [`AutoPlacementLayout`](./autoplacementlayout.md) instead.

## Declaration

```
object AdvertisingLayout
```

## Discussion

Define the margins for the [`BannerAdvertisement`](./banneradvertisement.md) components that are inserted automatically. This object is different from the [`ComponentLayout`](./componentlayout.md) object and supports only one property, `margin`.

This object can be used in [`AdvertisingSettings`](./advertisingsettings.md).

### Example

```json
{
  "advertisingSettings": {
    "frequency": 10,
    "layout": {
      "margin": {
        "top": 15,
        "bottom": 20
      }
    }
  }
}
```

## Properties

- `margin` ((Margin | integer)) *(required)* *(deprecated)*: Describes margins on top and bottom as a single integer or as an object containing separate properties for top and bottom margins.

  Version 1.1

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
- [object AutoPlacementLayout](./autoplacementlayout.md)
  The object for defining the margin above and below advertising components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/advertisinglayout)*