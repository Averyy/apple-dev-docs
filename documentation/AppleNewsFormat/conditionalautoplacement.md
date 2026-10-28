# ConditionalAutoPlacement

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining conditional properties for an automatically placed component, and when the conditional properties are in effect.

**Availability**:
- Apple News Format 1.9+ - Deprecated in 1.25

## Declaration

```
object ConditionalAutoPlacement
```

## Mentions

- [Apple News Format Release Notes](../AppleNews/apple-news-format-release-notes.md)

## Discussion

Use the `ConditionalAutoPlacement` object to define an array of conditional automatic placement properties and the conditions under which to apply them. When a condition is met, the value of a property in `ConditionalAutoPlacement` overrides the value of the same property if defined in the parent `AdvertisementAutoPlacement` object. See [`AdvertisementAutoPlacement`](./advertisementautoplacement.md).

### Example

```json
{
  "version": "1.9",
  "identifier": "SampleArticle",
  "language": "en",
  "title": "Apple News",
  "layout": {
    "columns": 7,
    "width": 1024,
    "margin": 75,
    "gutter": 20
  },
  "autoplacement": {
    "advertisement": {
      "enabled": true,
      "bannerType": "any",
      "distanceFromMedia": "50vh",
      "frequency": 10,
      "layout": {
        "margin": 10
      },
      "conditional": [
        {
          "enabled": false,
          "conditions": [
            {
              "verticalSizeClass": "compact"
            }
          ]
        }
      ]
    }
  },
  …
}
```

## Properties

- `conditions` ((Condition | [Condition])) *(required)* *(deprecated)*: An instance or array of conditions that, when met, cause the conditional automatic placement properties to take effect.

  **Allowed Types**: `Condition`, `[Condition]`
- `enabled` (boolean) *(deprecated)*: A Boolean that defines whether placement of advertisements is enabled.

  **Default**: `false`
- `layout` (AutoPlacementLayout) *(deprecated)*: A value that defines the layout properties for the automatically inserted components.

## See Also

### Conditional Design Elements
- [object Condition](./condition.md)
  The object for defining a condition that, when met, causes conditional properties to go into effect.
- [object ConditionalComponent](./conditionalcomponent.md)
  The object for defining conditional properties for a component, and when the conditional properties are in effect.
- [object ConditionalComponentLayout](./conditionalcomponentlayout.md)
  The object for defining conditional properties for a component layout, and when the conditional properties are in effect.
- [object ConditionalSection](./conditionalsection.md)
  The object for defining conditional properties for a section component, and when the conditional properties are in effect.
- [object ConditionalDocumentStyle](./conditionaldocumentstyle.md)
  The object for defining conditional properties for a document style, and when the conditional properties are in effect.
- [object ConditionalText](./conditionaltext.md)
  The object for defining conditional properties for a text component, and when the conditional properties are in effect.
- [object ConditionalTextStyle](./conditionaltextstyle.md)
  The object for defining conditional properties for a text style, and when the conditional properties are in effect.
- [object ConditionalComponentTextStyle](./conditionalcomponenttextstyle.md)
  The object for defining conditional properties for a component text style, and when the conditional properties are in effect.
- [object ConditionalComponentStyle](./conditionalcomponentstyle.md)
  The object for defining conditional properties for a component style, and when the conditional properties are in effect.
- [object ConditionalContainer](./conditionalcontainer.md)
  The object for defining conditional properties for a container component, and when the conditional properties are in effect.
- [object ConditionalDivider](./conditionaldivider.md)
  The object for defining conditional properties for a divider component, and when the conditional properties are in effect.
- [object ConditionalButton](./conditionalbutton.md)
  The object for defining a button component’s conditional properties, and when the conditional properties are in effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/conditionalautoplacement)*