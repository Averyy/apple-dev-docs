# Adding Color to Text Ranges

**Framework**: Apple News

Create text in color by using HTML to refer to TextStyle objects.

#### Overview

You can then edit the `TextStyle` object in one place and affect multiple ranges of text.

![Screenshot of an Apple News article with an HTML-styled inset pull quote on iPad.](https://docs-assets.developer.apple.com/published/f45f5334e481ed171b4c1f7aa2127d38/media-3624922%402x.png)

![Screenshot of an Apple News article with an HTML-styled layered header on iPad.](https://docs-assets.developer.apple.com/published/a16b6320509e20b24e416b0876fbd348/media-3624921%402x.png)

##### Create Textstyle Objects with Different Colors

Create the `TextStyle` objects that you will refer to inline in the HTML.

1. Copy the example code [`Styles with Text Color: Copy This Code`](adding-color-to-text-ranges#Styles-with-Text-Color-Copy-This-Code.md).
2. Paste the code inside your article’s `ArticleDocument.textStyles` object, inside the braces (`{}`).

Your code should look like the example code [`Styles with Text Color: Result`](adding-color-to-text-ranges#Styles-with-Text-Color-Result.md).

###### Styles with Text Color Copy This Code

```json
    "lightGrayText": {
      "textColor": "#A6AAA9"
    },
    "whiteText": {
      "textColor": "#FFF"
    },
    "DINText": {
      "fontName": "DINAlternate-Bold",
      "tracking": 0.01
    },
    "mediumGrayText": {
      "textColor": "#53585F"
    }
```

###### Styles with Text Color Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "textStyles": {
    "lightGrayText": {
      "textColor": "#A6AAA9"
    },
    "whiteText": {
      "textColor": "#FFF"
    },
    "DINText": {
      "fontName": "DINAlternate-Bold",
      "tracking": 0.01
    },
    "mediumGrayText": {
      "textColor": "#53585F"
    }
  },
  ...
}
```

##### Use Text Styles to Change Text Color

Create references to the TextStyle objects you just created.

1. In your `article.json` file, ensure that each of these components has a property named `format` with a value of `"html"`: `title`, `byline`, all four `caption` components, all `body` components, and the first of the two `pullquote` components. See the example code [`Text Color: Result`](adding-color-to-text-ranges#Text-Color-Result.md).
2. Copy the example code [`Title Text: Copy This Code`](adding-color-to-text-ranges#Title-Text-Copy-This-Code.md), and then, inside your `title` component, select the value of the `text` property and paste the copied code, replacing the existing `text` property.
3. Copy the example code [`Byline Text: Copy This Code`](adding-color-to-text-ranges#Byline-Text-Copy-This-Code.md), and then, inside your `byline` component, select the value of the `text` property and paste the copied code, replacing the existing `text` property.
4. Copy the example code [`Floating Caption Text: Copy This Code`](adding-color-to-text-ranges#Floating-Caption-Text-Copy-This-Code.md), and then, inside your first `caption` component, select the value of the `text` property and paste the copied code, replacing the existing `text` property.
5. Copy the example code [`Body Text: Copy This Code`](adding-color-to-text-ranges#Body-Text-Copy-This-Code.md), and then, inside your `body` component that uses the `bodyFirstDropCap` component text style, select the value of the `text` property and paste the copied code, replacing the existing `text` property.
6. Copy the example code [`Pull Quote Text: Copy This Code`](adding-color-to-text-ranges#Pull-Quote-Text-Copy-This-Code.md), and then, inside your `pullquote` component, select the value of the `text` property and paste the copied code, replacing the existing `text` property.
7. Copy the example code [`Gallery Caption Text: Copy This Code`](adding-color-to-text-ranges#Gallery-Caption-Text-Copy-This-Code.md), and then, inside the `caption` component that follows your gallery, select the value of the `text` property and paste the copied code, replacing the existing `text` property.
8. Copy the example code [`Mosaic Caption Text: Copy This Code`](adding-color-to-text-ranges#Mosaic-Caption-Text-Copy-This-Code.md), and then, inside the `caption` component that follows your mosaic, select the value of the `text` property and paste the copied code, replacing the existing `text` property.
9. Copy the example code [`Inset Photo Caption Text: Copy This Code`](adding-color-to-text-ranges#Inset-Photo-Caption-Text-Copy-This-Code.md), and then, inside the `caption` component that accompanies your inset photo, select the value of the `text` property and paste the copied code, replacing the existing `text` property.

Your code should look like the example code [`Text Color: Result`](adding-color-to-text-ranges#Text-Color-Result.md).

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see the text ranges in color.

###### Title Text Copy This Code

```html
"<span data-anf-textstyle='lightGrayText'>ARTICLE TITLE</span> <span data-anf-textstyle='whiteText'>WITH INLINE TEXT STYLE REFERENCES</span>"
```

###### Byline Text Copy This Code

```html
"<span data-anf-textstyle='lightGrayText'>By</span> Urna Semper"
```

###### Floating Caption Text Copy This Code

```html
"<span data-anf-textstyle='DINText'>ABOVE:</span> Sed ut pers piciatis unde omnis iste error sit volup tatem accusa ntium dolor emque, totam rem. (Attribution)"
```

###### Body Text Copy This Code

```html
"<p><span data-anf-textstyle='DINText'>Bold lead-in,</span> cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, dolor repellendus. <a href='http://www.apple.com'>Link text</a> quibusdam et aut.</p><p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, adipisci velit.</p>"
```

###### Pull Quote Text Copy This Code

```html
"“QUIA CONSEQUUNTUR MAGNI DOLORES EOS <span data-anf-textstyle='mediumGrayText'>QUI RATIONE VOLUPTATEM SEQUI NESCIUNT.”</span>"
```

###### Gallery Caption Text Copy This Code

```html
"<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the entire gallery. Individual photos in the gallery also have their own captions. (Shared attribution)"
```

###### Mosaic Caption Text Copy This Code

```html
"<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the entire mosaic. Individual photos in the mosaic also have their own captions. (Shared attribution)"
```

###### Inset Photo Caption Text Copy This Code

```html
"<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the sidebar photo. (Attribution)"
```

###### Text Color Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
   ...
  "components": [
    {
      "role": "section",
      ...
      "components": [
        {
          "role": "header",
          ...
          "components": [
            {
              "role": "container",
              ...
              "components": [
                ...
                {
                  "role": "title",
                  "textStyle": "heading1Light",
                  "format": "html",
                  "layout": "halfMarginBelowLayout",
                  "text": "<span data-anf-textstyle='lightGrayText'>ARTICLE TITLE</span> <span data-anf-textstyle='whiteText'>WITH INLINE TEXT STYLE REFERENCES</span>"
                }
              ]
            }
          ]
        }
      ]
    },
    {
      "role": "section",
      ...
      "components": [
        ...
        {
          "role": "byline",
          "format": "html",
          "layout": "fullMarginBelowLayout",
          "text": "<span data-anf-textstyle='lightGrayText'>By</span> Urna Semper"
        },
        ...
        {
          "role": "container",
          ...
          "components": [
            {
              "role": "caption",
              "format": "html",
              "layout": "fullBleedLayout",
              "text": "<span data-anf-textstyle='DINText'>ABOVE:</span> Sed ut pers piciatis unde omnis iste error sit volup tatem accusa ntium dolor emque, totam rem. (Attribution)"
            }
          ]
        },
        {
          "identifier": "body1",
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "textStyle": "bodyFirstDropCap",
          "text": "<p><span data-anf-textstyle='DINText'>Bold lead-in,</span> cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, dolor repellendus. <a href='http://www.apple.com'>Link text</a> quibusdam et aut.</p><p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, adipisci velit.</p>"
        },
        ...
        {
          "role": "container",
          ...
          "components": [
            {
              "role": "pullquote",
              "format": "html",
              "layout": "halfMarginAboveQuarterBelowContainedLayout",
              "text": "“QUIA CONSEQUUNTUR MAGNI DOLORES EOS <span data-anf-textstyle='mediumGrayText'>QUI RATIONE VOLUPTATEM SEQUI NESCIUNT.”</span>"
            },
            ...
          ]
        },
        ...
        {
          "role": "caption",
          "format": "html",
          "layout": "halfMarginBothLayout",
          "text": "<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the entire gallery. Individual photos in the gallery also have their own captions. (Shared attribution)"
        },
        ...
        {
          "role": "caption",
          "format": "html",
          "layout": "halfMarginBothLayout",
          "text": "<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the entire mosaic. Individual photos in the mosaic also have their own captions. (Shared attribution)"
        },
        ...
            {
              "role": "caption",
              "format": "html",
              "layout": "halfMarginBothContainedLayout",
              "text": "<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the sidebar photo. (Attribution)"
            }
          ]
        },
        ...
      ]
    }
  ],
  ...
}
```

##### Previous

[`Creating an Inset Photo`](creating-an-inset-photo.md)

##### Next

[`Adding Animations`](adding-animations.md)

## See Also

- [Defining and Applying Text Styles](defining-and-applying-text-styles.md)
  Define and apply custom, default, and inline text styles, or use HTML tags or Markdown syntax to style your text.
- [Using HTML with Apple News Format](using-html-with-apple-news-format.md)
  Use HTML formatting for text components.
- [object TextStyle](../applenewsformat/textstyle.md)
  The object for defining the text style, such as font family, size, and color, that you can apply to ranges of text.
- [Creating a Complex, Layered Header](creating-a-complex-layered-header.md)
  Layer a title and heading in front of an image, with their colors optimized for legibility.
- [Creating a Floating Caption](creating-a-floating-caption.md)
  Position a caption in the wide right margin of your article.
- [Creating an Inset Pull Quote](creating-an-inset-pull-quote.md)
  Wrap article body text around an inset pull quote.
- [Creating an Inset Photo](creating-an-inset-photo.md)
  Wrap article body text around an inset photo.
- [Adding Animations](adding-animations.md)
  Use animations to affect how parts of your article come into view the first time they appear.
- [Adding a Scene](adding-a-scene.md)
  Control how the article’s opening section comes into view.
- [Viewing the Finished Article for Advanced Design Tutorial 2](viewing-the-finished-article-for-advanced-design-tutorial-2.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-color-to-text-ranges)*