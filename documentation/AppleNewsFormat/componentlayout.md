# ComponentLayout

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining the positioning for a specific component within the article’s column system.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ComponentLayout
```

## Mentions

- [Positioning the Content in Your Article](../AppleNews/positioning-the-content-in-your-article.md)
- [Creating an Article: Main Steps](../AppleNews/creating-an-article-main-steps.md)
- [Displaying Components Side By Side](../AppleNews/displaying-components-side-by-side.md)

## Discussion

Use the `ComponentLayout` object to define a position for a specific component within the column system defined using the [`Layout`](./layout.md) object.

For information on setting the units for the width and height, see [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md). For information on aligning components, see [`Anchor`](./anchor.md).

> **Note**:  If two components refer to the same `ComponentLayout` object, but they exist in containers of different column spans, both components adopt the width of the narrower component. This occurs even if the referenced `ComponentLayout` doesn’t explicitly declare `columnStart` or `columnSpan`. In this situation, use separate layouts for the child components.

You can use this object in [`ArticleDocument`](./articledocument.md).

### Example

```json
{
  "components": [
    {
      "role": "heading1",
      "layout": "heading1Layout",
      "text": "Heading Text"
    },
    {
      "role": "body",
      "text": "Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life."
    }
  ],
  "componentLayouts": {
    "heading1Layout": {
      "columnStart": 0,
      "columnSpan": 7,
      "margin": {
        "top": 24,
        "bottom": 10
      }
    }
  }
}
```

## Properties

- `columnSpan` (integer): A number that indicates how many columns the component spans, based on the number of columns in the document.

  By default, the component spans the entire width of the document or the width of its container component.

  **Minimum**: `1`
- `columnStart` (integer): A number that indicates which column the component’s start position is in, based on the number of columns in the document or parent container.

  By default, the component starts in the first column (note that the first column is 0, not 1).

  **Minimum**: `0`
- `conditional` ((ConditionalComponentLayout | [ConditionalComponentLayout])): An instance or array of component layout properties that you can apply conditionally, and the conditions that cause Apple News Format to apply them.

  **Allowed Types**: `ConditionalComponentLayout`, `[ConditionalComponentLayout]`
- `horizontalContentAlignment` (string): A string value that sets the alignment of the content within the component. This property applies only when the width of the content is less than the width of the component.

  Apple News supports this property for [`LinkButton`](./linkbutton.md), [`Image`](./image.md), [`Logo`](./logo.md), [`Divider`](./divider.md), and [`MediumRectangleAdvertisement`](./mediumrectangleadvertisement.md). All other components ignore this property.

  **Default**: `center`; **Allowed Values**: `left`, `center`, `right`
- `ignoreDocumentGutter` ((boolean | string("none" | "left" | "right" | "both"))): A value that indicates whether Apple News ignores the gutters (if any) to the left and right of the component. The gutter size is defined in the `Layout` object at the root level of the document.

  Use this option if you want to position two components right next to each other without a gutter between them. This property applies only when a gutter actually exists to the left or right of the component. The first column doesn’t have a left gutter, and the last column doesn’t have a right gutter.

  Valid values:

  - `none` (default). The component doesn’t ignore any gutters.
  - `left`. The component ignores the gutter on the left.
  - `right`. The component ignores the gutter on the right.
  - `both`. The component ignores gutters, if any, on both sides.

  You can also set this property to `true` to indicate that the component ignores both gutters, or set it to `false` to ignore none of the gutters. By default, none of the gutters are ignored.

  **Allowed Types**: `boolean`, `string("none" | "left" | "right" | "both")`
- `ignoreDocumentMargin` ((boolean | string("none" | "left" | "right" | "both"))): A value that indicates whether the component applies or ignores the document’s margins. Ignoring document margins positions the component based on the document’s width and margin.

  Valid values:

  - `none` (default). The component doesn’t ignore the margins.
  - `left`. The component ignores the left margin.
  - `right`. The component ignores the right margin.
  - `both`. The component ignores margins, if any, on both sides.

  Instead of specifying margins, you can set this property to `true` so the component ignores both margins, or set it to `false` so the component ignores neither margin. By default, neither margin is  ignored.

  The layout of a parent component always constrains any child components. As such, setting `ignoreDocumentMargin` to `true` for a component has no effect if it’s inside of a container with `ignoreDocumentMargin` set to `false`.

  Specifying a value other than `none` for `ignoreViewportPadding` takes precedence over any value defined for `ignoreDocumentMargin`.

  On device with a screen size wider than the document `width` and `margin` combined, a component with `ignoreDocumentMargin` property set to `true` extends the width of the document plus the margin, but doesn’t extend into the viewport padding.

  **Allowed Types**: `boolean`, `string("none" | "left" | "right" | "both")`
- `ignoreViewportPadding` ((boolean | string("none" | "left" | "right" | "both"))): A value that indicates whether the component applies or ignores the viewport padding. Ignoring viewport padding positions the component at the edge of the display screen. This property affects the layout only if the component is in the first or last column.

  Valid values:

  - `none` (default). The component doesn’t ignore the padding.
  - `left`. The component ignores left padding.
  - `right`. The component ignores right padding.
  - `both`. The component ignores padding, if any, on both sides.

  Instead of specifying the padding, you can also set this property to `true` so the component ignores paddings on both sides, or set it to `false` so the component ignores neither padding. By default, neither padding is ignored.

  The layout of a parent component always constrains any child components. Setting `ignoreViewportPadding` to `true` for a component has no effect if it’s inside of a container with `ignoreViewportPadding` set to `false`.

  If `ignoreViewportPadding` is set to `true`, `left`, `right`, or `both`, it overrides the layout’s `ignoreDocumentMargin` value and spans the entire screen.

  If `ignoreViewportPadding` is set to `none`, Apple News Format accepts the value of `ignoreDocumentMargin`.

  By default, components don’t ignore the viewport padding, even if you previously specified `ignoreDocumentMargin` to span the entire width of the screen. To achieve the same functionality, you must update your article to use `ignoreViewportPadding`.

  **Allowed Types**: `boolean`, `string("none" | "left" | "right" | "both")`
- `margin` ((Margin | integer)): A value that sets the margins for the top and bottom of the component as a single integer that Apple News applies to the top and bottom margins, or as an object containing separate properties for top and bottom.

  **Allowed Types**: `Margin`, `integer`
- `maximumContentWidth` ((SupportedUnits | number)): A value that sets the maximum width of the content within the component. Specify this value as a number in points or using one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  Apple News supports this property for [`LinkButton`](./linkbutton.md), [`Image`](./image.md), [`Logo`](./logo.md), [`Divider`](./divider.md), and [`MediumRectangleAdvertisement`](./mediumrectangleadvertisement.md). All other components ignore this property.

  **Allowed Types**: `SupportedUnits`, `number`
- `minimumHeight` ((SupportedUnits | number)): A value that sets the minimum height of the component. A component is taller than its defined `minimumHeight` when the contents require the component to be taller. You can define the minimum height as a number in points or using one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `minimumWidth` ((SupportedUnits | number)): A value that defines the minimum width of the layout when you use it within a [`Container`](./container.md) with [`HorizontalStackDisplay`](./horizontalstackdisplay.md) as the specified `contentDisplay` type. You can define the minimum width as a number in points or using one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `maximumWidth` ((SupportedUnits | number)): A value that defines the maximum width of the layout when you use it within a [`Container`](./container.md) with [`HorizontalStackDisplay`](./horizontalstackdisplay.md) as the specified `contentDisplay` type. You can define the maximum width as a number in points or using one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `number`
- `padding` ((SupportedUnits | Padding | number)): A value that defines the padding between the content of the component and the edges of the component. You can define padding as a number in points or using one of the available units of measure for components. See [Specifying Measurements for Components](../AppleNews/specifying-measurements-for-components.md).

  **Allowed Types**: `SupportedUnits`, `Padding`, `number`

## Relationships

### Inherited By
- [ConditionalComponentLayout](./conditionalcomponentlayout.md)

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
- [object Anchor](./anchor.md)
  The object for anchoring one component to another component in your article’s layout.
- [object Margin](./margin.md)
  The object for defining the space above and below a component.
- [object AutoPlacementLayout](./autoplacementlayout.md)
  The object for defining the margin above and below advertising components.
- [object AdvertisingLayout](./advertisinglayout.md)
  The object for defining the margin above and below advertising components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/componentlayout)*