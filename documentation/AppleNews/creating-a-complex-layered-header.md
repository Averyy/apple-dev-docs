# Creating a Complex, Layered Header

**Framework**: Apple News

Layer a title and heading in front of an image, with their colors optimized for legibility.

#### Overview

In the first advanced tutorial, you created a header with layering and parallax behavior.

In this second article, you’ll add more code to the same article to modify the layout. You’ll wrap body text around an image, place captions in the article margin, create a more complex header, and add component animations.

##### Move Title and Heading Text Into the Header

First, you need to layer title and heading information in front of the header’s image fill. You’ll move `heading1`, `divider`, and `title` components from the second section of the article into the `header` component.

This image shows the heading and title before they have been lightened for legibility; you’ll lighten this text in [`Define a Light Text Style for Heading Text`](creating-a-complex-layered-header#Define-a-Light-Text-Style-for-Heading-Text.md).

![Labeled screenshot of an Apple News article on iPhone. The article includes a title and heading layered in front of a header image.](https://docs-assets.developer.apple.com/published/9d7496774f34ed5762b8b96c0fd1c58d/media-3627616%402x.png)

1. Open the `article.json` file that you completed in [`Adding Parallax Behavior`](adding-parallax-behavior.md), or open `Desktop/News_Design_Tutorial/News_Design_Tutorial_Advanced_Article_1/article.json`.
2. In the `article.json` file (not the example code below), cut the first three components inside the second section to your clipboard. The code you are cutting begins with the opening bracket (`{`) before `"role": "heading1",` and ends with the closing bracket and comma  (`},`) that end the `title` component.
3. Paste the components inside the `components` array in your article’s header, after the opening square bracket (`[`) that comes a few lines after this line: `"role": "header",`

Your code should look like the example code [`Moving Components: Result`](creating-a-complex-layered-header#Moving-Components-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see that the title is layered in front of the header as shown in the previous figure.

###### Moving Components Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "behavior": {
        "type": "parallax",
        "factor": 0.8
      },
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
              "role": "heading1",
              "layout": "heading1Layout",
              "text": "HEADING"
            },
            {
              "role": "divider",
              "layout": "bigDividerLayout",
              "stroke": {
                "width": 3,
                "color": "#D5B327"
              }
            },
            {
              "role": "title",
              "layout": "halfMarginBelowLayout",
              "text": "ARTICLE TITLE"
            },
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
        }
      ]
    },
    ...
  ],
  ...
}
```

##### Create More Space Above the Intro Component

When you moved your title in [`Move Title and Heading Text into the Header`](creating-a-complex-layered-header#Move-Title-and-Heading-Text-into-the-Header.md), the spacing around your `intro` component changed. You can use an already defined `ComponentLayout` object to create more space above the `intro` component.

To create additional space, in your `article.json` file, inside the `intro` component, change the value of `layout` from `"halfMarginBelowLayout"` to `"halfMarginBothLayout"`.

Your code should look like the example code [`Intro ComponentLayout Object: Result`](creating-a-complex-layered-header#Intro-ComponentLayout-Object-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see the adjustment to the `intro` component’s position.

###### Intro Componentlayout Object Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "behavior": {
        "type": "parallax",
        "factor": 0.8
      },
      "components": [
        ...
      ]
    },
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "style": "bodyBackgroundStyle",
      "components": [
        {
          "role": "intro",
          "layout": "halfMarginBothLayout",
          "text": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque ipsum?"
        },
        ...
      ]
    }
  ],
  ...
}
```

##### Anchor the Title to the Bottom of the Header

If you anchor multiple child components to the same side of the parent, the children will stack as in the following figure. This image shows the heading and title before they have been lightened for legibility; you’ll lighten this text in [`Use the Dark Background and Light Text`](creating-a-complex-layered-header#Use-the-Dark-Background-and-Light-Text.md).

![Labeled screenshot of an Apple News article on iPhone. The article includes a title and heading within a container that is layered in front of a header image and anchored to the bottom of the header.](https://docs-assets.developer.apple.com/published/51d2ea8846887297dd5d44fb57995ed1/media-3627615%402x.png)

1. In your working `article.json` file, delete the contents of the `components` array inside your `header` component.
2. Copy the example code [`Header Contents: Copy This Code`](creating-a-complex-layered-header#Header-Contents-Copy-This-Code.md).
3. Paste the code inside the now-empty `components` array of the header, where you deleted content in step 1. Make sure to paste inside the square brackets (`[]`).

Your code should look like the example code [`Header Contents: Result`](creating-a-complex-layered-header#Header-Contents-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see that the article title information is anchored to the bottom of the header.

###### Header Contents Copy This Code

```json
            {
              "role": "container",
              "layout": "fullBleedLayout",
              "anchor": {
                "targetAnchorPosition": "bottom"
              },
              "components": [
                {
                  "role": "heading1",
                  "layout": "heading1Layout",
                  "text": "HEADING"
                },
                {
                  "role": "divider",
                  "layout": "bigDividerLayout",
                  "stroke": {
                    "width": 3,
                    "color": "#D5B327"
                  }
                },
                {
                  "role": "title",
                  "format": "html",
                  "layout": "halfMarginBelowLayout",
                  "text": "ARTICLE TITLE"
                }
              ]
            },
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
```

###### Header Contents Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "behavior": {
        "type": "parallax",
        "factor": 0.8
      },
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
              "anchor": {
                "targetAnchorPosition": "bottom"
              },
              "components": [
                {
                  "role": "heading1",
                  "layout": "heading1Layout",
                  "text": "HEADING"
                },
                {
                  "role": "divider",
                  "layout": "bigDividerLayout",
                  "stroke": {
                    "width": 3,
                    "color": "#D5B327"
                  }
                },
                {
                  "role": "title",
                  "format": "html",
                  "layout": "halfMarginBelowLayout",
                  "text": "ARTICLE TITLE"
                }
              ]
            },
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
        }
      ]
    },
    ...
  ],
  ...
}
```

##### Define a Dark Background for the Title and Heading

To add contrast to your title and heading text, you can adjust the text color and the background of the text’s parent container. You’ll set the title container background to a gradient that fades from transparent at the top to black at the bottom.

![Labeled screenshot of an Apple News article on iPhone. The article includes a title and heading within a container with a contrasting background color. The container is layered in front of a header image and anchored to the bottom of the header.](https://docs-assets.developer.apple.com/published/f1adea1dac5ef77a9e4c17c361f42377/media-3627614%402x.png)

1. Copy the example code [`scrimBackgroundStyle: Copy This Code`](creating-a-complex-layered-header#scrimBackgroundStyle-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentStyle` object and the closing brace for the whole `componentStyles` property.

Your code should look like the example code [`scrimBackgroundStyle: Result`](creating-a-complex-layered-header#scrimBackgroundStyle-Result.md).

###### Scrimbackgroundstyle Copy This Code

```json
,
    "scrimBackgroundStyle": {
      "fill": {
        "type": "linear_gradient",
        "colorStops": [
          {
            "color": "#00000000"
          },
          {
            "color": "#00000090"
          }
        ]
      }
    }
```

###### Scrimbackgroundstyle Result

```json
{
  ...
  "componentStyles": {
    ...
    "scrimBackgroundStyle": {
      "fill": {
        "type": "linear_gradient",
        "colorStops": [
          {
            "color": "#00000000"
          },
          {
            "color": "#00000090"
          }
        ]
      }
    }
  },
  ...
}
```

##### Define a Light Text Style for Heading Text

Before you can lighten the text of the heading, you must define a new `ComponentTextStyle` object.

1. Copy the example code [`heading1Light: Copy This Code`](creating-a-complex-layered-header#heading1Light-Copy-This-Code.md).
2. Paste the code inside the `ArticleDocument.componentTextStyles` object in your `article.json` file, after the closing brace (`}`) of the last `ComponentTextStyle` object and before the closing brace for the whole `componentTextStyles` property.

Your code should look like the example code [`heading1Light: Result`](creating-a-complex-layered-header#heading1Light-Result.md).

###### Heading1light Copy This Code

```json
,
    "heading1Light": {
      "textColor": "#FFF"
    }
```

###### Heading1light Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentTextStyles": {
    ...
    "heading1Light": {
      "textColor": "#FFF"
    }
  }
  ...
}

```

##### Use the Dark Background and Light Text

Now you can add references to the `scrimBackgroundStyle` and `heading1Light` objects.

1. In your `article.json` file, inside the `header` component’s child container, add a property named `style` with a value of `"scrimBackgroundStyle"`, as in the example code [`Dark Background and Light Text: Result`](creating-a-complex-layered-header#Dark-Background-and-Light-Text-Result.md).
2. In your `article.json file`, inside both the `heading1` component and the `title` component, add a property named `textStyle` with a value of `"heading1Light"`, as in the example code [`Dark Background and Light Text: Result`](creating-a-complex-layered-header#Dark-Background-and-Light-Text-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see the optimized styling of your header.

###### Dark Background and Light Text Result

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
          },
          "components": [
            {
              "role": "container",
              "layout": "fullBleedLayout",
              "style": "scrimBackgroundStyle",
              "anchor": {
                "targetAnchorPosition": "bottom"
              },
              "components": [
                {
                  "role": "heading1",
                  "textStyle": "heading1Light",
                  "layout": "heading1Layout",
                  "text": "HEADING"
                },
                {
                  "role": "divider",
                  "layout": "bigDividerLayout",
                  "stroke": {
                    "width": 3,
                    "color": "#D5B327"
                  }
                },
                {
                  "role": "title",
                  "textStyle": "heading1Light",
                  "format": "html",
                  "layout": "halfMarginBelowLayout",
                  "text": "ARTICLE TITLE"
                }
              ]
            },
            ...
          ]
        }
      ]
    },
    ...
  ],
  ...
}
```

##### Previous

[`Viewing the Finished Article for Advanced Design Tutorial 1`](viewing-the-finished-article-for-advanced-design-tutorial-1.md)

##### Next

[`Creating a Floating Caption`](creating-a-floating-caption.md)

## See Also

- [Positioning the Content in Your Article](positioning-the-content-in-your-article.md)
  Align article components with columns in your layout.
- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [Applying a Background to a Component](applying-a-background-to-a-component.md)
  Change the appearance of the backgrounds in your article.
- [Defining and Applying Text Styles](defining-and-applying-text-styles.md)
  Define and apply custom, default, and inline text styles, or use HTML tags or Markdown syntax to style your text.
- [object Header](../applenewsformat/header.md)
  The component for defining the top area of an article, chapter, or section.
- [object LinearGradientFill](../applenewsformat/lineargradientfill.md)
  The object for displaying a linear gradient as a component background.
- [object ComponentLayout](../applenewsformat/componentlayout.md)
  The object for defining the positioning for a specific component within the article’s column system.
- [object ComponentTextStyle](../applenewsformat/componenttextstyle.md)
  The object for defining the style for a text component, including spacing, alignment, and drop caps.
- [object ComponentStyle](../applenewsformat/componentstyle.md)
  The object for setting style properties for components, including background color and fill, borders, and table styles.
- [Creating a Floating Caption](creating-a-floating-caption.md)
  Position a caption in the wide right margin of your article.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-a-complex-layered-header)*