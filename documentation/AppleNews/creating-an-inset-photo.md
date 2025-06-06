# Creating an Inset Photo

**Framework**: Apple News

Wrap article body text around an inset photo.

#### Overview

In [`Creating an Inset Pull Quote`](creating-an-inset-pull-quote.md), you placed a pull quote within the article body.

- Place a photo within the article body.
- Use a `ComponentLayout` object to control horizontal placement in the column system.
- Add an anchor to control vertical placement and make text wrap around the photo.

![Screenshot of an Apple News article with an inset photo on iPad.](https://docs-assets.developer.apple.com/published/48fe5e55e2f466580a8aa774cf4cc857/media-3624923%402x.png)

##### Define Componentlayout Objects for an Inset Photo

Before you can position the photo inside the article body, you must define some new `ComponentLayout` objects for this example. The `smallImageLayout` object determines that the pull quote container gets laid out in the rightmost three columns of the article text. The other two `ComponentLayout` objects make minor vertical adjustments.

1. Copy the example code [`Inset Photo Layout: Copy This Code`](creating-an-inset-photo#Inset-Photo-Layout-Copy-This-Code.md).
2. Paste the code between the closing brace (}) of the last `ComponentLayout` object and the closing brace for the whole `componentLayouts` property.

Your code should look like the example code [`Inset Photo Layout: Result`](creating-an-inset-photo#Inset-Photo-Layout-Result.md).

###### Inset Photo Layout Copy This Code

```json
,
    "smallImageLayout": {
      "columnStart": 8,
      "columnSpan": 6
    },
    "halfMarginAboveContainedLayout": {
      "margin": {
        "top": 12
      }
    },
    "halfMarginBothContainedLayout": {
      "margin": {
        "top": 12,
        "bottom": 12
      }
    }
```

###### Inset Photo Layout Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentLayouts": {
    ...
    "smallImageLayout": {
      "columnStart": 8,
      "columnSpan": 6
    },
    "halfMarginAboveContainedLayout": {
      "margin": {
        "top": 12
      }
    },
    "halfMarginBothContainedLayout": {
      "margin": {
        "top": 12,
        "bottom": 12
      }
    }
  },
  ...
}
```

##### Define a Bottom Border

Before you can add a bottom border to the inset photo, you must define a `ComponentStyle` object that creates a bottom border only.

1. Copy the example code [`captionLockupStyle: Copy This Code`](creating-an-inset-photo#captionLockupStyle-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentStyle` object and the closing brace for the whole `componentStyles` property.

Your code should look like the example code [`captionLockupStyle: Result`](creating-an-inset-photo#captionLockupStyle-Result.md).

###### Captionlockupstyle Copy This Code

```json
,
    "captionLockupStyle": {
      "border": {
        "all": {
          "width": 1,
          "color": "#D5B327"
        },
        "top": false,
        "right": false,
        "bottom": true,
        "left": false
      }
    }
```

###### Captionlockupstyle Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentStyles": {
    ...
    "captionLockupStyle": {
      "border": {
        "all": {
          "width": 1,
          "color": "#D5B327"
        },
        "top": false,
        "right": false,
        "bottom": true,
        "left": false
      }
    }
  },
  ...
}
```

##### Use Style and Layout and Wrap Text Around a Container

In Download the Article Bundle Examples, you downloaded a bundle called `News_Design_Tutorial_Advanced_Article_2` that contains a sidebar image. Now, you’ll move that image into your working folder and create a photo component to display the image.

1. Move the `sidebar.jpg` file from `Desktop/News_Design_Tutorial_Advanced/News_Design_Tutorial_Advanced_Article_2` folder to your working article directory. This directory is most likely `Desktop/News_Design_Tutorial_Advanced/News_Design_Tutorial_6_Embeds` or `Desktop/News_Design_Tutorial_Advanced/News_Design_Tutorial_Advanced_Article_1`.
2. Copy the example code [`Container: Copy This Code`](creating-an-inset-photo#Container-Copy-This-Code.md).
3. Paste the code before the opening brace (`{`) of the body component whose text begins with `Consequatur aut doloribus`.
4. Copy the code `<a id='a1' />`
5. Paste the code in the `body` component whose text begins with `Consequatur aut doloribus`, as in the example code [`Container: Result`](creating-an-inset-photo#Container-Result.md). You may have to scroll to the right in the example code to see this.

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see the inset photo.

###### Container Copy This Code

```json
        {
          "role": "container",
          "layout": "smallImageLayout",
          "style": "captionLockupStyle",
          "anchor": {
            "targetAnchorPosition": "top",
            "originAnchorPosition": "top",
            "target": "a1"
          },
          "components": [
            {
              "role": "photo",
              "layout": "noMarginLayout",
              "URL": "bundle://sidebar.jpg",
              "caption": "A caption for the sidebar photo."
            },
            {
              "role": "caption",
              "format": "html",
              "layout": "halfMarginBothContainedLayout",
              "text": "ABOVE: A caption for the sidebar photo. (Attribution)"
            }
          ]
        },
```

###### Container Result

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
          "layout": "smallImageLayout",
          "style": "captionLockupStyle",
          "anchor": {
            "targetAnchorPosition": "center",
            "target": "a1"
          },
          "components": [
            {
              "role": "photo",
              "layout": "halfMarginAboveContainedLayout",
              "URL": "bundle://sidebar.jpg",
              "caption": "A caption for the sidebar photo."
            },
            {
              "role": "caption",
              "format": "html",
              "layout": "halfMarginBothContainedLayout",
              "text": "ABOVE: A caption for the sidebar photo. (Attribution)"
            }
          ]
        },
        {
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "text": "<p>Consequatur aut doloribus asperiores repellat. Sed ut perspiciatis unde omnis iste natus error sit volup tatem accusantium doloremque laudantium, totam rem, eaque ipsa quae ab illo inventore veritatis et quasi archit ecto beatae vitae.</p><p>Nemo enim ipsam volup tatem quia voluptas sit aspernatur aut odit aut fugit, sed quia conse quuntur magni. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt <a id='a1' />ut labore et dolore aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam.</p><p>Consequatur aut perferendis doloribus asperiores repellat. Sed ut perspiciatis unde omnis iste natus error sit volup tatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi archit ecto beatae vitae dicta. Nemo enim ipsam volup tatem quia voluptas sit <a href='http://www.apple.com'>link text</a> aut odit aut fugit, sed quia conse quuntur perspiciatis doloribus magni dolores.</p><p>Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam suscipit laboriosam.</p>"
        },
        ...
      ]
    }
  ],
  ...
}
```

##### Previous

[`Creating an Inset Pull Quote`](creating-an-inset-pull-quote.md)

##### Next

[`Adding Color to Text Ranges`](adding-color-to-text-ranges.md)

## See Also

- [Positioning the Content in Your Article](positioning-the-content-in-your-article.md)
  Align article components with columns in your layout.
- [Wrapping Text Around a Component](wrapping-text-around-a-component.md)
  Define the layout of a text component to wrap around another component.
- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [object Photo](../applenewsformat/photo.md)
  The component for including a photograph.
- [object Container](../applenewsformat/container.md)
  Properties shared by all container types.
- [object Anchor](../applenewsformat/anchor.md)
  The object for anchoring one component to another component in your article’s layout.
- [object Border](../applenewsformat/border.md)
  The object for setting borders for component sides or tables.
- [Creating a Complex, Layered Header](creating-a-complex-layered-header.md)
  Layer a title and heading in front of an image, with their colors optimized for legibility.
- [Creating a Floating Caption](creating-a-floating-caption.md)
  Position a caption in the wide right margin of your article.
- [Creating an Inset Pull Quote](creating-an-inset-pull-quote.md)
  Wrap article body text around an inset pull quote.
- [Adding Color to Text Ranges](adding-color-to-text-ranges.md)
  Create text in color by using HTML to refer to TextStyle objects.
- [Adding Animations](adding-animations.md)
  Use animations to affect how parts of your article come into view the first time they appear.
- [Adding a Scene](adding-a-scene.md)
  Control how the article’s opening section comes into view.
- [Viewing the Finished Article for Advanced Design Tutorial 2](viewing-the-finished-article-for-advanced-design-tutorial-2.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-an-inset-photo)*