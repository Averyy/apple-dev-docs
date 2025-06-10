# Viewing the Finished Article for Advanced Design Tutorial 3

**Framework**: Apple News

See the full JSON code from this tutorial.

#### Overview

This page brings together everything from this tutorial as a template that you can use for your News articles. If you followed the steps throughout this tutorial, the following example code should match the code in your `article.json` file.

You can copy this template (which is also the `article.json` file in `Desktop/News_Design_Tutorial_Advanced/News_Design_Tutorial_Advanced_Article_3`) and modify it to create your own News articles with the effects from this tutorial. See [`Download the Article Bundle Examples`](setting-up-the-advanced-tutorials#Download-the-Article-Bundle-Examples.md). To preview this article, see [`Preview the Article Bundle Examples`](setting-up-the-introductory-tutorial#Preview-the-Article-Bundle-Examples.md).

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
      "role": "header",
      "layout": "fullBleedLayout",
      "behavior": {
        "type": "parallax",
        "factor": 0.8
      },
      "components": [
        {
          "role": "video",
          "layout": "fullBleedLayout",
          "URL": "http://podcasts.apple.com/resources/462787156.mp4",
          "stillURL": "bundle://video-still.jpg",
          "accessibilityCaption": "Sed ut pers piciatis unde omnis iste natus volup tatem accusantium dolor emque, totam rem aperiam."
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
              "textStyle": "captionLight",
              "text": "<span data-anf-textstyle='DINText'>ABOVE:</span> Sed ut pers piciatis unde omnis iste error sit volup tatem accusa ntium dolor emque, totam rem. (Attribution)"
            }
          ]
        },
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
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "TWEET HEADING"
        },
        {
          "role": "tweet",
          "layout": "noMarginLayout",
          "URL": "https://twitter.com/Urna_Semper/status/1480968065630285834?s=20"
        },
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "HEADING"
        },
        {
          "role": "body",
          "format": "html",
          "layout": "halfMarginBelowLayout",
          "text": "<p>Sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas.</p><p>Etiam tempor, quam ut tristique pharetra, sem nisi dapibus augue, ut ultricies ex felis quis mauris. Morbi vitae ipsum quis diam facilisis ultricies sed ut nisi. Proin vel ligula aliquet mauris efficitur varius in quis dui. Suspendisse vel ex at ex consequat porta eu a nisl. Donec volutpat nunc id augue aliquet dictum. Duis elementum rhoncus porttitor. Nulla et elit interdum dui euismod feugiat. Vestibulum vel lectus vel nunc suscipit interdum molestie non diam. Vivamus nulla dui, feugiat et ultricies nec, tempor at mi.</p><p>Nullam vitae egestas dui. Pellentesque tincidunt ipsum ut nisi vestibulum, ac tincidunt quam scelerisque. Sed laoreet odio quam, quis elementum risus hendrerit ac. Sed feugiat ex at nibh mattis iaculis. Praesent sed sagittis velit, non imperdiet est. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. In vitae feugiat orci. Nam ornare et elit eu condimentum. Etiam et nibh aliquet, dapibus arcu ac, consequat nulla.</p>"
        },
        {
          "role": "heading2",
          "layout": "fullMarginAboveHalfBelowLayout",
          "text": "NEWSLETTER SIGN-UP HEADING"
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
    },
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
    },
    "fullScreenImageLayout": {
      "ignoreDocumentMargin": true,
      "minimumHeight": "100vmax",
      "margin": {
        "top": 24,
        "bottom": 12
      }
    },
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
    },
    "darkBackgroundStyle": {
      "backgroundColor": "#202020",
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
    },
    "sidebarBackgroundStyle": {
      "backgroundColor": "#EAF1F4"
    },
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
      "fontStyle": "italic",
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
    },
    "bodyFirstDropCapDark": {
      "textColor": "#FFF",
      "dropCapStyle": {
        "fontName": "DINAlternate-Bold",
        "textColor": "#D5B327",
        "numberOfLines": 2
      }
    },
    "pullquoteLight": {
      "textColor": "#F5F9FB"
    },
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

##### Previous

[`Creating a Newsletter Sign-Up Element`](creating-a-newsletter-sign-up-element.md)

## See Also

- [Giving the Article a Dark Color Scheme](giving-the-article-a-dark-color-scheme.md)
  Apply a new color scheme to your article.
- [Adding a Video](adding-a-video.md)
  Add a video component inside the header component.
- [Creating a Sidebar](creating-a-sidebar.md)
  Create a box with an HTML bulleted list in the margin.
- [Adding a Fixed Image Fill](adding-a-fixed-image-fill.md)
  Add an image that remains stationary when the user scrolls.
- [Creating a Newsletter Sign-Up Element](creating-a-newsletter-sign-up-element.md)
  Add a newsletter sign-up element in your article.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/viewing-the-finished-article-for-advanced-design-tutorial-3)*