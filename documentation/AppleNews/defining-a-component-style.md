# Defining a Component Style

**Framework**: Apple News

Set style options for the components in your article.

#### Overview

You can use component styles to add interest and variety to your article and to make some content easier to read. Component styles include:

- Background color. Set a background color for the component.
- Corner radius. Apply rounded corners to a component by using the `mask` property in [`ComponentStyle`](https://developer.apple.com/documentation/applenewsformat/componentstyle).
- Fill. Use an image or video for a component background, or set a gradient fill that transitions from one color to another.
- Opacity. Set the opacity for a component from completely opaque to completely transparent.
- Border. Set the border color, width, and style for a component or for a table cell.
- Table style. Specify the styling (color, stroke style, text style, and so on) that you want for the rows, columns, and cells of a data or HTML table.

##### Define a Style

To use a component style once, simply include a [`ComponentStyle`](https://developer.apple.com/documentation/applenewsformat/componentstyle) object as the value of the individual component’s style property.

To define a style for multiple components:

1. In the [`ArticleDocument.componentStyles`](https://developer.apple.com/documentation/applenewsformat/articledocument/componentstyles-data.dictionary) object, include a property with a name that you define and a `ComponentStyle` object value.
2. Use the name you defined as the value of the individual componentʼs style property.

For more about properties and objects, see [`JSON Concepts and Article Structure`](json-concepts-and-article-structure.md).

## See Also

- [object ComponentStyle](../applenewsformat/componentstyle.md)
  The object for setting style properties for components, including background color and fill, borders, and table styles.
- [object CornerMask](../applenewsformat/cornermask.md)
  The object for creating rounded corners.
- [object Border](../applenewsformat/border.md)
  The object for setting borders for component sides or tables.
- [object StrokeStyle](../applenewsformat/strokestyle.md)
  The object for defining the color, width, and style of a border or divider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/defining-a-component-style)*