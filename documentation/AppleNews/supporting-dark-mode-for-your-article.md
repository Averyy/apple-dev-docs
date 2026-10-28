# Supporting Dark Mode for Your Article

**Framework**: Apple News  
**Role**: Article

Update your article template so that your article adapts when Dark Mode is active.

## Overview

> **Note**:  Automatic Dark Mode support is available in iOS 14, iPadOS 14, and macOS 10.16 and later.

In Apple News Format, you can customize the appearance of your article in Dark Mode. Do the following:

- Use the value `dark` for the [`Condition`](../AppleNewsFormat/condition.md) object’s `preferredColorScheme` property.
- Set conditions for [`DocumentStyle`](../AppleNewsFormat/documentstyle.md), [`TextStyle`](../AppleNewsFormat/textstyle.md), [`ComponentTextStyle`](../AppleNewsFormat/componenttextstyle.md), and [`ComponentStyle`](../AppleNewsFormat/componentstyle.md).

If you don’t configure Dark Mode, Apple News automatically inverts colors for automatic Dark Mode.

You can customize the appearance of components requiring special consideration in Dark Mode while retaining automatic color inversion for others.

When automatic Dark Mode is on, Apple News does the following:

- Evaluates `documentStyle.backgroundColor` to determine if the article already has a dark appearance.
- Evaluates the colors in the article and picks an inverted color to automatically switch to a dark appearance.

You can control the way your article appears in Dark Mode by changing your article template to use darker background colors and lighter foreground colors, and you can modify styles to make your article content stand out. To set up different styles based on conditions, see [`ConditionalDocumentStyle`](../AppleNewsFormat/conditionaldocumentstyle.md), [`ConditionalTextStyle`](../AppleNewsFormat/conditionaltextstyle.md), [`ConditionalComponentTextStyle`](../AppleNewsFormat/conditionalcomponenttextstyle.md), and [`ConditionalComponentStyle`](../AppleNewsFormat/conditionalcomponentstyle.md).

Here are some important points to note about automatic Dark Mode in Apple News:

- Text styling you use for full-screen image [`Caption`](../AppleNewsFormat/caption.md) isn’t inverted.
- In a [`Text`](../AppleNewsFormat/text.md) component, the text colors aren’t inverted if any of their parent containers use a fill.
- [`GradientFill`](../AppleNewsFormat/gradientfill.md) colors aren’t inverted.

The sections that follow provide example code that shows how to modify properties to set up your article for Dark Mode.

### Define Document Style

In this code example, note how the `backgroundColor` property within the `preferredColorScheme`, `dark` condition, sets up the document style for Dark Mode. This conditional background color appears any time a device is in Dark Mode.

```json
{
  "documentStyle": {
    "backgroundColor": "#FFF",
    "conditional": [
      {
        "backgroundColor": "#000",
        "conditions": [
          {
            "preferredColorScheme": "dark"
          }
        ]
      } 
    ]
  }  
}
```

### Define Text Style

In this code example, note how the `textColor` property within the `preferredColorScheme`, `dark` condition, sets up the text style for Dark Mode. This conditional text color appears any time a device is in Dark Mode.

```json
{
  "textStyles": {
    "default-tag-abbr": {
      "textColor": "#34AF15",
      "conditional": [
        {
          "textColor": "#FFC800",
          "conditions": [
            {
              "preferredColorScheme": "dark"
            }
          ]
        }
      ]
    }
  },
  "components": [
    {
      "role": "body",
      "format": "html",
      "text": "<p>The <abbr>WWF</abbr> is an international wildlife fund.</p>"
    }
  ]
}
```

### Define Component Text Style

In this code example, note how the `textColor` property within the `preferredColorScheme`, `dark` condition, sets up the component text style for Dark Mode. This conditional text color appears any time a device is in Dark Mode.

```json
{
  "componentTextStyles": {
    "exampleStyle": {
      "textColor": "#666",
      "conditional": [
        {
          "textColor": "#FFF",
          "conditions": [
            {
              "preferredColorScheme": "dark"
            }
          ]
        }
      ]
    }
  },
  "components": [
    {
      "role": "body",
      "text": "This is body text",
      "textStyle": "exampleStyle"
    }
  ]
}
```

### Define Component Style

In this code example, note how the `color` property for the `border` object within the `preferredColorScheme`, `dark` condition, sets up the component style for Dark Mode. This conditional color appears any time a device is in Dark Mode.

```json
{
    "role": "container",
    "layout": {},
    "style": {
      "border": {
        "all": {
          "width": 1,
          "color": "#333"
        }
      },
      "conditional": [
        {
          "border": {
            "all": {
              "width": 1,
              "color": "#FFF"
            }
          },
          "conditions": [
            {
              "preferredColorScheme": "dark"
            }
          ]
        }
      ]
    },
    "components": [
      {
        "role": "title",
        "text": "Test Title"
      }
    ]
  }
```

## See Also

### Styles
- [Enhancing Your Articles with Styles](./enhancing-your-articles-with-styles.md)
  Improve the appearance of the text and components in your article by using Apple News Format styles.
- [object DocumentStyle](../AppleNewsFormat/documentstyle.md)
  The object for setting the background color for your article.
- [Text Styles](./text-styles.md)
  Learn about text styles and how to apply them to your text and text components.
- [Component Styles](./component-styles.md)
  Learn to use component styles to add borders, set background colors, and apply background images to components and to set the styling for tables.
- [Supported Color Names](./supported-color-names.md)
  Learn the color names supported in Apple News Format.
- [type Color](../AppleNewsFormat/color.md)
  The strings for defining colors in Apple News Format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/supporting-dark-mode-for-your-article)*