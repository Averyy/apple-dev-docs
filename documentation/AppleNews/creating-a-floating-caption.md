# Creating a Floating Caption

**Framework**: Apple News

Position a caption in the wide right margin of your article.

#### Overview

Apple News Format makes it easy to create side-by-side content, such as a caption that floats next to the article body. On sufficiently wide displays, News automatically lays out such a caption in the article margin; on narrower displays, News automatically stacks the caption with other article content.

![Screenshot of an Apple News article with a floating caption on iPad.](https://docs-assets.developer.apple.com/published/de1298d6802c3d0b960eb8d673c64d5e/media-3624920%402x.png)

##### Create a Componentlayout Object for the Floating Caption

Before you can position the caption in the right margin, you must define a component layout object that specifies that the caption will begin in column 7 of the article layout and span three columns.

1. Copy the example code [`sideCaptionLayout: Copy This Code`](creating-a-floating-caption#sideCaptionLayout-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentLayout` object and the closing brace for the whole `componentLayouts` property.

Your code should look like the example code [`sideCaptionLayout: Result`](creating-a-floating-caption#sideCaptionLayout-Result.md).

###### Sidecaptionlayout Copy This Code

```json
,
    "sideCaptionLayout": {
      "columnStart": 14,
      "columnSpan": 6,
      "margin": {
        "bottom": 24
      }
    }
```

###### Sidecaptionlayout Result

```json
{
  ...
  "componentLayouts": {
    ...
    "sideCaptionLayout": {
      "columnStart": 14,
      "columnSpan": 6,
      "margin": {
        "bottom": 24
      }
    }
  },
  ...
}
```

##### Anchor the Caption to the Article Body

On wide displays, when you anchor a caption to the article body, the caption’s top edge will be aligned with the body’s top edge; on narrower displays, the caption will be stacked above the body.

1. Delete the `caption` component and its parent container from your header. The code you’re deleting begins with the comma and opening brace (,`{`) before `"role": "container",` and ends with a mix of three alternating braces and brackets, and a comma (`}]}`).
2. Copy the example code [`Caption: Copy This Code`](creating-a-floating-caption#Caption-Copy-This-Code.md).
3. Paste the code inside your article’s second section, before the opening brace (`{`) of the `body` component whose text begins with `Nam libero tempore`.
4. Inside the `body` component whose text begins with `Nam libero tempore`, add an `identifier` property with a value of `"body1"`, as shown in the example code [`Caption: Result`](creating-a-floating-caption#Caption-Result.md).

After you make these changes in your `article.json` file, you can preview your working `article.json` file in News Preview to see the floating caption.

###### Caption Copy This Code

```json
        {
          "role": "container",
          "layout": "sideCaptionLayout",
          "anchor": {
            "targetComponentIdentifier": "body1",
            "targetAnchorPosition": "top",
            "originAnchorPosition": "top"
          },
          "components": [
            {
              "role": "caption",
              "format": "html",
              "layout": "fullBleedLayout",
              "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusa ntium dolor emque, totam rem. (Attribution)"
            }
          ]
        },
```

###### Caption Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    ...
    {
      "role": "section",
      ...
      "components": [
        ...
        {
          "role": "container",
          "layout": "sideCaptionLayout",
          "anchor": {
            "targetComponentIdentifier": "body1",
            "targetAnchorPosition": "top",
            "originAnchorPosition": "top"
          },
          "components": [
            {
              "role": "caption",
              "format": "html",
              "layout": "fullBleedLayout",
              "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusa ntium dolor emque, totam rem. (Attribution)"
            }
          ]
        },
        {
          "identifier": "body1",
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "textStyle": "bodyFirstDropCap",
          "text": "<p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, dolor repellendus. <a href='http://www.apple.com'>Link text</a> quibusdam et aut.</p><p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, adipisci velit.</p>"
        },
        ...
      ]
    }
  ],
  ...
}
```

##### Previous

[`Creating a Complex, Layered Header`](creating-a-complex-layered-header.md)

##### Next

[`Creating an Inset Pull Quote`](creating-an-inset-pull-quote.md)

## See Also

- [Planning the Layout for Your Article](planning-the-layout-for-your-article.md)
  Define a layout that supports the look you want for your article.
- [Positioning the Content in Your Article](positioning-the-content-in-your-article.md)
  Align article components with columns in your layout.
- [Wrapping Text Around a Component](wrapping-text-around-a-component.md)
  Define the layout of a text component to wrap around another component.
- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [object Caption](../applenewsformat/caption.md)
  The component for adding caption text.
- [object Layout](../applenewsformat/layout.md)
  The object for defining columns, gutters, and margins for your article’s designed width.
- [object ComponentLayout](../applenewsformat/componentlayout.md)
  The object for defining the positioning for a specific component within the article’s column system.
- [object Anchor](../applenewsformat/anchor.md)
  The object for anchoring one component to another component in your article’s layout.
- [Creating a Complex, Layered Header](creating-a-complex-layered-header.md)
  Layer a title and heading in front of an image, with their colors optimized for legibility.
- [Creating an Inset Pull Quote](creating-an-inset-pull-quote.md)
  Wrap article body text around an inset pull quote.
- [Creating an Inset Photo](creating-an-inset-photo.md)
  Wrap article body text around an inset photo.
- [Adding Color to Text Ranges](adding-color-to-text-ranges.md)
  Create text in color by using HTML to refer to TextStyle objects.
- [Adding Animations](adding-animations.md)
  Use animations to affect how parts of your article come into view the first time they appear.
- [Adding a Scene](adding-a-scene.md)
  Control how the article’s opening section comes into view.
- [Viewing the Finished Article for Advanced Design Tutorial 2](viewing-the-finished-article-for-advanced-design-tutorial-2.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-a-floating-caption)*