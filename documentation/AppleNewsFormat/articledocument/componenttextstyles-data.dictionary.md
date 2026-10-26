# ArticleDocument.componentTextStyles

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

An object containing component text style defaults as well as component text styles that components in the article can use.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ArticleDocument.componentTextStyles
```

## Mentions

- [Defining and Applying Text Styles](../../AppleNews/defining-and-applying-text-styles.md)
- [Enhancing Your Articles with Styles](../../AppleNews/enhancing-your-articles-with-styles.md)

#### Discussion

`ArticleDocument.componentTextStyles` is an object containing the component text style defaults as well as component text style objects that components in your article can use. You provide each component text style object as a key-value pair. The value of each pair is a [`ComponentTextStyle`](../componenttextstyle.md) object.

**To create a default style for the entire article**, use the key `"default"`. Apple News automatically applies this style to all text components.

**To create a default style for all body components**, use the key `"default-body"`. Apple News automatically applies this style  to all `body` components, after it applies the default style. If a property is in both `default-body` and `default`, the value in `default-body` overrides the property in `default`. This works for all components that inherit properties from [`Text`](../text.md), including [`Body`](../body.md), [`Title`](../title.md), and [`Heading`](../heading.md).

**To create a style for components to refer to**, create a key that’s meaningful to you. Apple News applies this style  to any components that refer to it, after it applies the default styles. If a property is in both the referenced style and one of the defaults, the property in the referenced style overrides the defaults.

##### Example

```json
{
  "title": "Article Title",
  "identifier": "sample",
  "version": "1.8",
  "language": "en",
  "layout": {
    "columns": 20,
    "width": 1024,
    "margin": 60,
    "gutter": 20
  },
  "documentStyle": {
    "backgroundColor": "#FFF"
  },
  "components": [
    {
      "role": "section",
      "components": [
        {
          "role": "body",
          "format": "html",
          "textStyle": "exampleStyle",
          "text": "<p>There is a moment in every dawn when light floats, there is the possibility of magic.</p>"
        }
      ]
    }
  ],
  "componentTextStyles": {
    "default": {
      "fontName": "Courier",
      "textColor": "#000",
      "fontSize": 22,
      "lineHeight": 20,
      "linkStyle": {
        "textColor": "#000",
        "underline": false
      },
      "hyphenation": false
    },
    "exampleStyle": {
      "fontFamily": "Gill Sans",
      "fontWeight": "bolder",
      "textColor": "#333333",
      "fontSize": 18,
      "textShadow": {
        "radius": 20,
        "opacity": 0.3,
        "color": "#99999930",
        "offset": {
          "x": -10,
          "y": 5
        }
      },
      "stroke": {
        "color": "#FFC800",
        "width": 1
      }
    }
  },
  "textStyles": {},
  "componentStyles": {},
  "componentLayouts": {}
}
```

## Properties

- `Any Key` (ComponentTextStyle): A component text style, with a name you define that components within this document can use.

## See Also

### Objects
- [object ArticleDocument.componentLayouts](./componentlayouts-data.dictionary.md)
  An object containing component layout objects that components in the article can refer to.
- [object ArticleDocument.componentStyles](./componentstyles-data.dictionary.md)
  An object containing component style objects that components in the article can refer to.
- [object ArticleDocument.textStyles](./textstyles-data.dictionary.md)
  An object containing text style objects that components within this document can refer to inline in text.
- [object ArticleDocument.colorScheme](./colorscheme-data.dictionary.md)
  The object that contains information about the color scheme of the document, including Dark Mode behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/articledocument/componenttextstyles-data.dictionary)*