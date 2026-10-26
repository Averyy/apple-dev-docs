# ConditionalComponent

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining conditional properties for a component, and when the conditional properties are in effect.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object ConditionalComponent
```

#### Discussion

Use the `ConditionalComponent` object to define an array of conditional component properties and the conditions under which to apply them. When a condition is met, the value of a property in `ConditionalComponent` overrides the value of the same property if you define it in the parent component. See [`Component`](./component.md).

##### Example

```json
{
  "components": [
    {
      "role": "title",
      "text": "Article Title",
      "style": "red-background",
      "textStyle": {
        "textAlignment": "center"
      },
      "layout": "short-header",
      "conditional": [
        {
          "style": "blue-background",
          "textStyle": {
            "textAlignment": "left"
          },
          "layout": "tall-header",
          "conditions": [
            {
              "minViewportWidth": 415
            }
          ]
        }
      ]
    }
  ],
  "componentStyles": {
    "red-background": {
      "backgroundColor": "red"
    },
    "blue-background": {
      "backgroundColor": "blue"
    }
  },
  "componentLayouts": {
    "short-header": {
      "minimumHeight": 100
    },
    "tall-header": {
      "minimumHeight": 200
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

  To remove a previously set condition, use `none`.

  **Allowed Types**: `Behavior`, `string("none")`
- `hidden` (boolean): A Boolean value that determines whether the component is hidden.

  **Default**: `false`
- `layout` ((ComponentLayout | string)): An inline `ComponentLayout` object that contains layout information, or a string reference to a `ComponentLayout` object that you define at the top level of the document.

  If you don’t define the layout, Apple News bases the size and position on various factors, such as the device type, the length of the content, and the `role` of this component.

  **Allowed Types**: `ComponentLayout`, `string`
- `style` ((ComponentStyle | string | string("none"))): An inline `ComponentStyle` object that defines the appearance of this component, or a string reference to a `ComponentStyle` object that you define at the top level of the document.

  To remove a previously set condition, use `none`.

  **Allowed Types**: `ComponentStyle`, `string`, `string("none")`

## Relationships

### Inherited By
- [ConditionalButton](./conditionalbutton.md)
- [ConditionalContainer](./conditionalcontainer.md)
- [ConditionalDivider](./conditionaldivider.md)
- [ConditionalText](./conditionaltext.md)

## See Also

### Conditional Design Elements
- [object Condition](./condition.md)
  The object for defining a condition that, when met, causes conditional properties to go into effect.
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
- [object ConditionalButton](./conditionalbutton.md)
  The object for defining a button component’s conditional properties, and when the conditional properties are in effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/conditionalcomponent)*