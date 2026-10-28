# ConditionalButton

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining a button component’s conditional properties, and when the conditional properties are in effect.

**Availability**:
- Apple News Format 1.11+

## Declaration

```
object ConditionalButton
```

## Discussion

Use the `ConditionalButton` object to define an array of conditional button properties and the conditions under which to apply them. When a condition is met, the value of a property in `ConditionalButton` overrides the value of the same property if you define it in the parent button component. See [`LinkButton`](./linkbutton.md).

### Example

```json
{
  "components": [
    {
      "role": "link_button",
      "URL": "http://apple.com",
      "text": "Read More",
      "style": {
        "backgroundColor": "#DDD",
        "mask": {
          "type": "corners",
          "radius": 25
        }
      },
      "layout": {
        "padding": 10
      },
      "conditional": [
        {
          "style": "dark-mode-background",
          "textStyle": "dark-mode-text-style",
          "conditions": [
            {
              "preferredColorScheme": "dark"
            }
          ]
        },
        {
          "style": "light-mode-background",
          "textStyle": "light-mode-text-style",
          "conditions": [
            {
              "preferredColorScheme": "light"
            }
          ]
        }
      ]
    }
  ],
  "componentStyles": {
    "dark-mode-background": {
      "backgroundColor": "#5e5e5e",
      "mask": {
        "type": "corners",
        "radius": 25
      }
    },
    "light-mode-background": {
      "backgroundColor": "#DDD",
      "mask": {
        "type": "corners",
        "radius": 25
      }
    }
  },
  "componentTextStyles": {
    "dark-mode-text-style": {
      "textColor": "#FFF"
    },
    "light-mode-text-style": {
      "textColor": "#000"
    }
  }
}
```

## Properties

- `conditions` ((Condition | [Condition])) *(required)*: An instance or array of conditions that, when met, cause the conditional component properties to take effect.

  **Allowed Types**: `Condition`, `[Condition]`
- `anchor` (Anchor): An object that defines vertical alignment with another component.
- `animation` ((ComponentAnimation | string("none"))): An object that defines an animation to apply to the component.

  To remove a previously set condition, use `none`.

  **Allowed Types**: `ComponentAnimation`, `string("none")`
- `behavior` ((Behavior | string("none"))): An object that defines behavior for a component, like [`Parallax`](./parallax.md) or [`Springy`](./springy.md).

  **Allowed Types**: `Behavior`, `string("none")`
- `hidden` (boolean): A Boolean value that determines whether Apple News hides the component.

  **Default**: `false`
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define layout, Apple News bases the size and position on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`
- `textStyle` ((ComponentTextStyle | string)): An inline `ComponentTextStyle` object that contains styling information, or a string reference to a `ComponentTextStyle` object that you define at the top level of the document.

  **Allowed Types**: `ComponentTextStyle`, `string`

## Relationships

### Inherits From
- [ConditionalComponent](./conditionalcomponent.md)

## See Also

### Conditional Design Elements
- [object Condition](./condition.md)
  The object for defining a condition that, when met, causes conditional properties to go into effect.
- [object ConditionalComponent](./conditionalcomponent.md)
  The object for defining conditional properties for a component, and when the conditional properties are in effect.
- [object ConditionalComponentLayout](./conditionalcomponentlayout.md)
  The object for defining conditional properties for a component layout, and when the conditional properties are in effect.
- [object ConditionalAutoPlacement](./conditionalautoplacement.md)
  The object for defining conditional properties for an automatically placed component, and when the conditional properties are in effect.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/conditionalbutton)*