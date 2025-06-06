# Adding Animations

**Framework**: Apple News

Use animations to affect how parts of your article come into view the first time they appear.

#### Overview

The images below display some animations. In the first image, the pull quote gets larger and darker as the user scrolls through the text. In the second image, the photo gets darker, but not larger, as the user scrolls. In the third image, the gallery moves in from the right side of the screen.

![Side-by-side screenshots of an Apple News article on iPhone showing the effect of scrolling with a scale fade animation.](https://docs-assets.developer.apple.com/published/9a1e30efa0b4822e6d1b238cd6bd3917/media-3625689%402x.png)

![Side-by-side screenshots of an Apple News article on iPhone showing the effect of scrolling with a fade-in animation.](https://docs-assets.developer.apple.com/published/f42dc49a0e2c5ae4d3cfcbf07d0729e7/media-3625691%402x.png)

![Side-by-side screenshots of an Apple News article on iPhone showing the effect of scrolling with a move-in animation.](https://docs-assets.developer.apple.com/published/ebcb91dec2f7fc2c6dc6b7d220768098/media-3625690%402x.png)

##### Create Animations

1. Copy the example code [`Scale Fade Animation: Copy This Code`](adding-animations#Scale-Fade-Animation-Copy-This-Code.md).
2. Paste the code inside the `pullquote` component in your `article.json` file, after the closing quotation mark that ends the `text` property.
3. Copy the example code [`Move-In Animation: Copy This Code`](adding-animations#Move-In-Animation-Copy-This-Code.md).
4. Paste the code inside the `gallery` component in your `article.json` file, after the comma that ends the `layout` property.
5. Copy the example code [`Fade-In Animation: Copy This Code`](adding-animations#Fade-In-Animation-Copy-This-Code.md).
6. Paste the code inside the `photo` component in your `article.json` file, after the closing quotation mark that ends the `caption` property.

Your code should look like the example code [`Animations: Result`](adding-animations#Animations-Result.md).

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see the animations.

###### Scale Fade Animation Copy This Code

```json
,
              "animation": {
                "type": "scale_fade",
                "userControllable": true,
                "initialAlpha": 0.5,
                "initialScale": 0.75
              }
```

###### Move in Animation Copy This Code

```json
          "animation": {
            "type": "move_in",
            "preferredStartingPosition": "right"
          },
```

###### Fade in Animation Copy This Code

```json
,
              "animation": {
                "type": "fade_in",
                "userControllable": true,
                "initialAlpha": 0.5
              }
```

###### Animations Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    ...
    {
      "role": "section",
      ...
      "components": [
        ...
        {
          "role": "container",
          ...
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
            ...
          ]
        },
        ...
        {
          "role": "gallery",
          "layout": "noMarginLayout",
          "animation": {
            "type": "move_in",
            "preferredStartingPosition": "right"
          },
          "items": [
            ...
          ]
        },
        ...
        {
          "role": "container",
          ...
          "components": [
            {
              "role": "photo",
              "layout": "halfMarginAboveContainedLayout",
              "URL": "bundle://sidebar.jpg",
              "caption": "A caption for the sidebar photo.",
              "animation": {
                "type": "fade_in",
                "userControllable": true,
                "initialAlpha": 0.5
              }
            },
            ...
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

[`Adding Color to Text Ranges`](adding-color-to-text-ranges.md)

##### Next

[`Adding a Scene`](adding-a-scene.md)

## See Also

- [About Component Animations](about-component-animations.md)
  Learn how to affect the way in which components come into view.
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
- [Adding a Scene](adding-a-scene.md)
  Control how the article’s opening section comes into view.
- [Viewing the Finished Article for Advanced Design Tutorial 2](viewing-the-finished-article-for-advanced-design-tutorial-2.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-animations)*