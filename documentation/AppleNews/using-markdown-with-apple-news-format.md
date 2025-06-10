# Using Markdown with Apple News Format

**Framework**: Apple News

Use Markdown formatting for text components.

#### Overview

Apple News Format supports a subset of Markdown syntax. You can use Markdown in the following components by setting the `format` property to `markdown`.

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

In addition to the components above, you can also use Markdown to format text in [`CaptionDescriptor`](https://developer.apple.com/documentation/applenewsformat/captiondescriptor), and [`FormattedText`](https://developer.apple.com/documentation/applenewsformat/formattedtext) objects.

##### Example

```json
{
"role": "heading",
"text": "1\\. First list item",
"format": "markdown"
}
```

To learn more about Markdown, visit the [`Markdown`](https://developer.apple.comhttps://commonmark.org) website.

##### Text Level Markdown Syntax

Apple News Format supports these Markdown features within text paragraphs.

###### Emphasis Italics

Use single asterisks (`*`) or single underscores (`_`).

```other
A sentence with _emphasis_ and two different types of *emphasis notation*.
```

A sentence with  and two different types of .

```other
This _sentence_'s Markdown formatting is (_more_) in_volved_.
```

This ’s Markdown formatting is () in.

###### Strong Emphasis Bold

To make text bold, use double asterisks (`**`) or double underscores (`__`).

```other
A sentence containing something **really important**.
```

A sentence containing something .

```other
This __sentence__'s Markdown formatting is (__more__) in__volved__.
```

This ’s Markdown formatting is () in.

###### Combined Emphasis Italics and Strong Bold

You can nest emphasis and strong emphasis to use bold-italic font faces by using underscores with double asterisks (or double underscores with single asterisks).

```other
A _**sentence**_ containing **_four_** ways to __*combine*__ strong and *__emphasis__*.
_An emphasized sentence containing a **strong phrase**._
```

In the first example, the words , , , and  are in both italics and bold.

In the second example, the entire sentence is displayed in italics with  in italics and bold.

```other
This _**sentence**_'s Markdown formatting is (__*more*__) *in__volved__*.
```

In this example, the word  (but not the apostrophe and the letter  that follow it) is in italics and bold, as is the word  (but not the parentheses). The  portion of the word  is also italics and bold, while the  part of the word is italics only.

> **Note**: Apple News Format doesn’t support the use of triple asterisks (`***`) or triple underscores (`___`) to create bold-italic.

###### Strikethrough

For strikethrough text, surround with double tildes (~~).

```other
A sentence containing something ~~no longer neeeded~~.
```

In this example, the text  is crossed out.

##### Links

To add a link with Markdown, use brackets for the linked text and parentheses for the link URL. Brackets must contain at least one character; empty brackets are invalid.

:

```other
This text contains [a link to another page](http:/www.apple.com).
_This emphasized sentence contains [a link to another page] (http://www.apple.com)_.
This text contains an emphasized [_link to another page_](http://www.apple.com).
```

:

The first example contains a simple link.

The second example italicizes the entire sentence, including the link text.

The third example italicizes just the link.

> **Note**: Apple News Format doesn’t support Markdown reference links, which use a second set of square brackets that contain a label that’s defined elsewhere in the article.

##### Block Level Markdown

###### Headings

To indicate that text is a heading, use the `#` character.

`# Heading 1`

`## Heading 2`

`### Heading 3`

`#### Heading 4`

`##### Heading 5`

`###### Heading 6`

###### Inline Text Style

To apply a text style that you have already defined in Apple News Format, use square brackets (`[]`) to enclose the text you want to format and put the name of the text style you want to use in curly brackets (`{}`). You must define the text style you refer to using the `textStyles` property in the article document properties.

For this example, `specialTextStyle` is predefined to be . (Your actual result depends on how you define `specialTextStyle`.)

:

```other
The trail passes the [Big Sur Waterfall]{specialTextStyle} before ending in the valley.
```

:

The trail passes the  before ending in the valley.

###### Paragraphs

To separate text into paragraphs, use two of the Markdown new line tags `(\n\n)` between the end of one paragraph and the beginning of the next paragraph. In JSON, new lines are encoded as `\n`.

:

```other
Last line of paragraph 1.\n\nFirst line of paragraph 2.
```

:

Last line of paragraph 1.

First line of paragraph 2.

Apple News Format doesn’t support Markdown paragraph and line separators (`\n` or `\n\n`) at the beginning or end of components. To add space in these locations within a component, use layout margins.

> **Note**: Apple News Format does not support single `\n` or `\r` Markdown tags. You can use the Unicode line separator `(\u2028)` to start a new line.

###### Lists

###### Bulleted List

To create a bulleted list item, start a new line, then type either a hyphen (`-`), an asterisk (`*`), or a plus sign (`+`) followed by a space.

```other
- First item
- Second item
```

- First item
- Second item

###### Numbered List

Use numbers and periods followed by a space (`1. `).

```other
1. First numbered item
2. Second numbered item
```

1. First numbered item
2. Second numbered item

###### Numbered List in Apple News Format

In a numbered list, Apple News Format restarts at 1 for each new component — no matter what number you provide in your text.

If you need to separate a list into multiple components, remove `"format": "markdown"` from each component or “escape” the period with two backslashes (`\\`), as shown in the following JSON example:

```json
{
   "role": "heading",
   "text": "1\\. First list item",
   "format": "markdown"
},
{
   "role": "heading",
   "text": "2\\. Second list item",
   "format": "markdown"
}
```

1. First list item
2. Second list item

###### Divider

To create a divider line or horizontal rule, type at least 3 hyphens (`---`) or 3 asterisks (`***`) on a new, empty line.

```other
Dividers can separate portions of text.
---
Here's the epilogue to my story.
```

###### Maps

To add a map that renders within your article, begin the URL for your map with `https://maps.apple.com/`. When Apple News Format renders the article, it converts the link to a map that you can manipulate the same way as a `map` component. If your URL doesn’t start with `https://maps.apple.com/`, then Apple News Format only displays a link to the map.

:

```other
Apple's main campus occupies 172 acres at [Apple Park](https://maps.apple.com?sll=37.3327,-122.00533&t=standard&spn=0.02,0.02&q=Apple%20Inc).
```

:

Apple’s main campus occupies 172 acres at Apple Park.

![Screenshot of a full-screen map showing the location of Apple Park in Cupertino.](https://docs-assets.developer.apple.com/published/7b5d4d4847a0d404897033151e56bbe8/media-3591443%402x.png)

##### Escaping Markdown

To escape special Markdown characters in a JSON document, use two backslashes (one to escape Markdown and one to escape JSON) as shown in the following examples:

###### Example 1

:

```other
This is an asterisk: \*\n\nThis is an underscore: \_
```

:

```other
This is an asterisk: \\*\n\nThis is an underscore: \\_
```

:

This is an asterisk: *

This is an underscore: _

###### Example 2

:

```other
1. First list item\n1. Second list item\n\n1\. Not a list item
```

:

```other
1. First list item\n1. Second list item\n\n1\\. Not a list item
```

1. First list item
2. Second list item

`1`. Not a list item

## See Also

- [Using HTML with Apple News Format](using-html-with-apple-news-format.md)
  Use HTML formatting for text components.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/using-markdown-with-apple-news-format)*