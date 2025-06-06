# Creating a Layered Header

**Framework**: Apple News

Create a header with a caption that’s layered in front of an image.

#### Overview

In [`Setting Up the Advanced Tutorials`](setting-up-the-advanced-tutorials.md), you learned how to download some article bundles, including one called `News_Design_Tutorial_6_Embeds.zip`, which represents the outcome of the introductory tutorial.

##### Replace a Captioned Photo with an Image Fill

An image fill is an image that is set as the background fill of a component. When you use an image fill, any other content in the component looks like it is layered in front of the image. This allows you to create collage effects and other layering effects.

In these steps, you’ll:

- Add a header with an image fill to your article code.
- Use a `fillMode` property with a value of `cover` to ensure that the image covers the entire `header` component while maintaining the image aspect ratio.
- Ensure that the bottom rather than the top edge of the image gets cropped, by using the `verticalAlignment` property to align the top edge of the image to the top edge of the `header` component.
- Remove a captioned photo from your article code.

To replace a captioned photo with an image fill:

1. Open the `article.json` file that you completed in [`Adding a Podcast`](adding-a-podcast.md), or open `Desktop/News_Design_Tutorial/News_Design_Tutorial_6_Embeds/article.json`.
2. Copy the example code [`Header and Caption: Copy This Code`](creating-a-layered-header#Header-and-Caption-Copy-This-Code.md).
3. Paste the code inside the `components` array in your `article.json` file, after the opening bracket (`[`). Previewing your article won’t work temporarily, because it includes a reference to a nonexistent `headerImageLayout` object. You’ll define this `ComponentLayout` object in [`Define a ComponentLayout Object for Headers`](creating-a-layered-header#Define-a-ComponentLayout-Object-for-Headers.md)
4. In your `article.json` file, delete the `photo` component and the `caption` component that follows it, beginning with the opening brace (`{`) before `"role": "photo"` and ending with a closing brace and comma (`},`).

Your code should look like the example code [`Header and Caption: Result`](creating-a-layered-header#Header-and-Caption-Result.md).

###### Header and Caption Copy This Code

```json
    {
      "role": "header",
      "layout": "headerImageLayout",
      "style": {
        "fill": {
          "type": "image",
          "URL": "bundle://header.jpg",
          "fillMode": "cover",
          "verticalAlignment": "top",
          "horizontalAlignment": "center"
        }
      }
    },
    {
      "role": "caption",
      "layout": "halfMarginBothLayout",
      "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusantium dolor emque, totam rem. (Attribution)"
    },
```

###### Header and Caption Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "header",
      "layout": "headerImageLayout",
      "style": {
        "fill": {
          "type": "image",
          "URL": "bundle://header.jpg",
          "fillMode": "cover",
          "verticalAlignment": "top",
          "horizontalAlignment": "center"
        }
      }
    },
    {
      "role": "caption",
      "layout": "halfMarginBothLayout",
      "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusantium dolor emque, totam rem. (Attribution)"
    },
    ...
  ],
  ...
}
```

##### Define a Componentlayout Object for Headers

In [`Replace a Captioned Photo with an Image Fill`](creating-a-layered-header#Replace-a-Captioned-Photo-with-an-Image-Fill.md), you added a reference to an undefined `ComponentLayout` object. Now, you’ll define that `ComponentLayout` object. You’ll make the `ComponentLayout` object extend to both sides of the display, and you’ll give it a height that is 44 percent of the viewport’s longest side.

1. Copy the example code [`headerImageLayout: Copy This Code`](creating-a-layered-header#headerImageLayout-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentLayout` object and the closing brace for the whole `componentLayouts` property.

Your code should look like the example code [`headerImageLayout: Result`](creating-a-layered-header#headerImageLayout-Result.md).

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see the header with the image fill. The caption is still below the header. In [`Move a Caption Inside a Header`](creating-a-layered-header#Move-a-Caption-Inside-a-Header.md), you’ll layer the caption in front of the header.

###### Headerimagelayout Copy This Code

```json
,
    "headerImageLayout": {
      "ignoreDocumentMargin": true,
      "minimumHeight": "44vmax"
    }
```

###### Headerimagelayout Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentLayouts": {
    ...
    "headerImageLayout": {
      "ignoreDocumentMargin": true,
      "minimumHeight": "44vmax"
    }
  },
  ...
}
```

##### Move a Caption Inside a Header

In [`Replace a Captioned Photo with an Image Fill`](creating-a-layered-header#Replace-a-Captioned-Photo-with-an-Image-Fill.md), you added a `header` component to your article. Now, you’ll move a `caption` component so that it’s a child of that header. This creates a layering effect.

![Labeled screenshot of an Apple News article on iPhone. The article includes a header with an image fill and a child caption.](https://docs-assets.developer.apple.com/published/2bd3a52f4c070d4a5833f473a471fe4f/media-3624527%402x.png)

1. In your `article.json` file, delete the first `caption` component. The code you are deleting begins with the opening brace (`{`) before `"role": "caption",` and ends with a closing brace and comma (`},`). This is the caption that you pasted in [`Replace a Captioned Photo with an Image Fill`](creating-a-layered-header#Replace-a-Captioned-Photo-with-an-Image-Fill.md).
2. Copy the example code [`Child Components: Copy This Code`](creating-a-layered-header#Child-Components-Copy-This-Code.md).
3. Paste the code inside the `header` component, after the two closing braces (`}}`) for the `fill` and `style` properties and before the third closing brace that ends the whole `header` component.

Your code should look like the example code [`Child Components: Result`](creating-a-layered-header#Child-Components-Result.md).

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see that the caption is layered in front of the header image.

###### Child Components Copy This Code

```json
,
      "components": [
        {
          "role": "caption",
          "layout": "halfMarginBothLayout",
          "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusantium dolor emque, totam rem. (Attribution)"
        }
      ]
```

###### Child Components Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "header",
      "layout": "headerImageLayout",
      "style": {
        "fill": {
          "type": "image",
          "URL": "bundle://header.jpg",
          "fillMode": "cover",
          "verticalAlignment": "top",
          "horizontalAlignment": "center"
        }
      },
      "components": [
        {
          "role": "caption",
          "layout": "halfMarginBothLayout",
          "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusantium dolor emque, totam rem. (Attribution)"
        }
      ]
    },
    ...
  ],
  ...
}
```

##### Define a Dark Background for the Caption

In [`Move a Caption Inside a Header`](creating-a-layered-header#Move-a-Caption-Inside-a-Header.md), you layered a caption in front of your header, but the caption that you moved is now difficult to read. Before you can give your container a darker background, you must define a new `ComponentStyle` object.

1. Copy the example code [`captionBarBackgroundStyle: Copy This Code`](creating-a-layered-header#captionBarBackgroundStyle-Copy-This-Code.md).
2. Paste the code inside your article’s `ArticleDocument.componentStyles` object, inside the braces (`{}`).

Your code should look like the example code [`captionBarBackgroundStyle: Result`](creating-a-layered-header#captionBarBackgroundStyle-Result.md).

###### Captionbarbackgroundstyle Copy This Code

```json
    "captionBarBackgroundStyle": {
      "backgroundColor": "#000"
    }
```

###### Captionbarbackgroundstyle Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentStyles": {
    "captionBarBackgroundStyle": {
      "backgroundColor": "#000"
    }
  },
  ...
}
```

##### Define a Light Text Color for the Caption

Before you can lighten the text of the caption, you must define a new `ComponentTextStyle` object.

1. Copy the example code [`captionLight: Copy This Code`](creating-a-layered-header#captionLight-Copy-This-Code.md).
2. Paste the code inside the `ArticleDocument.componentTextStyles` object, after the closing brace (`}`) of the last component text style and before the closing brace for the whole `componentTextStyles` property.

Your code should look like the example code [`captionLight: Result`](creating-a-layered-header#captionLight-Result.md).

###### Captionlight Copy This Code

```json
,
    "captionLight": {
      "textColor": "#FFF"
    }
```

###### Captionlight Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentTextStyles": {
    ...
    "captionLight": {
      "textColor": "#FFF"
    }
  }
  ...
}
```

##### Use the Caption Background Color Text Color and Layout

To make your caption easier to read, apply the styles that you added in [`Define a Dark Background for the Caption`](creating-a-layered-header#Define-a-Dark-Background-for-the-Caption.md) and [`Define a Light Text Color for the Caption`](creating-a-layered-header#Define-a-Light-Text-Color-for-the-Caption.md). Adjust the position of the caption using the `ComponentLayout` object `headerImageLayout` that you created earlier in [`Define a ComponentLayout Object for Headers`](creating-a-layered-header#Define-a-ComponentLayout-Object-for-Headers.md). Because your `caption` component is in a container, you can adjust its position without affecting the parent container.

![Labeled screenshot of an Apple News article on iPhone. The article includes a child caption that has a background color.](https://docs-assets.developer.apple.com/published/dbf492862edd0b65d7eaee767bb21b73/media-3624525%402x.png)

1. In your `article.json` file, delete the first `caption` component. The code you are deleting begins with the opening brace (`{`) before `"role": "caption",` and ends with a closing brace (`}`). This is the caption that you pasted in [`Move a Caption Inside a Header`](creating-a-layered-header#Move-a-Caption-Inside-a-Header.md).
2. Copy the example code [`Container and Caption: Copy This Code`](creating-a-layered-header#Container-and-Caption-Copy-This-Code.md).
3. Paste the code in the now-empty `components` array of the header, where you deleted content in step 1. Make sure to paste inside the brackets (`[]`).

Your code should look like the example code [`Container and Caption: Result`](creating-a-layered-header#Container-and-Caption-Result.md).

###### Container and Caption Copy This Code

```json
        {
          "role": "container",
          "layout": "fullBleedLayout",
          "style": "captionBarBackgroundStyle",
          "components": [
            {
              "role": "caption",
              "textStyle": "captionLight",
              "layout": "halfMarginBothLayout",
              "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusantium dolor emque, totam rem. (Attribution)"
            }
          ]
        }
```

###### Container and Caption Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "header",
      "layout": "headerImageLayout",
      "style": {
        "fill": {
          "type": "image",
          "URL": "bundle://header.jpg",
          "fillMode": "cover",
          "verticalAlignment": "top",
          "horizontalAlignment": "center"
        }
      },
      "components": [
        {
          "role": "container",
          "layout": "fullBleedLayout",
          "style": "captionBarBackgroundStyle",
          "components": [
            {
              "role": "caption",
              "textStyle": "captionLight",
              "layout": "halfMarginBothLayout",
              "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusantium dolor emque, totam rem. (Attribution)"
            }
          ]
        }
      ]
    },
    ...
  ],
  ...
}
```

##### Anchor the Caption to the Bottom of the Header

The final step in creating your layered header is to anchor the caption to the bottom of the header by adding an `anchor` property to the `container` component.

![Labeled screenshot of an Apple News article on iPhone. The article includes a child caption anchored to the bottom of the header.](https://docs-assets.developer.apple.com/published/71ccc4f4c5aa67d441fda98284e5f293/media-3624526%402x.png)

1. Copy the example code [`Anchor: Copy This Code`](creating-a-layered-header#Anchor-Copy-This-Code.md).
2. Paste the code inside the `container` component, after the line `"style": "captionBarBackgroundStyle",`

Your code should look like the example code [`Anchor: Result`](creating-a-layered-header#Anchor-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see that the caption is anchored to the bottom of the header.

###### Anchor Copy This Code

```json
          "anchor": {
            "targetAnchorPosition": "bottom"
          },
```

###### Anchor Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "header",
      "layout": "headerImageLayout",
      "style": {
        "fill": {
          "type": "image",
          "URL": "bundle://header.jpg",
          "fillMode": "cover",
          "verticalAlignment": "top",
          "horizontalAlignment": "center"
        }
      },
      "components": [
        {
          "role": "container",
          "layout": "fullBleedLayout",
          "style": "captionBarBackgroundStyle",
          "anchor": {
            "targetAnchorPosition": "bottom"
          },
          "components": [
            {
              "role": "caption",
              "textStyle": "captionLight",
              "layout": "halfMarginBothLayout",
              "text": "ABOVE: Sed ut pers piciatis unde omnis iste error sit volup tatem accusantium dolor emque, totam rem. (Attribution)"
            }
          ]
        }
      ]
    },
    ...
  ],
  ...
}
```

##### Next

[`Adding Parallax Behavior`](adding-parallax-behavior.md)

## See Also

- [Applying a Background to a Component](applying-a-background-to-a-component.md)
  Change the appearance of the backgrounds in your article.
- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Defining and Applying Text Styles](defining-and-applying-text-styles.md)
  Define and apply custom, default, and inline text styles, or use HTML tags or Markdown syntax to style your text.
- [object Anchor](../applenewsformat/anchor.md)
  The object for anchoring one component to another component in your article’s layout.
- [object Header](../applenewsformat/header.md)
  The component for defining the top area of an article, chapter, or section.
- [object Container](../applenewsformat/container.md)
  Properties shared by all container types.
- [object Caption](../applenewsformat/caption.md)
  The component for adding caption text.
- [object CaptionDescriptor](../applenewsformat/captiondescriptor.md)
  The object you use in image components for displaying captions when the image is full-screen.
- [object ComponentStyle](../applenewsformat/componentstyle.md)
  The object for setting style properties for components, including background color and fill, borders, and table styles.
- [object ImageFill](../applenewsformat/imagefill.md)
  The object for adding an image background fill to a component.
- [object ComponentTextStyle](../applenewsformat/componenttextstyle.md)
  The object for defining the style for a text component, including spacing, alignment, and drop caps.
- [Specifying Measurements for Components](specifying-measurements-for-components.md)
  Specify the units of measure to use for margins, minimum heights, and other dimensions.
- [Setting Up the Advanced Tutorials](setting-up-the-advanced-tutorials.md)
  Download the tutorial files, and learn about what you’ll create in the three advanced tutorials.
- [About Containers](about-containers.md)
  Learn the basic Apple News Format container concepts required for the three advanced tutorials.
- [Adding Parallax Behavior](adding-parallax-behavior.md)
  Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.
- [Viewing the Finished Article for Advanced Design Tutorial 1](viewing-the-finished-article-for-advanced-design-tutorial-1.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-a-layered-header)*