# Adding an HTML Table

**Framework**: Applenews

Add a table formatted in HTML to your article.

#### Overview

To add an HTML table to your article, you add a component with the `role` property set to `htmltable`. In the required `html` property, add the coded HTML table consisting of your data and the HTML tags that indicate rows. Make sure that all of your HTML code is enclosed in `<table> </table>` tags.

To change the appearance of an HTML table, you can use any of the HTML tags Apple News Format supports; for more information, see [`Using HTML with Apple News Format`](using-html-with-apple-news-format.md). You can also apply c`omponentStyles` from Apple News Format; for more information, see [`TableStyle`](https://developer.apple.com/documentation/applenewsformat/tablestyle).

##### Review the Html Table Tags

Apple News Format supports these tags for HTML tables:

```html
	<table> </table>

	<th> </th>

	<tr> </tr>

	<td> </td>

	<thead> </thead>

	<tbody> </tbody>

	<tfoot> </tfoot>

	<caption> </caption>
```

> **Note**: HTML `<th>` or `<td>` elements that span multiple columns or rows aren’t supported. Apple News Format ignores `colspan` and `rowspan` attributes.

This list describes how to use the basic HTML table tags:

- Begin each row of the table (including the header row) with `<tr>` and end each row with `</tr>`.
- Use table heading tags (`<th>` and `</th>`) around each element in the table header.
- Put table data tags (`<td>` and `</td>`) around each element in a row.
- Enclose a  single row or group of rows in `<thead>`, `<tbody>`, or `<tfoot>` tags.
- Style your table text using supported HTML tags. See [`Using HTML with Apple News Format`](using-html-with-apple-news-format.md).
- Use a JSON [`ComponentStyle`](https://developer.apple.com/documentation/applenewsformat/componentstyle) that has the `tableStyle` object defined to specify table alignment, table padding, and other, nontextual table styles. Apple News Format ignores any style-related HTML attributes, such as `cellpadding`, `cellspacing`, `width`, and `alignment`.

Consider the following example HTML code:

```html
<table><tr><th>First Name</th><th>Last Name</th></tr>
<tr><td>John</td><td>Appleseed</td></tr></table>
```

This code results in a table with two columns and two rows — one row is for the heading and one is for data.

| First name | Last name |
| --- | --- |
| John | Appleseed |

## See Also

- [object HTMLTable](../applenewsformat/htmltable.md)
  The component for adding tables with HTML data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleNews/adding-an-html-table)*