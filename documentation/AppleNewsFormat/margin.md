# Margin

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the space above and below a component.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Margin
```

## Mentions

- [Positioning the Content in Your Article](../AppleNews/positioning-the-content-in-your-article.md)

## Discussion

Use the `margin` object to specify top and bottom margins to designate space above and below a component. For information on the units, see [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

You can use this object in [`ComponentLayout`](./componentlayout.md) and [`AutoPlacementLayout`](./autoplacementlayout.md).

### Example

```json
{
  "components": [
    {
      "role": "header",
      "layout": "headerLayout",
      "components": [
        {
          "role": "title",
          "text": "Article Title"
        }
      ]
    }
  ],
  "componentLayouts": {
    "headerLayout": {
      "margin": {
        "top": 50,
        "bottom": 50
      }
    }
  }
}
```

## Properties

- `bottom` ((SupportedUnits | number)): The bottom margin in `points`, or with any of the units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `top` ((SupportedUnits | number)): The top margin in `points`, or with any of the units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`

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
- [object AutoPlacementLayout](./autoplacementlayout.md)
  The object for defining the margin above and below advertising components.
- [object AdvertisingLayout](./advertisinglayout.md)
  The object for defining the margin above and below advertising components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/margin)*