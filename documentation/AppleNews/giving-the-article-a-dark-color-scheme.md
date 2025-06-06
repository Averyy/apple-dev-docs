# Giving the Article a Dark Color Scheme

**Framework**: Apple News

Apply a new color scheme to your article.

#### Overview

In this third advanced article design, you’ll create some visual effects using a dark color scheme, a `video` component, and a fixed image fill.

.

![Screenshot of an Apple News article with a dark color scheme on iPhone.](https://docs-assets.developer.apple.com/published/1159bd5b0ddc9c289e47312c6661f9f2/media-3624917%402x.png)

##### Define a Dark Background Color for Components

You can use a dark color scheme to create contrast between one group of articles and another or for variety within a single article.

This `ComponentStyle` object has a dark background color.

1. Open the `article.json` file that you completed in [`Adding a Scene`](adding-a-scene.md), or open `Desktop/News_Design_Tutorial/News_Design_Tutorial_Advanced_Article_2/article.json`.
2. Copy the example code [`darkBackgroundStyle: Copy This Code`](giving-the-article-a-dark-color-scheme#darkBackgroundStyle-Copy-This-Code.md).
3. Paste the code between the closing brace (`}`) of the last `ComponentStyle` object and the closing brace for the whole `componentStyles` property.

Your code should look like the example code [`darkBackgroundStyle: Result`](giving-the-article-a-dark-color-scheme#darkBackgroundStyle-Result.md).

###### Darkbackgroundstyle Copy This Code

```json
,
    "darkBackgroundStyle": {
      "backgroundColor": "#202020"
    }
```

###### Darkbackgroundstyle Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentStyles": {
    ...
    "darkBackgroundStyle": {
      "backgroundColor": "#202020"
    }
  },
  ...
}
```

##### Define a Light Color Text Style

The `ComponentTextStyle` object called `bodyFirstDropCapDark` has a light text color.

1. Copy the example code [`bodyFirstDropCapDark: Copy This Code`](giving-the-article-a-dark-color-scheme#bodyFirstDropCapDark-Copy-This-Code.md).
2. Paste the code inside the `ArticleDocument.componentTextStyles` object in your `article.json` file, after the closing brace (`}`) of the last text style and before the closing bracket for the whole `componentTextStyles` property.

Your code should look like the example code [`bodyFirstDropCapDark: Result`](giving-the-article-a-dark-color-scheme#bodyFirstDropCapDark-Result.md).

###### Bodyfirstdropcapdark Copy This Code

```json
,
    "bodyFirstDropCapDark": {
      "textColor": "#FFF",
      "dropCapStyle": {
        "fontName": "DINAlternate-Bold",
        "textColor": "#D5B327",
        "numberOfLines": 2
      }
    }
```

###### Bodyfirstdropcapdark Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentTextStyles": {
    ...
    "bodyFirstDropCapDark": {
      "textColor": "#FFF",
      "dropCapStyle": {
        "fontName": "DINAlternate-Bold",
        "textColor": "#D5B327",
        "numberOfLines": 2
      }
    }
  }
}
```

##### Implement the Dark Color Scheme

You’ll move some components from the header into a new section and add references to a new `ComponentStyle` object and a new `ComponentTextStyle` object.

1. In your `article.json` file, delete the contents of your header’s `components` array. The code you’re deleting begins with the opening brace (`{`) before `"role": "container"`, and ends with a mix of three alternating brackets and braces (`}]}`).
2. Copy the example code [`Components: Copy This Code`](giving-the-article-a-dark-color-scheme#Components-Copy-This-Code.md).
3. Paste the code inside your second section’s `components` array, after the opening bracket (`[`).
4. Copy the example code [`Section Boundary: Copy This Code`](giving-the-article-a-dark-color-scheme#Section-Boundary-Copy-This-Code.md).
5. Paste the code inside your second section, replacing the comma that follows the first body component.
6. In your second section, change the value of `style` to `"darkBackgroundStyle"`.
7. In your floating caption, add a `textStyle` property with a value of `"captionLight"`.
8. In the body component that uses `bodyFirstDropCap`, change the value of `textStyle` to `"bodyFirstDropCapDark"`, and change the value of `layout` to `"fullMarginBelowLayout"`.

Your code should look like the example code [`Dark Color Scheme: Result`](giving-the-article-a-dark-color-scheme#Dark-Color-Scheme-Result.md).

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see the dark color scheme.

###### Components Copy This Code

```json
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
          "text": "<span data-anf-textstyle='lightGrayText'>ARTICLE TITLE</span> <span data-anf-textstyle='whiteText'>WITH INLINE TEXT STYLE REFERENCES</span>"
        },
```

###### Section Boundary Copy This Code

```json
]
    },
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "style": "bodyBackgroundStyle",
      "components": [
```

###### Dark Color Scheme Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "scene": {
        "type": "fading_sticky_header",
        "fadeColor": "#000"
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
          }
        }
      ]
    },
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "style": "darkBackgroundStyle",
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
          "text": "<span data-anf-textstyle='lightGrayText'>ARTICLE TITLE</span> <span data-anf-textstyle='whiteText'>WITH INLINE TEXT STYLE REFERENCES</span>"
        },
        ...
        {
          "identifier": "body1",
          "role": "body",
          "format": "html",
          "layout": "fullMarginBelowLayout",
          "textStyle": "bodyFirstDropCapDark",
          "text": "<p><span data-anf-textstyle='DINText'>Bold lead-in,</span> cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, dolor repellendus. <a href='http://www.apple.com'>Link text</a> quibusdam et aut.</p><p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, adipisci velit.</p>"
        }
      ]
    },
    {
      "role": "section",
      "layout": "fullBleedLayout",
      "style": "bodyBackgroundStyle",
      "components": [
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "HEADING"
        },
        ...
      ]
    }
  ],
  ...
}
```

##### Set the Default to a Dark Color Scheme

To view the dark color scheme in Dark Mode, switch your simulator device to a dark systemwide appearance (Features > Toggle Appearance).

You can maintain the dark color scheme for your article even when a user switches between a light or dark appearance. Set the `preferredColorScheme` conditional to define the background color for a specific appearance. For more information about conditionals, see Apple News Format > [`Condition`](https://developer.apple.com/documentation/applenewsformat/condition).

In [`Define a Dark Background Color for Components`](giving-the-article-a-dark-color-scheme#Define-a-Dark-Background-Color-for-Components.md), you created a new `ComponentStyle` called `darkBackgroundStyle`. Now you’ll update that style with a conditional to explicitly set a value for your article’s  dark appearance.

1. Copy the example code from [`Condition Dark Mode: Copy This Code`](giving-the-article-a-dark-color-scheme#Condition-Dark-Mode-Copy-This-Code.md).
2. Paste the code inside the `darkBackgroundStyle`, `componentStyle` of your article, at the end of this line: `"backgroundColor": "#202020"`.` `Your code should look like the example code in [`Condition Dark Mode: Result`](giving-the-article-a-dark-color-scheme#Condition-Dark-Mode-Result.md).

###### Condition Dark Mode Copy This Code

```json
,
"conditional": [
  {
    "backgroundColor": "#202020",
    "conditions": [
      {
        "preferredColorScheme": "dark"
      }
    ]
  }
]

```

###### Condition Dark Mode Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{  ...
  "componentStyles": {
    ...
     "darkBackgroundStyle": {
      "backgroundColor": "#202020",
      "conditional": [
        {
          "backgroundColor": "#202020",
          "don’tions": [
            {
              "preferredColorScheme": "dark"
            }
          ]
        }
      ]
    },
    ...
}
```

To view the dark color scheme when the device appearance is toggled, preview your working `article.json` file in News Preview.

![Screenshot of an Apple News article with a dark color scheme on iPhone displaying a light systemwide appearance.](https://docs-assets.developer.apple.com/published/538f90f9e7aa5df57307c6b781824527/media-3966565%402x.png)

![Screenshot of an Apple News article with a dark color scheme on iPhone displaying a dark systemwide appearance.](https://docs-assets.developer.apple.com/published/3ec0beb9f7108c7f92601ee91056edad/media-3966566%402x.png)

##### Further Exploration

For information about using Dark Mode and adjusting designs for light and dark appearances, see [`Apple Human Interface Guidelines > Dark Mode`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/macos/visual-design/dark-mode/).

For information about updating your article so that it adapts when Dark Mode is active, see [`Supporting Dark Mode for Your Article`](supporting-dark-mode-for-your-article.md).

##### Previous

[`Viewing the Finished Article for Advanced Design Tutorial 2`](viewing-the-finished-article-for-advanced-design-tutorial-2.md)

##### Next

[`Adding a Video`](adding-a-video.md)

## See Also

- [Applying a Background to a Component](applying-a-background-to-a-component.md)
  Change the appearance of the backgrounds in your article.
- [Defining a Component Style](defining-a-component-style.md)
  Set style options for the components in your article.
- [object ComponentStyle](../applenewsformat/componentstyle.md)
  The object for setting style properties for components, including background color and fill, borders, and table styles.
- [object TextStyle](../applenewsformat/textstyle.md)
  The object for defining the text style, such as font family, size, and color, that you can apply to ranges of text.
- [Adding a Video](adding-a-video.md)
  Add a video component inside the header component.
- [Creating a Sidebar](creating-a-sidebar.md)
  Create a box with an HTML bulleted list in the margin.
- [Adding a Fixed Image Fill](adding-a-fixed-image-fill.md)
  Add an image that remains stationary when the user scrolls.
- [Creating a Newsletter Sign-Up Element](creating-a-newsletter-sign-up-element.md)
  Add a newsletter sign-up element in your article.
- [Viewing the Finished Article for Advanced Design Tutorial 3](viewing-the-finished-article-for-advanced-design-tutorial-3.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/giving-the-article-a-dark-color-scheme)*