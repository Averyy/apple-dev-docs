# Adding Parallax Behavior

**Framework**: Apple News

Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.

#### Overview

You’ll first divide the article’s components into two sections. This requires moving a large amount of code. Then, you’ll simply add a `behavior` property on the upper section and complete the effect by giving the lower section an opaque background color.

![Labeled screenshot of an Apple News article with two sections on iPad.](https://docs-assets.developer.apple.com/published/b5bb58096aa72b0f4afa853d04e33f36/media-3624566%402x.png)

![Side-by-side screenshots of an Apple News article on iPhone. The left image shows the article before scrolling, and the right image shows the effect of scrolling with parallax behavior.](https://docs-assets.developer.apple.com/published/4472e10eba3a1d70a13dc32668dc5f0e/media-3624570%402x.png)

##### Divide the Article Content Into Sections

Add sections to the article’s top-level `components` array and move all existing components into the new sections. This requires moving a large amount of code.

1. Copy the example code [`Section Components: Copy This Code`](adding-parallax-behavior#Section-Components-Copy-This-Code.md).
2. Paste the code inside the article’s top-level `components` array, after the opening bracket (`[`).
3. In your `article.json` file, cut your `header` component—including all its nested component arrays—to your clipboard. The code you are cutting begins with the opening brace (`{`) before `"role": "header"` and ends with a mix of five alternating braces and brackets (`}]}]}`).
4. In your `article.json` file, select the ellipses (`...`) in the first section.
5. Paste the copied code into `article.json`, replacing the line that you selected in the previous step.
6. In your `article.json` file, cut all components after the second section to your clipboard. The code you are cutting begins with the opening brace (`{`) before `"role": "heading1",` and ends with the closing brace (`}`) that ends your `tweet` component.
7. In your `article.json` file, select the ellipses (`...`) in the second section.
8. Paste the copied code into `article.json`, replacing the line that you selected in the previous step.
9. Delete the extra comma between the closing brace (`}`) that ends the second `section` component and the closing bracket (`]`) that ends the article’s top-level `components` array.

Your code should look like the example code [`Section Components: Result (Collapsed)`](adding-parallax-behavior#Section-Components-Result-Collapsed.md) and [`Section Components: Result (Expanded)`](adding-parallax-behavior#Section-Components-Result-Expanded.md).

After you make these changes in your code, you can successfully preview your working `article.json` file in News Preview, but it won’t look any different until you add parallax behavior in [`Add Parallax Behavior in the First Section`](adding-parallax-behavior#Add-Parallax-Behavior-in-the-First-Section.md).

###### Section Components Copy This Code

```json
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "components": [
        ...
      ]
    },
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "components": [
        ...
      ]
    }
```

###### Section Components Result Collapsed

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "components": [
        ...
      ]
    },
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "components": [
        ...
      ]
    }
  ],
  ...
}
```

###### Section Components Result Expanded

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "section",
      "layout": "fullBleedLayout",
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
        }
      ]
    },
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "components": [
        {
          "role": "heading1",
          "layout": "heading1Layout",
          "text": "HEADING"
        },
        ...
        {
          "role": "tweet",
          "layout": "noMarginLayout",
          "URL": "https://twitter.com/Urna_Semper/status/1480968065630285834"
        }
      ]
    }
  ],
...
}
```

##### Add Parallax Behavior in the First Section

Your article currently has two sections. You’ll use the first section’s `behavior` property to assign a parallax factor lower than 1, causing the first section to scroll more slowly than the default scroll speed.

1. Copy the example code [`Behavior: Copy This Code`](adding-parallax-behavior#Behavior-Copy-This-Code.md).
2. Paste the code inside the first `section` component, after the line `"layout": "fullBleedLayout",`

Your code should look like the example code [`Behavior: Result`](adding-parallax-behavior#Behavior-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see the changes in scroll speed. You might notice text becoming illegible as it covers the image. You’ll fix this in [`Use the Opaque Background with the Lower Section`](adding-parallax-behavior#Use-the-Opaque-Background-with-the-Lower-Section.md) by adding a background color to the lower section.

###### Behavior Copy This Code

```json
      "behavior": {
        "type": "parallax",
        "factor": 0.8
      },
```

###### Behavior Result

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

##### Define a Componentstyle Object for Background Color

To finish the parallax behavior, you need to add a background color to the lower section. Before you can do that, you must define a `ComponentStyle` object.

1. Copy the example code [`bodyBackgroundStyle: Copy This Code`](adding-parallax-behavior#bodyBackgroundStyle-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentStyle` object and the closing brace for the whole `componentStyles` property.

Your code should look like the example code [`bodyBackgroundStyle: Result`](adding-parallax-behavior#bodyBackgroundStyle-Result.md).

###### Bodybackgroundstyle Copy This Code

```json
,
    "bodyBackgroundStyle": {
      "backgroundColor": "#FFF"
    }
```

###### Bodybackgroundstyle Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentStyles": {
    ...
    "bodyBackgroundStyle": {
      "backgroundColor": "#FFF"
    }
  },
  ...
}
```

##### Use the Opaque Background with the Lower Section

As a final step, you need to add a reference to the `ComponentStyle` object you just defined.

To add the reference, in your `article.json` file, inside your second `section` component, add a property named `style` with a value of `"bodyBackgroundStyle"`.

Your code should look like the example code [`Opaque Background: Result`](adding-parallax-behavior#Opaque-Background-Result.md).

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see that the lower section remains legible as it scrolls past the upper section.

###### Opaque Background Result

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
        ...
      ]
    }
  ],
  ...
}
```

##### Previous

[`Creating a Layered Header`](creating-a-layered-header.md)

##### Next

[`Viewing the Finished Article for Advanced Design Tutorial 1`](viewing-the-finished-article-for-advanced-design-tutorial-1.md)

## See Also

- [About Component Behaviors](about-component-behaviors.md)
  Learn how to affect components’ reactions to device motion and scrolling.
- [object Parallax](../applenewsformat/parallax.md)
  The behavior whereby a component moves at a speed different from the scroll speed.
- [object ComponentStyle](../applenewsformat/componentstyle.md)
  The object for setting style properties for components, including background color and fill, borders, and table styles.
- [object Section](../applenewsformat/section.md)
  The component for organizing an article into sections.
- [Setting Up the Advanced Tutorials](setting-up-the-advanced-tutorials.md)
  Download the tutorial files, and learn about what you’ll create in the three advanced tutorials.
- [About Containers](about-containers.md)
  Learn the basic Apple News Format container concepts required for the three advanced tutorials.
- [Creating a Layered Header](creating-a-layered-header.md)
  Create a header with a caption that’s layered in front of an image.
- [Viewing the Finished Article for Advanced Design Tutorial 1](viewing-the-finished-article-for-advanced-design-tutorial-1.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-parallax-behavior)*