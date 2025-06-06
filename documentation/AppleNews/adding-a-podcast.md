# Adding a Podcast

**Framework**: Apple News

Add a link to a podcast that displays the podcast artwork and the podcast show or episode information.

#### Overview

By using the podcast component, you can add a link to a podcast without using external assets.

:

- Create a podcast component.
- Change the podcast orientation.

![A screenshot of an Apple News article with a podcast on iPad.](https://docs-assets.developer.apple.com/published/850e8a5a83815fd545a5fc29646c63ad/media-3966391%402x.png)

##### Add a Podcast in Your Article

In [`Positioning Text Components`](positioning-text-components.md), you created some `ComponentLayout` objects. You’ll refer to those `ComponentLayout` objects in this code.

1. Copy the example code from [`Podcast: Copy This Code`](adding-a-podcast#Podcast-Copy-This-Code.md).
2. Paste the code inside the components array of your article,  after the closing brace and comma (`},`) of the body component that begins with `Consequatur` `aut doloribus`.

Your code should look like the example code in [`Podcast: Result`](adding-a-podcast#Podcast-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see a podcast in your article.

###### Podcast Copy This Code

```json
    {
      "role": "heading2",
      "layout": "fullMarginAboveHalfBelowLayout",
      "text": "PODCAST HEADING"
    },
    {
      "role": "podcast",
      "layout": "noMarginLayout",
      "URL": "https://podcasts.apple.com/us/podcast/apple-news-today/id1473872585"
    },
```

###### Podcast Result

Ellipses (…) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    ...
    {
      "role": "heading2",
      "layout": "fullMarginAboveHalfBelowLayout",
      "text": "PODCAST HEADING"
    },
    {
      "role": "podcast",
      "layout": "noMarginLayout",
      "URL": "https://podcasts.apple.com/us/podcast/apple-news-today/id1473872585"
    },
    ...
  ],
  ...
}
```

##### Adjust the Podcast Orientation

The podcast you added to your article shows the default podcast orientation that changes automatically based on screen size. On larger tablet screens, the podcast art displays on the left and the podcast information and link button appear on the right. On smaller mobile screens, the artwork, podcast information, and link button appear stacked.

Instead of using the orientation that automatically changes based on screen size, you can set the default orientation to `lanndscape`. The `landscape` orientation saves screen space on mobile devices.

1. Copy the line `"orientation": "landscape"`,
2. Paste the line inside your `podcast` component, after the line that begins with `"layout"`:

After you make this change in your code, you can preview your working `article.json` file in News Preview to see a podcast set to `landscape` orientation.

###### Podcast Orientation Result

Ellipses (…) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    ...
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
    ...
  ],
  ...
}
```

###### Previous

[`Adding a Tweet`](adding-a-tweet.md)

###### Next

[`Viewing the Finished Article for the Introductory Design Tutorial`](viewing-the-finished-article-for-the-introductory-design-tutorial.md)

## See Also

- [Setting Up the Introductory Tutorial](setting-up-the-introductory-tutorial.md)
  Download the tutorial files, and learn about what you’ll create in the introductory tutorial.
- [Creating Your First Article](creating-your-first-article.md)
  Create an article with text components and component text styles.
- [Positioning Text Components](positioning-text-components.md)
  Adjust the positions of the text components in your article—for example, place the article body off-center.
- [Adding a Divider](adding-a-divider.md)
  Create a horizontal, styled divider that extends to the right edge of the display.
- [Adding an Image and Captions](adding-an-image-and-captions.md)
  Create a photo that extends to both edges of the display, with captions that appear in the article layout and in full-screen view.
- [Adding a Pull Quote](adding-a-pull-quote.md)
  Break an existing body component into two components, and then insert a pull quote between them.
- [Adding a Gallery of Images](adding-a-gallery-of-images.md)
  Display three images as a sequential gallery.
- [Adding a Mosaic of Images](adding-a-mosaic-of-images.md)
  Display five images as mosaic tiles.
- [Adding a Tweet](adding-a-tweet.md)
  Include a tweet in an article.
- [Viewing the Finished Article for the Introductory Design Tutorial](viewing-the-finished-article-for-the-introductory-design-tutorial.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-a-podcast)*