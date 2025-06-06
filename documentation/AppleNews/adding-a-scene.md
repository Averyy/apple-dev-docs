# Adding a Scene

**Framework**: Apple News

Control how the article’s opening section comes into view.

#### Overview

The fading sticky header scene causes the header to briefly “stick” to the top of the screen and then fade to a defined color.

![Side-by-side screenshots of an Apple News article on iPhone showing the effect of scrolling with a fading sticky header scene.](https://docs-assets.developer.apple.com/published/15e322be7c406b36bdecf38d62e3bd4a/media-3624925%402x.png)

To implement a scene, you add a `scene` property to a `section` or `chapter` component.

##### Apply a Scene

1. In your working `article.json` file, delete the parallax behavior from the first section. The code you are deleting begins with `"behavior": {` and ends with a closing brace and a comma (`},`).
2. Copy the example code [`Scene: Copy This Code`](adding-a-scene#Scene-Copy-This-Code.md).
3. Paste the code inside the first section, replacing the behavior that you deleted in step 1.

Your code should look like the example code [`Scene: Result`](adding-a-scene#Scene-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see the fading sticky header scene.

###### Scene Copy This Code

```json
      "scene": {
        "type": "fading_sticky_header",
        "fadeColor": "#000"
      },
```

###### Scene Result

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

##### Previous

[`Adding Animations`](adding-animations.md)

##### Next

[`Viewing the Finished Article for Advanced Design Tutorial 2`](viewing-the-finished-article-for-advanced-design-tutorial-2.md)

## See Also

- [Adding a Scene to a Chapter or a Section Header](adding-a-scene-to-a-chapter-or-a-section-header.md)
  Add a scene to your article to create special effects.
- [object FadingStickyHeader](../applenewsformat/fadingstickyheader.md)
  The scene that briefly keeps a header at the top of the screen as the person scrolls through the article.
- [object Section](../applenewsformat/section.md)
  The component for organizing an article into sections.
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
- [Viewing the Finished Article for Advanced Design Tutorial 2](viewing-the-finished-article-for-advanced-design-tutorial-2.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-a-scene)*