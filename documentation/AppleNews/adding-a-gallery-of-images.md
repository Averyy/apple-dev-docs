# Adding a Gallery of Images

**Framework**: Apple News

Display three images as a sequential gallery.

#### Overview

![Screenshot of an Apple News article with a gallery on iPad.](https://docs-assets.developer.apple.com/published/021ce7a4f8e709bbb71ad8fc9e35e467/media-3624436%402x.png)

##### Add a Gallery in Your Article

In [`Download the Article Bundle Examples`](setting-up-the-introductory-tutorial#Download-the-Article-Bundle-Examples.md), you downloaded a bundle called `News_Design_Tutorial_5_Galleries` that contains gallery images and mosaic images. Now, you’ll move some of those images into your working folder and create a `gallery` component to display the images.

1. Move the `gallery-01.jpg`, `gallery-02.jpg`, and `gallery-03.jpg` files from the `Desktop/News_Design/Tutorial/News_Design_Tutorial_5_Galleries` folder that you downloaded in [`Download the Article Bundle Examples`](setting-up-the-introductory-tutorial#Download-the-Article-Bundle-Examples.md) to the folder that contains your working `article.json` file.
2. Copy the example code [`Gallery: Copy This Code`](adding-a-gallery-of-images#Gallery-Copy-This-Code.md).
3. Paste the code inside the `components` array of your article, after the closing brace (`}`) of the third `heading2` component.

Your code should look like the example code [`Gallery: Result`](adding-a-gallery-of-images#Gallery-Result.md).

After you make this change in your code, you can preview your working `article.json` file in News Preview to see a gallery in your article.

###### Gallery Copy This Code

```json
    {
      "role": "gallery",
      "items": [
        {
          "URL": "bundle://gallery-01.jpg"
        },
        {
          "URL": "bundle://gallery-02.jpg"
        },
        {
          "URL": "bundle://gallery-03.jpg"
        }
      ]
    },
```

###### Gallery Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    ...
    {
      "role": "gallery",
      "items": [
        {
          "URL": "bundle://gallery-01.jpg"
        },
        {
          "URL": "bundle://gallery-02.jpg"
        },
        {
          "URL": "bundle://gallery-03.jpg"
        }
      ]
    },
    ...
  ],
  ...
}
```

##### Add Captions for Gallery Images

In [`Adding an Image and Captions`](adding-an-image-and-captions.md), you created a `caption` component in your article layout and a `caption` property for when users view your photo in full screen. Here, you’ll do something similar, adding a `caption` component for the gallery and `caption` properties for each gallery item.

1. Copy the example code [`Caption: Copy This Code`](adding-a-gallery-of-images#Caption-Copy-This-Code.md).
2. Paste the code inside the `components` array of your article, after the closing brace and comma (`},`) that end the `gallery` component.
3. In each of the three gallery items in your `gallery` component, add a comma after `"bundle://gallery-<XX>.jpg"`
4. Copy the `"caption"` properties in the example code [`Caption: Result`](adding-a-gallery-of-images#Caption-Result.md), and paste them after the commas that you added in the previous step.

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see captions for each gallery item and for the whole gallery.

###### Caption Copy This Code

```json
    {
      "role": "caption",
      "text": "ABOVE: A caption for the entire gallery. Individual photos in the gallery also have their own captions. (Shared attribution)"
    },
```

###### Caption Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    ...
    {
      "role": "gallery",
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
      "text": "ABOVE: A caption for the entire gallery. Individual photos in the gallery also have their own captions. (Shared attribution)"
    },
    ...
  ],
  ...
}
```

##### Modify Gallery and Caption Positioning and Add a Divider

In [`Positioning Text Components`](positioning-text-components.md) and [`Adding an Image and Captions`](adding-an-image-and-captions.md), you created some `ComponentLayout` objects. You’ll refer to those `ComponentLayout` objects in this code. You’ll also add a `divider` component to set the gallery apart visually.

1. Copy the line `"layout": "noMarginLayout",`
2. Paste the line inside your `gallery` component, after the line `"role": "gallery",`
3. Copy the line `"layout": "halfMarginBothLayout",`
4. Paste the line inside your `caption` component, after the line `"role": "caption",`
5. Copy the example code [`Divider: Copy This Code`](adding-a-gallery-of-images#Divider-Copy-This-Code.md), and paste it after the closing brace and comma (`},`) that end the `caption` component for the gallery.

Your code should look like the example code [`Divider: Result`](adding-a-gallery-of-images#Divider-Result.md).

After you make these changes in your code, you can preview your working `article.json` file in News Preview to see the new divider and some changes in the positioning of your components.

###### Divider Copy This Code

```json
    {
      "role": "divider",
      "layout": "fullMarginBelowLayout",
      "stroke": {
        "width": 1,
        "color": "#D5B327"
      }
    },
```

###### Divider Result

Ellipses (`...`) indicate lines of code that have been omitted from this example.

```json
{
  ...
  "components": [
    ...
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
    ...
  ],
  ...
}
```

##### Further Exploration

At any time, you can try changing property values in your `article.json` file and then use News Preview to see how these changes affect the look of your article.

For example, try switching the order of the first two images in your `gallery` component:

1. In your `article.json` file, find the `items` array inside the `gallery` component.
2. Within the `items` array, cut the entire first object, including both braces (`{}`) and the comma, to your clipboard.
3. Paste the object between the two remaining objects in the gallery.
4. Preview your `article.json` file in News Preview.

The order of your first and second gallery items has been switched.

##### Previous

[`Adding a Pull Quote`](adding-a-pull-quote.md)

##### Next

[`Adding a Mosaic of Images`](adding-a-mosaic-of-images.md)

## See Also

- [object Gallery](../applenewsformat/gallery.md)
  The component for displaying a sequence of images in a specific order as a horizontal strip.
- [object GalleryItem](../applenewsformat/galleryitem.md)
  An object used in a gallery or mosaic component for displaying an individual image.
- [object Caption](../applenewsformat/caption.md)
  The component for adding caption text.
- [object CaptionDescriptor](../applenewsformat/captiondescriptor.md)
  The object you use in image components for displaying captions when the image is full-screen.
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
- [Adding a Mosaic of Images](adding-a-mosaic-of-images.md)
  Display five images as mosaic tiles.
- [Adding a Tweet](adding-a-tweet.md)
  Include a tweet in an article.
- [Adding a Podcast](adding-a-podcast.md)
  Add a link to a podcast that displays the podcast artwork and the podcast show or episode information.
- [Viewing the Finished Article for the Introductory Design Tutorial](viewing-the-finished-article-for-the-introductory-design-tutorial.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/adding-a-gallery-of-images)*