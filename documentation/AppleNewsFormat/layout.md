# Layout

**Framework**: AppleNewsFormat  
**Kind**: dictionary  
**Role**: Object

The object for defining columns, gutters, and margins for your article’s designed width.

**Availability**:
- Apple News Format 1.7+

## Declaration

```
object Layout
```

## Mentions

- [Positioning the Content in Your Article](../AppleNews/positioning-the-content-in-your-article.md)
- [JSON Concepts and Article Structure](../AppleNews/json-concepts-and-article-structure.md)
- [Planning the Layout for Your Article](../AppleNews/planning-the-layout-for-your-article.md)
- [Preparing Image, Video, Audio, Music, and ARKit Assets](../AppleNews/preparing-image-video-audio-music-and-arkit-assets.md)

## Discussion

Use the `Layou`t object to define the column-system rules for the components in your document. The column system controls the horizontal position and spacing of your components. The News app uses this information to automatically resize your article for different screen sizes. Configuring your article with 20 columns, a 60-point margin, and a 20-point gutter should give you a sufficiently flexible layout.

After you define your article’s layout, add its components to [`ArticleDocument.componentLayouts`](./articledocument/componentlayouts-data.dictionary.md) and then position each component using a [`ComponentLayout`](./componentlayout.md) object.

You can use object in [`ArticleDocument`](./articledocument.md).

### Example

```json
{
  "version": "1.7",
  "identifier": "SampleArticle",
  "language": "en",
  "title": "Apple News",
  "layout": {
    "columns": 20,
    "width": 1024,
    "margin": 60,
    "gutter": 20
  },
  …
}
```

## Properties

- `columns` (integer) *(required)*: The number of columns in this article’s design. You must have at least one column.

  Using a 7-column design allows components to start in columns 0 to 6, and be between 1 and 7 columns wide. An article designed with 7 columns provides sufficient layout information to automatically resize for  iPad, iPhone, Mac, and Apple Vision Pro sizes. An article designed with 20 columns provides more detail for the layout system and a better reading experience. Below 5 columns there may not be sufficient information for the layout system to automatically maintain your intended design when scaling down to smaller devices.

  **Minimum**: `1`
- `width` (integer) *(required)*: The `width` (in points) this article was designed for. Apple News uses this property to calculate down-scaling scenarios for smaller devices.

  The width of the document must be sufficient to fit two margin values and the gutter values that are needed between each of the columns.

  The `width` can’t be negative or `0`. As a best practice, set the width to the width of the iPad device. This helps you see the effects of positioning components in different columns.

  Apple News uses this property to automatically scale down article content for smaller devices. With a 7-column design and a width of `1024` points, the design is optimal for a landscape aspect ratio on iPad and scales down on iPhone.

  **Minimum**: `1`
- `gutter` (integer): The gutter size for the article (in points). The gutter provides spacing between columns. Use an even number for this property; Apple News rounds up odd numbers to the next even number. If you omit this property, Apple News applies a default gutter size of 20. If the gutter is negative, Apple News sets the number to 0.

  Note that the first column doesn’t have a left gutter, and the last column doesn’t have a right gutter.

  The width of the document must be sufficient to fit two margin values and the gutter values needed between each of the columns.

  Note that when using a width of 1024, a margin of 60, and 7 columns, the gutter can’t be greater than 150.

  **Default**: `20`; **Minimum**: `0`
- `margin` (integer): The outer (left and right) margins of the article, in points. If you omit this property, Apple News applies a default article margin of 60. If the margin is negative, the number is set to 0. If the margin is greater than or equal to the width divided by 2, the article delivery fails.

  Apple News sizes down the margins slightly when it scales down the article automatically for smaller devices.

  **Default**: `60`; **Minimum**: `0`

## See Also

### Article Layout
- [Planning the Layout for Your Article](../AppleNews/planning-the-layout-for-your-article.md)
  Define a layout that supports the look you want for your article.
- [Positioning the Content in Your Article](../AppleNews/positioning-the-content-in-your-article.md)
  Align article components with columns in your layout.
- [Wrapping Text Around a Component](../AppleNews/wrapping-text-around-a-component.md)
  Define the layout of a text component to wrap around another component.
- [object ComponentLayout](./componentlayout.md)
  The object for defining the positioning for a specific component within the article’s column system.
- [object Anchor](./anchor.md)
  The object for anchoring one component to another component in your article’s layout.
- [object Margin](./margin.md)
  The object for defining the space above and below a component.
- [object AutoPlacementLayout](./autoplacementlayout.md)
  The object for defining the margin above and below advertising components.
- [object AdvertisingLayout](./advertisinglayout.md)
  The object for defining the margin above and below advertising components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenewsformat/layout)*