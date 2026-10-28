# ArticleDocument.colorScheme

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object that contains information about the color scheme of the document, including Dark Mode behavior.

**Availability**:
- Apple News Format 1.14.1+

## Declaration

```
object ArticleDocument.colorScheme
```

## Discussion

Use the c`olorScheme` object to enable or disable automatic Dark Mode in a document.

### Example

```json
{
 "version": "1.14.1",
 "identifier": "SampleArticle",
 "language": "en",
 "title": "Apple News",
 "subtitle": "A look at the features of Apple News",
 "layout": {
   "columns": 20,
   "width": 1024,
   "margin": 60,
   "gutter": 20
 },
 …
 "colorScheme": {
   "automaticDarkModeEnabled": true
 }
}
```

## Properties

- `automaticDarkModeEnabled` (boolean): A Boolean value that indicates whether automatic Dark Mode is enabled for the document. The value for this property defaults to `true`, which causes the document to be inverted when the user switches the device to Dark Mode.

  **Default**: `true`

## See Also

### Objects
- [object ArticleDocument.componentLayouts](./componentlayouts-data.dictionary.md)
  An object containing component layout objects that components in the article can refer to.
- [object ArticleDocument.componentStyles](./componentstyles-data.dictionary.md)
  An object containing component style objects that components in the article can refer to.
- [object ArticleDocument.componentTextStyles](./componenttextstyles-data.dictionary.md)
  An object containing component text style defaults as well as component text styles that components in the article can use.
- [object ArticleDocument.textStyles](./textstyles-data.dictionary.md)
  An object containing text style objects that components within this document can refer to inline in text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/articledocument/colorscheme-data.dictionary)*