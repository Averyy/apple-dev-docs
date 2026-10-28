# ArticleDocument.componentStyles

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

An object containing component style objects that components in the article can refer to.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object ArticleDocument.componentStyles
```

## Mentions

- [Enhancing Your Articles with Styles](../../AppleNews/enhancing-your-articles-with-styles.md)
- [Defining a Component Style](../../AppleNews/defining-a-component-style.md)

## Discussion

`ArticleDocument.componentStyles` is an object containing the component style objects that components in your article can use. You provide each component style object as a key-value pair. In each pair, you create a key that’s meaningful to you. The value of each pair is a [`ComponentStyle`](../componentstyle.md) object.

### Example

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
    "backgroundColor": "#FFFFFF"
  },
  "components": [
    {
      "role": "section",
      "style": "exampleStyle",
      "components": [
        {
          "role": "body",
          "text": "Apple News Format allows publishers to craft beautiful editorial layouts. Galleries, audio, video, and fun interactions like animation make stories spring to life.",
          "layout": {
            "margin": {
              "top": 10,
              "bottom": 10
            }
          }
        }
      ]
    }
  ],
  "componentTextStyles": {},
  "textStyles": {},
  "componentStyles": {
    "exampleStyle": {
      "backgroundColor": "#FFFFFF",
      "opacity": 1,
      "border": {
        "all": {
          "width": 1,
          "color": "black"
        },
        "left": false,
        "right": false
      }
    }
  },
  "componentLayouts": {}
}
```

## Properties

- `Any Key` (ComponentStyle): A component style, with a name you define that components within this document can refer to.

## See Also

### Objects
- [object ArticleDocument.componentLayouts](./componentlayouts-data.dictionary.md)
  An object containing component layout objects that components in the article can refer to.
- [object ArticleDocument.componentTextStyles](./componenttextstyles-data.dictionary.md)
  An object containing component text style defaults as well as component text styles that components in the article can use.
- [object ArticleDocument.textStyles](./textstyles-data.dictionary.md)
  An object containing text style objects that components within this document can refer to inline in text.
- [object ArticleDocument.colorScheme](./colorscheme-data.dictionary.md)
  The object that contains information about the color scheme of the document, including Dark Mode behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/articledocument/componentstyles-data.dictionary)*