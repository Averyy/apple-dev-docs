# Condition

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining a condition that, when met, causes conditional properties to go into effect.

**Availability**:
- Apple News Format 1.9+

## Declaration

```
object Condition
```

## Mentions

- [Apple News Format Release Notes](../AppleNews/apple-news-format-release-notes.md)
- [Giving the Article a Dark Color Scheme](../AppleNews/giving-the-article-a-dark-color-scheme.md)
- [Supporting Dark Mode for Your Article](../AppleNews/supporting-dark-mode-for-your-article.md)

## Discussion

Use the `Condition` object to define the condition under which the associated properties are applied.

You can use this object in [`ConditionalComponent`](./conditionalcomponent.md), [`ConditionalContainer`](./conditionalcontainer.md), [`ConditionalSection`](./conditionalsection.md), [`ConditionalText`](./conditionaltext.md), [`ConditionalComponentLayout`](./conditionalcomponentlayout.md), [`ConditionalComponentStyle`](./conditionalcomponentstyle.md), [`ConditionalComponentTextStyle`](./conditionalcomponenttextstyle.md), [`ConditionalTextStyle`](./conditionaltextstyle.md), [`ConditionalDocumentStyle`](./conditionaldocumentstyle.md), [`ConditionalDivider`](./conditionaldivider.md), and [`ConditionalAutoPlacement`](./conditionalautoplacement.md).

### Example

```json
{
  "components": [
    {
      "role": "photo",
      "URL": "bundle://summer.jpg",
      "layout": "exampleLayout",
      "caption": "Thanks to the record drought, mountain lions have begun to descend from the peaks.",
      "hidden": false,
      "conditional": {
        "hidden": true,
        "conditions": {
          "maxViewportWidth": 320
        }
      }
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
              "minViewportWidth": 768
            }
          ]
        }
      ]
    }
  }
}
```

## Properties

- `app` (string): The application in which a person views the Apple News article.

  Valid values:

  - `any`: The person is viewing the Apple News article in either the Apple News app or in the Stocks app.
  - `news`: The person is viewing the Apple News article in the Apple News app.
  - `stocks`: The person is viewing the Apple News article in the Stocks app.

  **Default**: `any`; **Allowed Values**: `any`, `news`, `stocks`
- `following` ((boolean | string)): A Boolean or a string value to indicate whether the person viewing the article is following the channel that published the article. When you set the value to `true` or `false`, the system infers the channel ID from the article. When you set the value to a channel ID string, the conditional validates to `true` when the person is following that channel.

  **Allowed Types**: `boolean`, `string`
- `horizontalSizeClass` (string): A string describing the width at which Apple News displays the article. The value indicates whether iOS considers the article width constrained (`compact`) or expansive (`regular`). When Apple News displays the article at the specified size class, the conditional properties are in effect. The horizontal size class is always `regular` in macOS.

  **Allowed Values**: `any`, `regular`, `compact`
- `maxColumns` (integer): The maximum number of columns in which Apple News displays the article. When a person views the article with the specified number of columns or fewer, the conditional properties are in effect. For more information about the column system, see [Planning the Layout for Your Article](../AppleNews/planning-the-layout-for-your-article.md).

  **Minimum**: `1`
- `maxContentSizeCategory` (string): A string indicating a dynamic type size at which Apple News displays the article. When the article is displayed at the specified size or smaller, the conditional properties are in effect. The default content size category in iOS and macOS is `L`.

  **Default**: `AX-XXXL`; **Allowed Values**: `XS`, `S`, `M`, `L`, `XL`, `XXL`, `XXXL`, `AX-M`, `AX-L`, `AX-XL`, `AX-XXL`, `AX-XXXL`
- `maxSpecVersion` (string): An Apple News Format version that an Apple News client can use to display an article. When the Apple News Format version is equal to or less than the specified value, the conditional properties are in effect.
- `maxViewportAspectRatio` (float): A number indicating a width divided by a height. When the aspect ratio of the person’s viewport is the specified value or smaller, the conditional properties are in effect.

  **Minimum**: `0`
- `maxViewportWidth` (integer): A number indicating width in points. When the width of the person’s viewport is the specified value or smaller, the conditional properties are in effect.
- `minColumns` (integer): The minimum number of columns in which Apple News displays the article. When a person views the article with the specified number of columns or more, the conditional properties are in effect. For more information about the column system, see [Planning the Layout for Your Article](../AppleNews/planning-the-layout-for-your-article.md).

  **Minimum**: `0`
- `minContentSizeCategory` (string): A string indicating a dynamic type size at which Apple News displays the text in the article. When Apple News displays the article at the specified dynamic type size or greater, the conditional properties are in effect. The default content size category in iOS and macOS is `L`.

  **Default**: `XS`; **Allowed Values**: `XS`, `S`, `M`, `L`, `XL`, `XXL`, `XXXL`, `AX-M`, `AX-L`, `AX-XL`, `AX-XXL`, `AX-XXXL`
- `minSpecVersion` (string): An Apple News Format version that can be used by an Apple News client that is displaying an article. When the Apple News Format version is equal to or greater than the specified value, the conditional properties are in effect.
- `minViewportAspectRatio` (float): A number indicating a width divided by a height. When the aspect ratio of the person’s viewport is the specified value or greater, the conditional properties are in effect.

  **Minimum**: `0`
- `minViewportWidth` (integer): A number indicating the width in points. When the width of the person’s viewport is the specified value or greater, the conditional properties are in effect.
- `platform` (string): A platform on which a person can view an article. When the person views the article on the specified platform, the conditional properties are in effect.

  **Allowed Values**: `any`, `ios`, `macos`, `web`
- `preferredColorScheme` (string): A string describing the person’s preferred color theme for the system.

  Valid values:

  - `any`. The person has no preference.
  - `light`. The person hasn’t enabled Dark Mode.
  - `dark`. The person has enabled Dark Mode.

  **Allowed Values**: `any`, `light`, `dark`
- `subscriptionStatus` (string): The type of subscription the person has. When the subscription is of the specified type, the conditional properties are in effect.

  **Allowed Values**: `bundle`, `subscribed`
- `verticalSizeClass` (string): A string describing the height at which Apple News displays the article. The value indicates whether iOS considers the article width  constrained (`compact`) or expansive (`regular`). When Apple News displays the article at the specified size class, the conditional properties are in effect. The vertical size class is always `regular` in macOS.

  **Allowed Values**: `any`, `regular`, `compact`
- `territory` (string): The territory of the person. When the value is specified, the conditional properties are in effect.

  **Allowed Values**: `US`, `AU`, `GB`, `CA`
- `viewLocation` (string): The context of the article. When the context is of the specified type, the conditional properties are in effect.

  **Allowed Values**: `any`, `article`, `issue_table_of_contents`, `issue`

## See Also

### Conditional Design Elements
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
- [object ConditionalButton](./conditionalbutton.md)
  The object for defining a button component’s conditional properties, and when the conditional properties are in effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/condition)*