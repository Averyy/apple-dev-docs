# Adding a Video

**Framework**: Applenews

Add a video component inside the header component.

#### Overview

A `video` component allows the user to control playback and hear audio.

![Screenshot of an Apple News article with a video component on iPad.](https://docs-assets.developer.apple.com/published/53e00d87fe871aafebaec503a71c89d1/media-3624927%402x.png)

##### Add a Video to the Header

To add a video to your article, you simply add a `video` component to a `components` array. Here, you’ll add a `video` component to the `components` array in the `header` component.

> **Note**:  Alternatively, to include a video that plays automatically as the header’s background, you can use a [`VideoFill`](https://developer.apple.com/documentation/applenewsformat/videofill). With a video fill, playback and audio are disabled, but the video can automatically loop. With a video fill, but not a `video` component, you can also use a scene to affect how the opening section or chapter, including the video, comes into view. See [`Adding a Scene`](adding-a-scene.md).

In [`Download the Article Bundle Examples`](setting-up-the-advanced-tutorials#Download-the-Article-Bundle-Examples.md), you downloaded a bundle called `News_Design_Tutorial_Advanced_Article_3` that contains a thumbnail image. Now, you’ll move that image into your working folder and use it as a thumbnail.

1. Move the `video-still.jpg` file from the `Desktop/News_Design_Tutorial_Advanced/News_Design_Tutorial_Advanced_Article_3` folder to the folder that contains your working `article.json` file.
2. In your working `article.json` file, delete the first section, including its `components` array. The code you are deleting begins with the opening brace (`{`) before `"role": "section",` and ends with a closing bracket, a closing brace, and a comma (`]},`).
3. Copy the example code [`Header Component: Copy This Code`](adding-a-video#Header-Component-Copy-This-Code.md).
4. Paste the code inside the top-level `components` array, after the opening  bracket (`[`).

Your code should look like the example code [`Header Component: Result`](adding-a-video#Header-Component-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see the video.

###### Header Component Copy This Code

```json
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
```

###### Header Component Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
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
    ...
  ],
  ...
}
```

##### Previous

[`Giving the Article a Dark Color Scheme`](giving-the-article-a-dark-color-scheme.md)

##### Next

[`Creating a Sidebar`](creating-a-sidebar.md)

## See Also

- [object Video](../applenewsformat/video.md)
  The component for adding a video.
- [Preparing Image, Video, Audio, Music, and ARKit Assets](preparing-image-video-audio-music-and-arkit-assets.md)
  Add media assets to your article.
- [Giving the Article a Dark Color Scheme](giving-the-article-a-dark-color-scheme.md)
  Apply a new color scheme to your article.
- [Creating a Sidebar](creating-a-sidebar.md)
  Create a box with an HTML bulleted list in the margin.
- [Adding a Fixed Image Fill](adding-a-fixed-image-fill.md)
  Add an image that remains stationary when the user scrolls.
- [Creating a Newsletter Sign-Up Element](creating-a-newsletter-sign-up-element.md)
  Add a newsletter sign-up element in your article.
- [Viewing the Finished Article for Advanced Design Tutorial 3](viewing-the-finished-article-for-advanced-design-tutorial-3.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppleNews/adding-a-video)*