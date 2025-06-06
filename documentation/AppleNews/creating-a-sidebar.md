# Creating a Sidebar

**Framework**: Apple News

Create a box with an HTML bulleted list in the margin.

#### Overview

Placing supplemental or reference information in the margin of your article can create an informative and engaging experience.

![Screenshot of an Apple News article with an anchored sidebar on iPad.](https://docs-assets.developer.apple.com/published/879c27a2ea7d3a61ed1801527ae9c5bd/media-3624926%402x.png)

##### Create Component Layout Objects for the Sidebar

The `ComponentLayout` object called `sidebarLayout` specifies that the sidebar will begin in column 7 of the article layout and span three columns. The other `ComponentLayout` object makes a minor adjustment.

1. Copy the example code [`Sidebar Layout Objects: Copy This Code`](creating-a-sidebar#Sidebar-Layout-Objects-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentLayout` object and the closing brace for the whole `componentLayouts` property.

Your code should look like the example code [`Sidebar Layout Objects: Result`](creating-a-sidebar#Sidebar-Layout-Objects-Result.md).

###### Sidebar Layout Objects Copy This Code

```json
,
    "sidebarLayout": {
      "contentInset": {
        "left": true,
        "right": true
      },
      "columnStart": 14,
      "columnSpan": 6,
      "margin": {
        "top": 24
      }
    },
    "fullMarginBelowContainedLayout": {
      "margin": {
        "bottom": 24
      }
    }
```

###### Sidebar Layout Objects Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentLayouts": {
    ...
    "sidebarLayout": {
      "contentInset": {
        "left": true,
        "right": true
      },
      "columnStart": 14,
      "columnSpan": 6,
      "margin": {
        "top": 24
      }
    },
    "fullMarginBelowContainedLayout": {
      "margin": {
        "bottom": 24
      }
    }
  },
  ...
}
```

##### Define a Component Style Object for the Sidebar

Before you can apply a background color to the sidebar, you must define  a new `ComponentStyle` object for the sidebar background color.

1. Copy the example code [`sidebarBackgroundStyle: Copy This Code`](creating-a-sidebar#sidebarBackgroundStyle-Copy-This-Code.md).
2. Paste the code between the closing brace (`}`) of the last `ComponentStyle` object and the closing brace for the whole `componentStyles` property.

Your code should look like the example code [`sidebarBackgroundStyle: Result`](creating-a-sidebar#sidebarBackgroundStyle-Result.md).

###### Sidebarbackgroundstyle Copy This Code

```json
,
    "sidebarBackgroundStyle": {
      "backgroundColor": "#EAF1F4"
    }
```

###### Sidebarbackgroundstyle Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "componentStyles": {
    ...
    "sidebarBackgroundStyle": {
      "backgroundColor": "#EAF1F4"
    }
  },
  ...
}
```

##### Update the Body Component

In your working `article.json` file, update the `body` component that follows the `podcast` component.

1. Copy the example code [`Body: Copy This Code`](creating-a-sidebar#Body-Copy-This-Code.md).
2. Paste the copied code, replacing the `body` component that follows the `podcast` component.

Your code should look like the example code [`Body: Result`](creating-a-sidebar#Body-Result.md)

###### Body Copy This Code

```json
{
  "identifier": "body2",
  "role": "body",
  "format": "html",
  "layout": "fullMarginAboveLayout",
  "text": "<p>Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio. Dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati.</p><p>Sed dignissim magna nec metus tincidunt, in posuere tortor malesuada. Morbi auctor justo sodales nulla tincidunt rhoncus. Praesent aliquam, ex eu auctor auctor, turpis metus vehicula augue, non dapibus odio massa a massa. Nunc condimentum dui quis odio condimentum, ac sodales libero elementum. Nullam sagittis felis ac tortor varius ultricies. Duis aliquet ex vel orci aliquam, sit amet bibendum risus rhoncus. Interdum et malesuada fames ac ante ipsum primis in faucibus.</p><p>Aliquam erat volutpat. Phasellus laoreet porttitor quam ut hendrerit. Aliquam nec arcu scelerisque, scelerisque nisi sit amet, eleifend augue. Nunc sit amet elit commodo, congue felis eget, gravida nibh. Praesent lorem risus, tristique sed porta non, aliquam in sapien. Praesent rhoncus orci eu scelerisque euismod. Morbi bibendum lorem lorem, eu tincidunt neque volutpat sit amet. Sed urna ligula, volutpat nec posuere a, laoreet ut tellus. Curabitur lacinia ornare nisi, et aliquet ex pretium sit amet. Aliquam finibus tristique arcu at feugiat. Donec nec sodales magna. Nulla vulputate sem eget libero venenatis lobortis. Morbi nec sodales metus. Ut eu diam quis augue imperdiet interdum ac quis metus.</p>"
},
```

###### Body Result

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
          "role": "podcast",
          "layout": "noMarginLayout",
          "orientation": "horizontal",
          "URL": "https://podcasts.apple.com/us/podcast/apple-news-today/id1473872585"
        },
        {
          "identifier": "body2",
          "role": "body",
          "format": "html",
          "layout": "fullMarginAboveLayout",
          "text": "<p>Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio. Dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati.</p><p>Sed dignissim magna nec metus tincidunt, in posuere tortor malesuada. Morbi auctor justo sodales nulla tincidunt rhoncus. Praesent aliquam, ex eu auctor auctor, turpis metus vehicula augue, non dapibus odio massa a massa. Nunc condimentum dui quis odio condimentum, ac sodales libero elementum. Nullam sagittis felis ac tortor varius ultricies. Duis aliquet ex vel orci aliquam, sit amet bibendum risus rhoncus. Interdum et malesuada fames ac ante ipsum primis in faucibus.</p><p>Aliquam erat volutpat. Phasellus laoreet porttitor quam ut hendrerit. Aliquam nec arcu scelerisque, scelerisque nisi sit amet, eleifend augue. Nunc sit amet elit commodo, congue felis eget, gravida nibh. Praesent lorem risus, tristique sed porta non, aliquam in sapien. Praesent rhoncus orci eu scelerisque euismod. Morbi bibendum lorem lorem, eu tincidunt neque volutpat sit amet. Sed urna ligula, volutpat nec posuere a, laoreet ut tellus. Curabitur lacinia ornare nisi, et aliquet ex pretium sit amet. Aliquam finibus tristique arcu at feugiat. Donec nec sodales magna. Nulla vulputate sem eget libero venenatis lobortis. Morbi nec sodales metus. Ut eu diam quis augue imperdiet interdum ac quis metus.</p>"
        },
        ...
      ]
    }
  ],
  ...
}
```

##### Add and Anchor the Sidebar Content

In your working `article.json` file, the `body` component that follows the `podcast` component should now have an `identifier` property with the value `body2`.

1. Copy the example code [`Container: Copy This Code`](creating-a-sidebar#Container-Copy-This-Code.md).
2. Paste the code after the closing brace and comma at the end of the body component that contains an identifier property with the value `body2`.

Your code should look like the example code [`Container: Result`](creating-a-sidebar#Container-Result.md).

###### Container Copy This Code

```json
{
  "role": "container",
  "layout": "sidebarLayout",
  "style": "sidebarBackgroundStyle",
  "anchor": {
    "targetComponentIdentifier": "body2",
    "targetAnchorPosition": "bottom",
    "originAnchorPosition": "bottom"
  },
  "animation": {
    "type": "fade_in",
    "userControllable": true,
    "initialAlpha": 0.5
  },
  "components": [
    {
      "role": "heading3",
      "layout": "halfMarginBothContainedLayout",
      "text": "EPISODES OF NOTE"
    },
    {
      "role": "divider",
      "layout": "halfMarginBelowContainedLayout",
      "stroke": {
        "width": 1,
        "color": "#A6AAA9"
      }
    },
    {
      "role": "caption",
      "layout": "fullMarginBelowContainedLayout",
      "format": "html",
      "text": " <ul><li>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis.</li> <li>Praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi.</li> <li>Sint occaecati cupiditate non provident.</li> <li>similique sunt in culpa qui officia deserunt mollitia animi.</li> <li>Et harum quidem rerum facilis est et expedita distinctio.</li></ul>"
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
      "layout": "fullBleedLayout",
      "style": "bodyBackgroundStyle",
      "components": [
        ...
        {
          "identifier": "body2",
          "role": "body",
          "format": "html",
          "layout": "fullMarginAboveLayout",
          "text": "<p>Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio. Dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati.</p><p>Sed dignissim magna nec metus tincidunt, in posuere tortor malesuada. Morbi auctor justo sodales nulla tincidunt rhoncus. Praesent aliquam, ex eu auctor auctor, turpis metus vehicula augue, non dapibus odio massa a massa. Nunc condimentum dui quis odio condimentum, ac sodales libero elementum. Nullam sagittis felis ac tortor varius ultricies. Duis aliquet ex vel orci aliquam, sit amet bibendum risus rhoncus. Interdum et malesuada fames ac ante ipsum primis in faucibus.</p><p>Aliquam erat volutpat. Phasellus laoreet porttitor quam ut hendrerit. Aliquam nec arcu scelerisque, scelerisque nisi sit amet, eleifend augue. Nunc sit amet elit commodo, congue felis eget, gravida nibh. Praesent lorem risus, tristique sed porta non, aliquam in sapien. Praesent rhoncus orci eu scelerisque euismod. Morbi bibendum lorem lorem, eu tincidunt neque volutpat sit amet. Sed urna ligula, volutpat nec posuere a, laoreet ut tellus. Curabitur lacinia ornare nisi, et aliquet ex pretium sit amet. Aliquam finibus tristique arcu at feugiat. Donec nec sodales magna. Nulla vulputate sem eget libero venenatis lobortis. Morbi nec sodales metus. Ut eu diam quis augue imperdiet interdum ac quis metus.</p>"
        },
        {
          "role": "container",
          "layout": "sidebarLayout",
          "style": "sidebarBackgroundStyle",
          "anchor": {
            "targetComponentIdentifier": "body2",
            "targetAnchorPosition": "bottom",
            "originAnchorPosition": "bottom"
          },
          "animation": {
            "type": "fade_in",
            "userControllable": true,
            "initialAlpha": 0.5
          },
          "components": [
            {
              "role": "heading3",
              "layout": "halfMarginBothContainedLayout",
              "text": "EPISODES OF NOTE"
            },
            {
              "role": "divider",
              "layout": "halfMarginBelowContainedLayout",
              "stroke": {
                "width": 1,
                "color": "#A6AAA9"
              }
            },
            {
              "role": "caption",
              "layout": "fullMarginBelowContainedLayout",
              "format": "html",
              "text": " <ul><li>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis.</li> <li>Praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi.</li> <li>Sint occaecati cupiditate non provident.</li> <li>similique sunt in culpa qui officia deserunt mollitia animi.</li> <li>Et harum quidem rerum facilis est et expedita distinctio.</li></ul>"
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

[`Adding a Video`](adding-a-video.md)

##### Next

[`Adding a Fixed Image Fill`](adding-a-fixed-image-fill.md)

## See Also

- [Planning the Layout for Your Article](planning-the-layout-for-your-article.md)
  Define a layout that supports the look you want for your article.
- [Positioning the Content in Your Article](positioning-the-content-in-your-article.md)
  Align article components with columns in your layout.
- [Wrapping Text Around a Component](wrapping-text-around-a-component.md)
  Define the layout of a text component to wrap around another component.
- [Nesting Components in an Article](nesting-components-in-an-article.md)
  Use container components to create the component hierarchies you need for special article designs.
- [object Anchor](../applenewsformat/anchor.md)
  The object for anchoring one component to another component in your article’s layout.
- [Using HTML with Apple News Format](using-html-with-apple-news-format.md)
  Use HTML formatting for text components.
- [Giving the Article a Dark Color Scheme](giving-the-article-a-dark-color-scheme.md)
  Apply a new color scheme to your article.
- [Adding a Video](adding-a-video.md)
  Add a video component inside the header component.
- [Adding a Fixed Image Fill](adding-a-fixed-image-fill.md)
  Add an image that remains stationary when the user scrolls.
- [Creating a Newsletter Sign-Up Element](creating-a-newsletter-sign-up-element.md)
  Add a newsletter sign-up element in your article.
- [Viewing the Finished Article for Advanced Design Tutorial 3](viewing-the-finished-article-for-advanced-design-tutorial-3.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/creating-a-sidebar)*