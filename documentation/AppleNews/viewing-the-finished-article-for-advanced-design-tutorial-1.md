# Viewing the Finished Article for Advanced Design Tutorial 1

**Framework**: Applenews

See the full JSON code from this tutorial.

#### Overview

This page brings together everything from this tutorial as a template that you can use for your News articles. If you followed the steps throughout this tutorial, the following example code should match the code in your `article.json` file.

You can copy this template (which is also the `article.json` file in `News_Design_Tutorial_Advanced_Article_1`) and modify it to create your own News articles with unique and stylish headers. See [`Download the Article Bundle Examples`](setting-up-the-advanced-tutorials#Download-the-Article-Bundle-Examples.md). To preview this article, see [`Preview the Article Bundle Examples`](setting-up-the-introductory-tutorial#Preview-the-Article-Bundle-Examples.md).

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
      "style": "bodyBackgroundStyle",
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
          "role": "intro",
          "layout": "halfMarginBelowLayout",
          "text": "Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque ipsum?"
        },
        {
          "role": "byline",
          "layout": "fullMarginBelowLayout",
          "text": "By Urna Semper"
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
          "textStyle": "bodyFirstDropCap",
          "text": "<p>Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, dolor repellendus. <a href='http://www.apple.com'>Link text</a> quibusdam et aut.</p><p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, adipisci velit.</p>"
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
          "text": "Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio ducimus qui blanditiis."
        },
        {
          "role": "divider",
          "layout": "fullMarginAboveLayout",
          "stroke": {
            "width": 1,
            "color": "#D5B327"
          }
        },
        {
          "role": "pullquote",
          "layout": "halfMarginAboveQuarterBelowLayout",
          "text": "“QUIA CONSEQUUNTUR MAGNI DOLORES EOS QUI RATIONE VOLUPTATEM SEQUI NESCIUNT.”"
        },
        {
          "role": "pullquote",
          "layout": "halfMarginBelowLayout",
          "textStyle": "attribution",
          "text": "— ATTRIBUTION"
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
          "text": "<p>Cras ultricies mi eu turpis hendrerit fringilla. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ac dui quis mi consectetuer.</p><p>Temporibus autem et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque rerum hic tenetur.</p><p>Inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo esciunt enim ipsam voluptatem quia.</p><p>Ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis <a href='http://www.apple.com'>link text</a> repellat. Sed ut perspiciatis unde omnis iste natus sit voluptatem accusantium doloremque, totam rem aperiam, eaque ipsa quae ab illo inventore.</p><p>Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni.</p>"
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
          "layout": "halfMarginBothLayout",
          "text": "ABOVE: A caption for the entire gallery. Individual photos in the gallery also have their own captions. (Shared attribution)"
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
          "layout": "halfMarginBothLayout",
          "text": "ABOVE: A caption for the entire mosaic. Individual photos in the mosaic also have their own captions. (Shared attribution)"
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
          "role": "body",
          "format": "html",
          "layout": "noMarginLayout",
          "text": "<p>Consequatur aut doloribus asperiores repellat. Sed ut perspiciatis unde omnis iste natus error sit volup tatem accusantium doloremque laudantium, totam rem, eaque ipsa quae ab illo inventore veritatis et quasi archit ecto beatae vitae.</p><p>Nemo enim ipsam volup tatem quia voluptas sit aspernatur aut odit aut fugit, sed quia conse quuntur magni. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam.</p><p>Consequatur aut perferendis doloribus asperiores repellat. Sed ut perspiciatis unde omnis iste natus error sit volup tatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi archit ecto beatae vitae dicta. Nemo enim ipsam volup tatem quia voluptas sit <a href='http://www.apple.com'>link text</a> aut odit aut fugit, sed quia conse quuntur perspiciatis doloribus magni dolores.</p><p>Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam suscipit laboriosam.</p>"
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
    }
  },
  "componentStyles": {
    "captionBarBackgroundStyle": {
      "backgroundColor": "#000"
    },
    "bodyBackgroundStyle": {
      "backgroundColor": "#FFF"
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
    }
  }
}
```

##### Previous

[`Adding Parallax Behavior`](adding-parallax-behavior.md)

##### Next

[`Creating a Complex, Layered Header`](creating-a-complex-layered-header.md)

## See Also

- [Setting Up the Advanced Tutorials](setting-up-the-advanced-tutorials.md)
  Download the tutorial files, and learn about what you’ll create in the three advanced tutorials.
- [About Containers](about-containers.md)
  Learn the basic Apple News Format container concepts required for the three advanced tutorials.
- [Creating a Layered Header](creating-a-layered-header.md)
  Create a header with a caption that’s layered in front of an image.
- [Adding Parallax Behavior](adding-parallax-behavior.md)
  Create an illusion of multiple flat layers by causing the article body to overlap the header as the user scrolls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleNews/viewing-the-finished-article-for-advanced-design-tutorial-1)*