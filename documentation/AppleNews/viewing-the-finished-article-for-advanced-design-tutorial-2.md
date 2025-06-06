# Viewing the Finished Article for Advanced Design Tutorial 2

**Framework**: Applenews

See the full JSON code from this tutorial.

#### Overview

This page brings together everything from this tutorial as a template that you can use for your News articles. If you followed the steps throughout this tutorial, the following example code should match the code in your `article.json` file.

You can copy this template (which is also the `article.json` file in `News_Design_Tutorial_Advanced_Article_2`) and modify it to create your own News articles with varied layout and positioning. See [`Download the Article Bundle Examples`](setting-up-the-advanced-tutorials#Download-the-Article-Bundle-Examples.md). To preview this article, see [`Preview the Article Bundle Examples`](setting-up-the-introductory-tutorial#Preview-the-Article-Bundle-Examples.md).

> **Note**:  If your `article.json` file refers to an image using a URL that begins with `bundle://`, that image must be located within the same folder as your `article.json` file.

```json
{
  "title": "Article Title",
  "metadata": {
    "thumbnailURL": "bundle://header.jpg",
    "excerpt": "Quia consequuntur magni accusantium doloremque eos qui ratione voluptatem sequi nesciunt?"
  },
  "version": "1.5",
  "identifier": "testArticle",
  "language": "en",
  "layout": {
    "columns": 20,
    "width": 1024,
    "margin": 60,
    "gutter": 20
  },
  "documentStyle": {
    "backgroundColor": "#FFF"
  },
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
      "layout": "fullBleedLayout",
      "style": "bodyBackgroundStyle",
      "components": [
        {
          "role": "intro",
          "layout": "halfMarginBothLayout",
          "text": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque ipsum?"
        },
        {
          "role": "byline",
          "format": "html",
          "layout": "fullMarginBelowLayout",
          "text": "<span data-anf-textstyle='lightGrayText'>By</span> Urna Semper"
        },
        {
          "role": "divider",
          "layout": "fullMarginBelowLayout",
          "stroke": {
            "width": 1,
            "color": "#D5B327"
          }
        },
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
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "HEADING"
        },
        {
          "role": "container",
          "layout": "quoteLockupLayout",
          "style": "quoteLockupStyle",
          "anchor": {
            "targetAnchorPosition": "center",
            "target": "p1"
          },
          "components": [
            {
              "role": "pullquote",
              "format": "html",
              "layout": "halfMarginAboveQuarterBelowContainedLayout",
              "text": "“QUIA CONSEQUUNTUR MAGNI DOLORES EOS <span data-anf-textstyle='mediumGrayText'>QUI RATIONE VOLUPTATEM SEQUI NESCIUNT.”</span>",
              "animation": {
                "type": "scale_fade",
                "userControllable": true,
                "initialAlpha": 0.5,
                "initialScale": 0.75
              }
            },
            {
              "role": "pullquote",
              "layout": "halfMarginBelowContainedLayout",
              "textStyle": "attribution",
              "text": "— ATTRIBUTION"
            }
          ]
        },
        {
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "text": "<p>Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio ducimus qui blanditiis.</p><p id='p1'>Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer.</p><p>Temporibus autem et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque rerum hic tenetur.</p><p>Inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo esciunt enim ipsam voluptatem quia.</p><p>Ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis <a href='http://www.apple.com'>link text</a> repellat. Sed ut perspiciatis unde omnis iste natus sit voluptatem accusantium doloremque, totam rem aperiam, eaque ipsa quae ab illo inventore.</p><p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni.</p>"
        },
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "HEADING"
        },
        {
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "text": "Sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas."
        },
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "GALLERY HEADING"
        },
        {
          "role": "gallery",
          "layout": "noMarginLayout",
          "animation": {
            "type": "move_in",
            "preferredStartingPosition": "right"
          },
          "items": [
            {
              "URL": "bundle://gallery-01.jpg",
              "caption": "A caption for the first image in the gallery."
            },
            {
              "URL": "bundle://gallery-02.jpg",
              "caption": "A caption for the second image in the gallery."
            },
            {
              "URL": "bundle://gallery-03.jpg",
              "caption": "A caption for the third image in the gallery."
            }
          ]
        },
        {
          "role": "caption",
          "format": "html",
          "layout": "halfMarginBothLayout",
          "text": "<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the entire gallery. Individual photos in the gallery also have their own captions. (Attribution)"
        },
        {
          "role": "divider",
          "layout": "fullMarginBelowLayout",
          "stroke": {
            "width": 1,
            "color": "#D5B327"
          }
        },
        {
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "text": "Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas est, omnis dolor repellendus."
        },
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "MOSAIC HEADING"
        },
        {
          "role": "mosaic",
          "layout": "noMarginLayout",
          "items": [
            {
              "URL": "bundle://mosaic-01.jpg",
              "caption": "A caption for the first image in the mosaic."
            },
            {
              "URL": "bundle://mosaic-02.jpg",
              "caption": "A caption for the second image in the mosaic."
            },
            {
              "URL": "bundle://mosaic-03.jpg",
              "caption": "A caption for the third image in the mosaic."
            },
            {
              "URL": "bundle://mosaic-04.jpg",
              "caption": "A caption for the fourth image in the mosaic."
            },
            {
              "URL": "bundle://mosaic-05.jpg",
              "caption": "A caption for the fifth image in the mosaic."
            }
          ]
        },
        {
          "role": "caption",
          "format": "html",
          "layout": "halfMarginBothLayout",
          "text": "<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the entire mosaic. Individual photos in the mosaic also have their own captions. (Shared attribution)"
        },
        {
          "role": "divider",
          "layout": "noMarginLayout",
          "stroke": {
            "width": 1,
            "color": "#D5B327"
          }
        },
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "HEADING"
        },
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
              "caption": "A caption for the sidebar photo.",
              "animation": {
                "type": "fade_in",
                "userControllable": true,
                "initialAlpha": 0.5
              }
            },
            {
              "role": "caption",
              "format": "html",
              "layout": "halfMarginBothContainedLayout",
              "text": "<span data-anf-textstyle='DINText'>ABOVE:</span> A caption for the sidebar photo. (Attribution)"
            }
          ]
        },
        {
          "identifier": "body02",
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "text": "<p>Consequatur aut doloribus asperiores repellat. Sed ut perspiciatis unde omnis iste natus error sit volup tatem accusantium doloremque laudantium, totam rem, eaque ipsa quae ab illo inventore veritatis et quasi archit ecto beatae vitae.</p><p>Nemo enim ipsam volup tatem quia voluptas sit aspernatur aut odit aut fugit, sed quia conse quuntur magni. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt <a id='a1' />ut labore et dolore aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam.</p><p>Consequatur aut perferendis doloribus asperiores repellat. Sed ut perspiciatis unde omnis iste natus error sit volup tatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi archit ecto beatae vitae dicta. Nemo enim ipsam volup tatem quia voluptas sit <a href='http://www.apple.com'>link text</a> aut odit aut fugit, sed quia conse quuntur perspiciatis doloribus magni dolores.</p><p>Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam suscipit laboriosam.</p>"
        },
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "PODCAST HEADING"
        },
        {
          "role": "podcast",
          "layout": "noMarginLayout",
          "orientation": "landscape",
          "URL": "https://podcasts.apple.com/us/podcast/apple-news-today/id1473872585"
        },
        {
          "role": "body",
          "format": "html",
          "layout": "fullMarginAboveLayout",
          "text": "Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio. Dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati."
        },
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "TWEET HEADING"
        },
        {
          "role": "tweet",
          "layout": "noMarginLayout",
          "URL": "https://twitter.com/Urna_Semper/status/1480968065630285834"
        }
      ]
    }
  ],
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
  "componentLayouts": {
    "noMarginLayout": {
      "columnStart": 0,
      "columnSpan": 14
    },
    "heading1Layout": {
      "columnStart": 0,
      "columnSpan": 14,
      "margin": {
        "top": 24,
        "bottom": 3
      }
    },
    "halfMarginBelowLayout": {
      "columnStart": 0,
      "columnSpan": 14,
      "margin": {
        "bottom": 12
      }
    },
    "fullMarginBelowLayout": {
      "columnStart": 0,
      "columnSpan": 14,
      "margin": {
        "bottom": 24
      }
    },
    "fullMarginAboveHalfBelowLayout": {
      "columnStart": 0,
      "columnSpan": 14,
      "margin": {
        "top": 24,
        "bottom": 12
      }
    },
    "bigDividerLayout": {
      "ignoreDocumentMargin": "right",
      "columnStart": 0,
      "columnSpan": 20,
      "margin": {
        "top": 6,
        "bottom": 6
      }
    },
    "fullBleedLayout": {
      "ignoreDocumentMargin": true
    },
    "halfMarginBothLayout": {
      "columnStart": 0,
      "columnSpan": 14,
      "margin": {
        "top": 12,
        "bottom": 12
      }
    },
    "fullMarginAboveLayout": {
      "columnStart": 0,
      "columnSpan": 14,
      "margin": {
        "top": 24
      }
    },
    "halfMarginAboveQuarterBelowLayout": {
      "columnStart": 0,
      "columnSpan": 14,
      "margin": {
        "top": 12,
        "bottom": 6
      }
    },
    "headerImageLayout": {
      "ignoreDocumentMargin": true,
      "minimumHeight": "44vmax"
    },
    "sideCaptionLayout": {
      "columnStart": 14,
      "columnSpan": 6,
      "margin": {
        "bottom": 24
      }
    },
    "quoteLockupLayout": {
      "columnStart": 0,
      "columnSpan": 6
    },
    "halfMarginAboveQuarterBelowContainedLayout": {
      "margin": {
        "top": 12,
        "bottom": 6
      }
    },
    "halfMarginBelowContainedLayout": {
      "margin": {
        "bottom": 12
      }
    },
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
  "componentStyles": {
    "captionBarBackgroundStyle": {
      "backgroundColor": "#000"
    },
    "bodyBackgroundStyle": {
      "backgroundColor": "#FFF"
    },
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
    },
    "quoteLockupStyle": {
      "border": {
        "all": {
          "width": 1,
          "color": "#D5B327"
        },
        "top": true,
        "right": false,
        "bottom": true,
        "left": false
      }
    },
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
  "componentTextStyles": {
    "default": {
      "fontName": "DINAlternate-Bold",
      "textColor": "#222222",
      "fontSize": 16,
      "lineHeight": 22,
      "linkStyle": {
        "textColor": "#D5B327"
      }
    },
    "default-body": {
      "fontName": "IowanOldStyle-Roman",
      "paragraphSpacingBefore": 12,
      "paragraphSpacingAfter": 12
    },
    "default-title": {
      "fontName": "DINAlternate-Bold",
      "fontSize": 42,
      "lineHeight": 44,
      "textColor": "#53585F"
    },
    "default-intro": {
      "fontName": "DINAlternate-Bold",
      "fontSize": 18,
      "lineHeight": 22,
      "textColor": "#A6AAA9"
    },
    "default-byline": {
      "fontName": "DINAlternate-Bold",
      "fontSize": 15,
      "lineHeight": 18,
      "textColor": "#53585F"
    },
    "default-heading2": {
      "fontName": "DINAlternate-Bold",
      "tracking": 0.05,
      "textColor": "#53585F"
    },
    "default-heading1": {
      "fontName": "DINAlternate-Bold",
      "tracking": 0.12,
      "textColor": "#53585F"
    },
    "bodyFirstDropCap": {
      "dropCapStyle": {
        "fontName": "DINAlternate-Bold",
        "textColor": "#A6AAA9",
        "numberOfLines": 2
      }
    },
    "default-caption": {
      "fontName": "IowanOldStyle-Italic",
      "fontSize": 12,
      "lineHeight": 16,
      "paragraphSpacingBefore": 12,
      "paragraphSpacingAfter": 12,
      "textColor": "#53585F"
    },
    "default-pullquote": {
      "fontName": "DINAlternate-Bold",
      "fontSize": 30,
      "lineHeight": 36,
      "textColor": "#A6AAA9",
      "hangingPunctuation": true
    },
    "attribution": {
      "fontName": "DINAlternate-Bold",
      "fontSize": 12,
      "lineHeight": 16,
      "tracking": 0.12,
      "textColor": "#53585F",
      "textAlignment": "right"
    },
    "captionLight": {
      "textColor": "#FFF"
    },
    "heading1Light": {
      "textColor": "#FFF"
    }
  }
}
```

##### Previous

[`Adding a Scene`](adding-a-scene.md)

##### Next

[`Giving the Article a Dark Color Scheme`](giving-the-article-a-dark-color-scheme.md)

## See Also

- [Creating a Complex, Layered Header](creating-a-complex-layered-header.md)
  Layer a title and heading in front of an image, with their colors optimized for legibility.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleNews/viewing-the-finished-article-for-advanced-design-tutorial-2)*