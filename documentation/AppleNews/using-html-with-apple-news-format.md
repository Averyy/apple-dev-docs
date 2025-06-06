# Using HTML with Apple News Format

**Framework**: Applenews

Use HTML formatting for text components.

#### Overview

Apple News Format supports a subset of HTML tags. You can use HTML tags in these components by setting their `format` property to `html`.

- [`Author`](https://developer.apple.com/documentation/applenewsformat/author)
- [`Body`](https://developer.apple.com/documentation/applenewsformat/body)
- [`Byline`](https://developer.apple.com/documentation/applenewsformat/byline)
- [`Caption`](https://developer.apple.com/documentation/applenewsformat/caption)
- [`Heading`](https://developer.apple.com/documentation/applenewsformat/heading)
- [`Illustrator`](https://developer.apple.com/documentation/applenewsformat/illustrator)
- [`Intro`](https://developer.apple.com/documentation/applenewsformat/intro)
- [`Photographer`](https://developer.apple.com/documentation/applenewsformat/photographer)
- [`PullQuote`](https://developer.apple.com/documentation/applenewsformat/pullquote)
- [`Quote`](https://developer.apple.com/documentation/applenewsformat/quote)
- [`Title`](https://developer.apple.com/documentation/applenewsformat/title)

In addition to the components above, you can also use HTML tags to format text in [`CaptionDescriptor`](https://developer.apple.com/documentation/applenewsformat/captiondescriptor) and [`FormattedText`](https://developer.apple.com/documentation/applenewsformat/formattedtext) objects.

To include an HTML table in your article, see [`Adding an HTML Table`](adding-an-html-table.md).

##### Example

```json
{
"role": "body",
"text": "<a href=\"https://www.example.com\">Subscribe to our newsletter for more great stories.</a>",
"format": "html"
}
```

##### Supported Html Tags

This section describes how to use the HTML tags Apple News Format supports.

> **Note**: Generic containers and autonomous custom elements such as `<span>` and `<div>` are allowed; however, they have no effect until you apply styling to them.

Begin each paragraph block with `<p>`, and end each paragraph with `</p>`.

For example, this code:

```html
<p>Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio ducimus qui blanditiis.</p><p>Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer.</p><p>Temporibus autem et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque rerum hic tenetur.</p>
```

Results in three paragraphs:

```other
Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio ducimus qui blanditiis.
Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer.
Temporibus autem et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque rerum hic tenetur.
```

Use `<strong>` or `<b>` tags around the text you want in bold.

Use `<em>` or `<i>` tags around the text you want emphasized.

Use the HTML `<a href="">` tag for links.

> **Note**: In URLs, be sure to escape any special characters, such as double quotation marks (`"`) or backslashes (`\`), using a backslash (`\`). For example, `<a href=\"http://www.apple.com\">Apple</a>`.

To add a hyperlink to another component in the same article, use an anchor link that starts with the hash symbol (#) and is followed by the `identifier` property for the component you want to link to.

This example shows a link to a `chapter` component with its `identifier` set to `chapter-1`:

```html
The text continues in <a href=\"#chapter-1\">Chapter One</a>.
```

To link to a component in another article, you must include an Apple News URL followed by the hash symbol (#) and component identifier as shown here:

```html
The recipe is <a href=\"https://apple.news/A5vHgPPmQSvuIxPjeXLTdGQ#TextComponent-1\">here</a>.
```

Use the `<ul>` tag to start an unordered (bulleted) list and the `<ol>` tag to start an ordered (numbered) list. Use the `<li>` tag to indicate each item in a list.

For example, this HTML code:

```html
<ul><li>apples</li><li>oranges</li></ul>
```

Results in this unordered, bulleted list:

- apples
- oranges

This HTML code:

```html
<ol><li>apples</li><li>oranges</li></ol>
```

Results in this numbered list:

1. apples
2. oranges

To create a single line break, use the `<br>` or `<br/>` tag.

For example, this HTML code:

```html
<p>Apple<br>1 Infinite Loop<br>Cupertino, CA</p>
```

Results in three lines of text using single line spacing:

Apple

1 Infinite Loop

Cupertino, CA

Use `<sub>` or `<sup>` tags around the text.

Use `<del>` or `<s>` tags around the text.

To represent preformatted blocks of text and preserve their white space, use the `<pre>` tag around the block.

For example, this coded text:

```html
<pre>var occupations = [\n\t"Malcolm": "Captain",\n\t"Kaylee": "Mechanic"\n]</pre>
```

Results in:

```other
var occupations = [
    "Malcolm": "Captain",
    "Kaylee": "Mechanic"
]
```

For information on displaying the contents of your `<pre>` tag using a monospaced font, see [`Text Styling`](using-html-with-apple-news-format#Text-Styling.md).

To add text that represents code to your article, use the HTML `<code>` or `<samp>` tags around the text.

For information on displaying the contents of your `<code>` or `<samp>` tag using a monospaced font, see [`Text Styling`](using-html-with-apple-news-format#Text-Styling.md).

To define a footer that isn’t part of the main story — like an author biography or copyright notice — use `<footer>` tags.

You can use `<aside>` tags to define a section of the text that is related to, but not part of, the main story. Using an [`Aside`](https://developer.apple.com/documentation/applenewsformat/aside) component has the additional benefit of helping Siri make more informed recommendations.

To set off a long quotation (or any text) in your article, you can use the HTML `<blockquote>` tag. However, if you want to use different margins for your block quote, use the Apple News Format [`Quote`](https://developer.apple.com/documentation/applenewsformat/quote) component instead.

##### Text Styling

You can change the appearance of text in your article using styles from Apple News Format, HTML tags, or a combination of both. The following sections show you how to use HTML with Apple News Format text styles.

You can create text styles that automatically get applied to HTML-tagged text, by using special names for your text style objects in [`ArticleDocument.textStyles`](https://developer.apple.com/documentation/applenewsformat/articledocument/textstyles-data.dictionary). Once you define the style for a specific HTML tag, then all occurrences of the HTML tag in your article receive that same text style.

For example, if you create a text style called `default-tag-pre` as shown here, all occurrences of the HTML `<pre>` tag in the article use the monospaced Menlo-Regular font and are dark gray.

```other
"textStyles": {
  "default-tag-pre": {
    "fontName": "Menlo-Regular",
      "textColor": "#333"
  }
}
```

You can also refer to any of your text styles by name in supported HTML tags. Within your HTML tag, use the `data-anf-textstyle` attribute to refer to the text style you want to use for your HTML-formatted text component.

For example, if you already have a custom text style called `authorNameStyle`, you can refer to it from within your HTML code:

```other
"components": [
 {
    "role": "body",
    "format": "html",
    "text": "<p>This document is written by <author data-anf-textstyle=\"authorNameStyle\">John Appleseed</author></p>"
  }
]
```

Apple News Format supports special characters that are encoded as HTML entities. This includes named entities like `&quot`; (for a double-quote character) or `&infin`; (for an infinity sign (∞)), as well as numeric entities like `&#169`; (for a copyright symbol (©)).

Apple News Format ignores most attributes on your HTML tags, but there are some exceptions. You can use:

- The `href` attribute of the `<a>` tag
- The `data-anf-textstyle` attribute on all supported tags

##### Unsupported Html Tags

The following is a list of unsupported HTML tags. Apple News Format rejects articles that contain HTML formatting with these tags.

|  |  |
| --- | --- |
| `<img>` | Use the [`Photo`](https://developer.apple.com/documentation/applenewsformat/photo), [`Portrait`](https://developer.apple.com/documentation/applenewsformat/portrait), [`Figure`](https://developer.apple.com/documentation/applenewsformat/figure), or [`Logo`](https://developer.apple.com/documentation/applenewsformat/logo) component instead. If none of those components describes your content, you can use the generic [`Image`](https://developer.apple.com/documentation/applenewsformat/image) component. |
| `<video>` | Use the [`Video`](https://developer.apple.com/documentation/applenewsformat/video) or [`EmbedWebVideo`](https://developer.apple.com/documentation/applenewsformat/embedwebvideo) (for YouTube and Vimeo video) component instead. |
| `<audio>` | Use the [`Audio`](https://developer.apple.com/documentation/applenewsformat/audio) component instead. |
| `<title>` | There is no replacement for this tag. |
| `<meta>` | There is no replacement for this tag. |
| `<script>` | There is no replacement for this tag. |
| `<noscript>` | There is no replacement for this tag. |
| `<style>` | There is no replacement for this tag. |
| `<link>` | There is no replacement for this tag. |
| `<applet>` | There is no replacement for this tag. |
| `<object>` | There is no replacement for this tag. |
| `<iframe>` | There is no replacement for this tag. |
| `<noframes>` | There is no replacement for this tag. |
| `<form>` | There is no replacement for this tag. |
| `<select>` | There is no replacement for this tag. |
| `<option>` | There is no replacement for this tag. |
| `<optgroup>` | There is no replacement for this tag. |

## See Also

- [Using Markdown with Apple News Format](using-markdown-with-apple-news-format.md)
  Use Markdown formatting for text components.
- [object Body](../applenewsformat/body.md)
  The component for adding body text.
- [object Title](../applenewsformat/title.md)
  The component for adding an article title.
- [object Heading](../applenewsformat/heading.md)
  The text component for adding a heading.
- [object Intro](../applenewsformat/intro.md)
  The component for adding introductory text.
- [object Caption](../applenewsformat/caption.md)
  The component for adding caption text.
- [object Author](../applenewsformat/author.md)
  The component for adding the name of the author.
- [object Byline](../applenewsformat/byline.md)
  The component for adding the publication date or contributor credits, especially for articles with multiple contributors.
- [object Illustrator](../applenewsformat/illustrator.md)
  The component for adding illustrator credit.
- [object Photographer](../applenewsformat/photographer.md)
  The component for adding a photographer credit.
- [object Quote](../applenewsformat/quote.md)
  The component for including a quote.
- [object PullQuote](../applenewsformat/pullquote.md)
  The component for including a pull quote.
- [object Text](../applenewsformat/text.md)
  Properties shared by all text component types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleNews/using-html-with-apple-news-format)*