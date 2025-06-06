# Adding a Fixed Image Fill

**Framework**: Apple News

Add an image that remains stationary when the user scrolls.

#### Overview

The fixed image fill is one of the most captivating effects in Apple News Format. A fixed image fill stays still when the user scrolls. As long as any portion of the filled component is visible in the viewport, the image maintains one position, while the rest of the article seems to scroll independently of the image.

![Screenshot of an Apple News article with a fixed image fill on iPad.](https://docs-assets.developer.apple.com/published/a9c06288356c7a5ed7d63b9bdd6e2ac3/media-3624928%402x.png)

##### Create a Componentlayout Object for the Fixed Image

Before you can make the image span the whole display area, you must create a new `ComponentLayout` object.

1. Copy the example code [`fullScreenImageLayout: Copy This Code`](adding-a-fixed-image-fill#fullScreenImageLayout-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentLayout` object and the closing brace for the whole `componentLayouts` property.

Your code should look like the example code [`fullScreenImageLayout: Result`](adding-a-fixed-image-fill#fullScreenImageLayout-Result.md).

###### Fullscreenimagelayout Copy This Code

```json
,
    "fullScreenImageLayout": {
      "ignoreDocumentMargin": true,
      "minimumHeight": "100vmax",
      "margin": {
        "top": 24,
        "bottom": 12
      }
    }
```

###### Fullscreenimagelayout Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentLayouts": {
    ...
    "fullScreenImageLayout": {
      "ignoreDocumentMargin": true,
      "minimumHeight": "100vmax",
      "margin": {
        "top": 24,
        "bottom": 12
      }
    }
  },
...
}
```

##### Create a Componenttextstyle Object for the Pull Quote

Create a new `ComponentTextStyle` object for a new color.

1. Copy the example code [`pullquoteLight: Copy This Code`](adding-a-fixed-image-fill#pullquoteLight-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentTextStyle` object and the closing brace for the whole `componentTextStyles` property.

Your code should look like the example code [`pullquoteLight: Result`](adding-a-fixed-image-fill#pullquoteLight-Result.md).

###### Pullquotelight Copy This Code

```json
,
    "pullquoteLight": {
      "textColor": "#F5F9FB"
    }
```

###### Pullquotelight Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentTextStyles": {
    ...
    "pullquoteLight": {
      "textColor": "#F5F9FB"
    }
  }
...
}
```

##### Add a New Container with a Fixed Image Fill

In [`Download the Article Bundle Examples`](setting-up-the-advanced-tutorials#Download-the-Article-Bundle-Examples.md), you downloaded a bundle called `News_Design_Tutorial_Advanced_Article_3` that contains a thumbnail image. Now, you’ll move that image into your working folder and use it as an image fill.

1. Move the `static-background.jpg` file from the `News_Design_Tutorial_Advanced_Article_3` folder to the folder that contains your working `article.json` file.
2. Copy the example code [`Fixed Image Fill: Copy This Code`](adding-a-fixed-image-fill#Fixed-Image-Fill-Copy-This-Code.md).
3. Paste the code inside your second section, near the end, before this code: `{ "role": tweet,`

Your code should look like the example code [`Fixed Image Fill: Result`](adding-a-fixed-image-fill#Fixed-Image-Fill-Result.md).

###### Fixed Image Fill Copy This Code

```json
        {
          "role": "container",
          "layout": "fullScreenImageLayout",
          "style": {
            "fill": {
              "type": "image",
              "URL": "bundle://static-background.jpg",
              "fillMode": "cover",
              "attachment": "fixed",
              "verticalAlignment": "center",
              "horizontalAlignment": "center"
            }
          },
          "components": [
            {
              "role": "pullquote",
              "layout": "fullMarginBelowLayout",
              "textStyle": "pullquoteLight",
              "text": "“QUIA CONSEQUUNTUR MAGNI DOLORES EOS QUI RATIONE VOLUPTATEM SEQUI NESCIUNT.”",
              "anchor": {
                "targetAnchorPosition": "center"
              }
            }
          ]
        },
```

###### Fixed Image Fill Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    ...
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "style": "bodyBackgroundStyle",
      "components": [
        ...
        {
          "role": "container",
          "layout": "fullScreenImageLayout",
          "style": {
            "fill": {
              "type": "image",
              "URL": "bundle://static-background.jpg",
              "fillMode": "cover",
              "attachment": "fixed",
              "verticalAlignment": "center",
              "horizontalAlignment": "center"
            }
          },
          "components": [
            {
              "role": "pullquote",
              "layout": "fullMarginBelowLayout",
              "textStyle": "pullquoteLight",
              "text": "“QUIA CONSEQUUNTUR MAGNI DOLORES EOS QUI RATIONE VOLUPTATEM SEQUI NESCIUNT.”",
              "anchor": {
                "targetAnchorPosition": "center"
              }
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

[`Creating a Sidebar`](creating-a-sidebar.md)

##### Next

[`Creating a Newsletter Sign-Up Element`](creating-a-newsletter-sign-up-element.md)

## See Also

- [object ImageFill](../applenewsformat/imagefill.md)
  The object for adding an image background fill to a component.
- [Specifying Measurements for Components](specifying-measurements-for-components.md)
  Specify the units of measure to use for margins, minimum heights, and other dimensions.
- [Giving the Article a Dark Color Scheme](giving-the-article-a-dark-color-scheme.md)
  Apply a new color scheme to your article.
- [Adding a Video](adding-a-video.md)
  Add a video component inside the header component.
- [Creating a Sidebar](creating-a-sidebar.md)
  Create a box with an HTML bulleted list in the margin.
- [Creating a Newsletter Sign-Up Element](creating-a-newsletter-sign-up-element.md)
  Add a newsletter sign-up element in your article.
- [Viewing the Finished Article for Advanced Design Tutorial 3](viewing-the-finished-article-for-advanced-design-tutorial-3.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-a-fixed-image-fill)*