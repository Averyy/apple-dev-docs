# ConditionalComponentLayout

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining conditional properties for a component layout, and when the conditional properties are in effect.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object ConditionalComponentLayout
```

## Discussion

Use the `ConditionalComponentLayout` object to define an array of conditional component layout properties and the conditions under which to apply them. When a condition is met, the value of a property in `ConditionalComponentLayout` overrides the value of the same property if defined in the parent `ComponentLayout` object. See [`ComponentLayout`](./componentlayout.md).

### Example

```json
{
  "components": [
    {
      "role": "photo",
      "URL": "bundle://summer.jpg",
      "layout": "exampleLayout",
      "caption": "Thanks to the record drought, mountain lions have begun to descend from the peaks."
    }
  ],
  "componentLayouts": {
    "exampleLayout": {
      "ignoreDocumentMargin": true,
      "conditional": [
        {
          "ignoreDocumentMargin": false,
          "conditions": [
            {
              "minViewportWidth": 415
            }
          ]
        }
      ]
    }
  }
}
```

## Properties

- `conditions` ((Condition | [Condition])) *(required)*: An instance or array of conditions that, when met, cause the conditional component layout properties to take effect.

  **Allowed Types**: `Condition`, `[Condition]`
- `columnSpan` (integer): A number that indicates how many columns the component spans, based on the number of columns in the document. Note that for the `columnSpan` value to take effect, you need to specify `columnStart`.

  By default, the component spans the entire width of the document or the width of its container component.

  **Minimum**: `1`
- `columnStart` (integer): A number that indicates which column the component’s start position is in, based on the number of columns in the document or parent container. Note that for the `columnStart` value to take effect, you need to specify `columnSpan`.

  By default, the component starts in the first column (note that the first column is `0`, not `1`).

  **Minimum**: `0`
- `horizontalContentAlignment` (string): The alignment of the content within the component. This property applies only when the width of the content is less than the width of the component.

  The [`Image`](./image.md), [`Logo`](./logo.md), and [`Divider`](./divider.md) components support this property. All other components ignore this property.

  **Default**: `center`; **Allowed Values**: `left`, `center`, `right`
- `ignoreDocumentGutter` ((boolean | string("none" | "left" | "right" | "both"))): A value that indicates whether Apple News ignores the gutters (if any) to the left and right of the component. The gutter size is defined in the `Layout` object at the root level of the document.

  Use this option to position two components next to each other without a gutter between them. This property applies only when a gutter actually exists to the left or right of the component. The first column doesn’t have a left gutter, and the last column doesn’t have a right gutter.

  Valid values:

  - `none` (default). The component doesn’t ignore the gutters.
  - `left`. The component ignores the left gutter.
  - `right`. The component ignores the right gutter.
  - `both`. The component ignores gutters, if any, on both sides.

  You can also set this property to `true` to indicate that you want to ignore `both` gutters, or set it to `false` to ignore none of the gutters. By default, the component doesn’t ignore `none` of the gutters.

  **Allowed Types**: `boolean`, `string("none" | "left" | "right" | "both")`
- `ignoreDocumentMargin` ((boolean | string("none" | "left" | "right" | "both"))): A value that indicates whether the parent container respects or ignores a document’s margins. Ignoring document margins positions the component at the edge of the display. This property affects the layout only if the component is in the first or last column.

  Valid values:

  - `none` (default). The parent container ignores the margins.
  - `left`. The parent container ignores the left margin.
  - `right`. The parent container ignores the right margin.
  - `both`. The parent container ignores margins on both sides (if any).

  Instead of specifying margins, you can set this property to `true` to indicate that the parent container ignores both margins, or set it to `false` to ignore none of the gutters. By default, the parent container doesn’t ignore any of the document margins.

  **Allowed Types**: `boolean`, `string("none" | "left" | "right" | "both")`
- `margin` ((Margin | integer)): The margins for the top and bottom of the component, as a single integer that is applied to the top and bottom margins, or as an object containing separate properties for top and bottom.

  **Allowed Types**: `Margin`, `integer`
- `maximumContentWidth` ((SupportedUnits | number)): The maximum width of the content within the component. Specify this value as a number in points, or use one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  This property is supported for [`Image`](./image.md), [`Logo`](./logo.md), and [`Divider`](./divider.md)  components. All other components ignore this property.

  **Allowed Types**: `SupportedUnits`, `number`
- `maximumWidth` ((SupportedUnits | number)): The maximum width of the layout when you use it within a [`Container`](./container.md) with [`HorizontalStackDisplay`](./horizontalstackdisplay.md) as the specified `contentDisplay` type.

  **Allowed Types**: `SupportedUnits`, `number`
- `minimumHeight` ((SupportedUnits | number)): The minimum height of the component. A component is taller than its defined `minimumHeight` when the contents require it. Specify this value as a number in points, or use one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `minimumWidth` ((SupportedUnits | number)): The minimum width of the layout when you use it within a container with [`HorizontalStackDisplay`](./horizontalstackdisplay.md) as the specified `contentDisplay` type.

  **Allowed Types**: `SupportedUnits`, `number`
- `padding` ((SupportedUnits | Padding | number)): The padding between the content of the component and the edges of the component.

  **Allowed Types**: `SupportedUnits`, `Padding`, `number`
- `ignoreViewportPadding` ((boolean | string("none" | "left" | "right" | "both"))): A value that indicates whether the component respects or ignores the viewport padding. Ignoring viewport padding positions the component at the edge of the display screen. This property affects the layout only if the component is in the first or last column.

  Valid values:

  - `none` (default). The component doesn’t ignore the padding.
  - `left`. The component ignores the left padding.
  - `right`. The component ignores the right padding.
  - `both`. The component ignores the padding, if any, on both sides.

  Instead of specifying padding, you can set this property to `true` to indicate the component ignores the padding on both sides, or set it to `false` to ignore neither padding. By default, it doesn’t ignore either padding.

  The layout of a parent component always constrains any child components. Setting `ignoreViewportPadding` to `true` for a component has no effect if it’s inside of a container with `ignoreViewportPadding` set to `false`.

  If you set `ignoreViewportPadding` to `true`, `left`, `right`, or `both,` it overrides the layout’s `ignoreDocumentMargin` value and spans the entire screen.

  If you set `ignoreViewportPadding` to `none`, the component accepts the value of `ignoreDocumentMargin`.

  By default, components don’t ignore the viewport padding, even if you previously specified `ignoreDocumentMargin` to span the entire width of the screen. To achieve the same functionality, you must update your article to use `ignoreViewportPadding`.

  **Allowed Types**: `boolean`, `string("none" | "left" | "right" | "both")`

## Relationships

### Inherits From
- [ComponentLayout](./componentlayout.md)

## See Also

### Conditional Design Elements
- [object Condition](./condition.md)
  The object for defining a condition that, when met, causes conditional properties to go into effect.
- [object ConditionalComponent](./conditionalcomponent.md)
  The object for defining conditional properties for a component, and when the conditional properties are in effect.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/conditionalcomponentlayout)*