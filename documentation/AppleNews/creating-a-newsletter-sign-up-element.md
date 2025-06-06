# Creating a Newsletter Sign-Up Element

**Framework**: Apple News

Add a newsletter sign-up element in your article.

#### Overview

You can provide your readers the option to sign up for your publication’s newsletter from an article. By using styles and layouts thoughtfully, you can visually separate your newsletter sign-up element from your article content.

- Add the newsletter sign-up element to your article.
- Use components, component styles, component text styles, and layout objects to customize the display of the newsletter sign-up element.

![A screenshot of an Apple News article with a newsletter sign-up element.](https://docs-assets.developer.apple.com/published/38d8b271e8a97289d233ba3ca6f834fd/media-4285520%402x.png)

##### Create Component Layout Objects for Newsletter Sign Up

To make adjustments to the positioning of the newsletter sign-up element, you must first create new `ComponentLayout` objects:

1. Copy the example code [`Layout: Copy This Code`](creating-a-newsletter-sign-up-element#Layout-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `componentLayout` object and the closing brace for the whole `ComponentLayouts` property.

Your code should look like the example code [`Layout: Result`](creating-a-newsletter-sign-up-element#Layout-Result.md).

###### Layout Copy This Code

```json
,
     "newsletterLayout": {
       "padding": 30
     },
     "newsletterHeadingLayout": {
       "margin": {
         "bottom": 24
       }
     },
     "newsletterBodyLayout": {
       "margin": {
         "bottom": 26
       }
     },
     "newsletterButtonLayout": {
       "padding": {
         "left": 24,
         "right": 24,
         "top": 12,
         "bottom": 12
       }
     }
```

###### Layout Result

Ellipses (…) indicate lines of code are omitted from this example.

```json
{
  ...
  "componentLayouts": {
    ...
    "newsletterLayout": {
      "padding": 30
    },
    "newsletterHeadingLayout": {
      "margin": {
         "bottom": 24
      }
    },
    "newsletterBodyLayout": {
      "margin": {
         "bottom": 26
      }
    },
    "newsletterButtonLayout": {
      "padding": {
         "left": 24,
         "right": 24,
         "top": 12,
         "bottom": 12
      }
    }
  },
  ...
}
```

##### Define Component Styles for the Newsletter Sign Up Element

Create a new `ComponentStyles` object so that you can apply styles to the newsletter sign-up element.

1. Copy the example code [`Component Styles: Copy This Code`](creating-a-newsletter-sign-up-element#Component-Styles-Copy-This-Code.md).
2. Paste the code between after the `backgroundColor` property of the `sidebarBackgroundStyle` object and the closing brace (`}`) for the whole `componentStyles` property.

Your code should look like the example code [`Component Styles: Result`](creating-a-newsletter-sign-up-element#Component-Styles-Result.md).

###### Component Styles Copy This Code

```json
,
 "newsletterStyle": {
      "mask": {
        "type": "corners",
        "radius": 6
      },
      "backgroundColor": "#F8F8FA",
      "conditional": [
        {
          "backgroundColor": "#1C1C1E",
          "conditions": [
            {
              "preferredColorScheme": "dark"
            }
          ]
        }
      ]
    },
    "newsletterButtonStyle": {
      "border": {
        "all": {
          "color": "#000000",
          "width": 1
        }
      },
      "mask": {
        "type": "corners",
        "radius": 6
      }
    }
```

###### Component Styles Result

Ellipses (…) indicate lines of code that are omitted from this example.

```json
{
  ...
  "componentStyles": {
    ...
    "newsletterStyle": {
      "mask": {
        "type": "corners",
        "radius": 6
      },
      "backgroundColor": "#F8F8FA",
      "conditional": [
        {
          "backgroundColor": "#1C1C1E",
          "conditions": [
            {
              "preferredColorScheme": "dark"
            }
          ]
        }
      ]
    },
    "newsletterButtonStyle": {
      "border": {
        "all": {
          "color": "#000000",
          "width": 1
        }
      },
      "mask": {
        "type": "corners",
        "radius": 6
      }
    }
  },
  ...
},
```

##### Define Component Text Styles for the Newsletter Sign Up Element

Create new `ComponentTextStyle` objects so that you can apply text styles to the heading, body, and button for the newsletter sign-up element.

1. Copy the example code [`Component Text Styles: Copy This Code`](creating-a-newsletter-sign-up-element#Component-Text-Styles-Copy-This-Code.md).
2. Paste the code after the last `componentTextStyle` object and the closing brace (}) for the whole `componentTextStyles` object.

Your code should look like the example code [`Component Text Styles: Result`](creating-a-newsletter-sign-up-element#Component-Text-Styles-Result.md).

###### Component Text Styles Copy This Code

```json
,
 "newsletterHeadingTextStyle": {
      "fontName": "HelveticaNeue",
      "fontSize": 20,
      "textColor": "#000000",
      "textAlignment": "center"
    },
    "newsletterBodyTextStyle": {
      "fontName": "HelveticaNeue",
      "fontSize": 15,
      "lineHeight": 18,
      "textColor": "#000000",
      "textAlignment": "center"
    },
    "newsletterButtonTextStyle": {
      "fontName": "HelveticaNeue",
      "fontSize": 15,
      "textColor": "#000000",
      "textAlignment": "center"
   }
```

###### Component Text Styles Result

Ellipses (…) indicate lines of code that are omitted from this example.

```json
{
  ...
  "componentTextStyles": {
    ...
    "newsletterHeadingTextStyle": {
      "fontName": "HelveticaNeue",
      "fontSize": 20,
      "textColor": "#000000",
      "textAlignment": "center"
    },
    "newsletterBodyTextStyle": {
      "fontName": "HelveticaNeue",
      "fontSize": 15,
      "lineHeight": 18,
      "textColor": "#000000",
      "textAlignment": "center"
    },
    "newsletterButtonTextStyle": {
      "fontName": "HelveticaNeue",
      "fontSize": 15,
      "textColor": "#000000",
      "textAlignment": "center"
    }
  }
}
```

##### Add a Newsletter Sign Up Element in Your Article

Finally, add the newsletter sign-up element to your article.

1. Copy the example code [`Newsletter: Copy This Code`](creating-a-newsletter-sign-up-element#Newsletter-Copy-This-Code.md).
2. Paste the code after the Twitter URL and before the closing square bracket (]) at the end of the `components` array.

Your code should look like the example code in [`Newsletter: Result`](creating-a-newsletter-sign-up-element#Newsletter-Result.md).

###### Newsletter Copy This Code

```json
 ,
  {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "NEWSLETTER SIGN-UP"
        },
        {
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "text": "Sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas."
        },
        {
          "role": "container",
          "layout": "newsletterLayout",
          "style": "newsletterStyle",
          "components": [
            {
              "role": "heading3",
              "text": "Lorem ipsum dolor sit amet",
              "textStyle": "newsletterHeadingTextStyle",
              "layout": "newsletterHeadingLayout"
            },
            {
              "role": "body",
              "text": "Sign up for our daily newsletter, delivered straight to your inbox.",
              "textStyle": "newsletterBodyTextStyle",
              "layout": "newsletterBodyLayout"
            },
            {
              "role": "link_button",
              "format": "html",
              "URL": "https://apple.com",
              "text": "Sign Up &#x2197;&#xFE0E;",
              "textStyle": "newsletterButtonTextStyle",
              "layout": "newsletterButtonLayout",
              "style": "newsletterButtonStyle"
            }
          ]
        }
```

###### Newsletter Result

Ellipses (…) indicate lines of code that are omitted from this example.

```json
{
  ...
  "components": [
    ...
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "NEWSLETTER SIGN-UP"
        },
        {
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "text": "Sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas."
        },
        {
          "role": "container",
          "layout": "newsletterLayout",
          "style": "newsletterStyle",
          "components": [
            {
              "role": "heading3",
              "text": "Lorem ipsum dolor sit amet",
              "textStyle": "newsletterHeadingTextStyle",
              "layout": "newsletterHeadingLayout"
            },
            {
              "role": "body",
              "text": "Sign up for our daily newsletter, delivered straight to your inbox.",
              "textStyle": "newsletterBodyTextStyle",
              "layout": "newsletterBodyLayout"
            },
            {
              "role": "link_button",
              "format": "html",
              "URL": "https://apple.com",
              "text": "Sign Up &#x2197;&#xFE0E;",
              "textStyle": "newsletterButtonTextStyle",
              "layout": "newsletterButtonLayout",
              "style": "newsletterButtonStyle"
            }
          ]
        }
      ]
    }
  ],
  ...
}
```

##### Previous

[`Adding a Fixed Image Fill`](adding-a-fixed-image-fill.md)

##### Next

[`Viewing the Finished Article for Advanced Design Tutorial 3`](viewing-the-finished-article-for-advanced-design-tutorial-3.md)

## See Also

- [Giving the Article a Dark Color Scheme](giving-the-article-a-dark-color-scheme.md)
  Apply a new color scheme to your article.
- [Adding a Video](adding-a-video.md)
  Add a video component inside the header component.
- [Creating a Sidebar](creating-a-sidebar.md)
  Create a box with an HTML bulleted list in the margin.
- [Adding a Fixed Image Fill](adding-a-fixed-image-fill.md)
  Add an image that remains stationary when the user scrolls.
- [Viewing the Finished Article for Advanced Design Tutorial 3](viewing-the-finished-article-for-advanced-design-tutorial-3.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-a-newsletter-sign-up-element)*