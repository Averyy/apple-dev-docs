# Setting Up the Introductory Tutorial

**Framework**: Apple News

Download the tutorial files, and learn about what you’ll create in the introductory tutorial.

#### Overview

With Apple News Format, you can create signature visual designs for your articles in News. Use Apple News Format to bring your articles to life with beautiful typography, rich photo galleries, and compelling multimedia content. This introductory tutorial will help you create the basic design and layout of an Apple News Format article.

The images below show what your Apple News Format article should look like once you’ve completed the introductory tutorial. These images show some of the design and layout features of Apple News Format. Apple News automatically optimizes your articles for iPhone, iPad, iPod touch, and Mac to give your readers the best experience for their device.

![Screenshot of an Apple News article with a variety of text styles and a photo, on a Mac, iPad, and iPhone.](https://docs-assets.developer.apple.com/published/015363004c93fc4fd07460f23d82248a/media-3958339%402x.png)

![Screenshot of an Apple News article with a mosaic on a Mac, iPad, and iPhone.](https://docs-assets.developer.apple.com/published/f84d6eb2a6629ad29f839aeef781e7fc/media-3624430%402x.png)

![Screenshot of an Apple News article with a map on a Mac, iPad, and iPhone.](https://docs-assets.developer.apple.com/published/0e58c962ab309a678e1391bee54be513/media-3624429%402x.png)

##### Choose an Option for Completing the Introductory Tutorial

Choose one of these options.

 (Recommended.) Download a basic `article.json` file, and use the instructions in this tutorial to add code to the file. Preview your changes as you go, using the [`News Preview`](https://developer.apple.comhttps://developer.apple.com/news-preview/) tool.

 Follow along by looking at downloadable examples that represent the completion of each stage of this tutorial. Preview the completed articles in the [`News Preview`](https://developer.apple.comhttps://developer.apple.com/news-preview/) tool.

##### Download the Article Bundle Examples

An  is a folder that contains the JSON that represents your article along with the article’s image files. You’ll need to download Apple News Format article bundles before beginning the introductory tutorial.

1. On your Desktop, create a folder named `News_Design_Tutorial`.
2. Download and unzip files according to the option you chose in [`Choose an Option for Completing the Introductory Tutorial`](setting-up-the-introductory-tutorial#Choose-an-Option-for-Completing-the-Introductory-Tutorial.md).
3. Move the folders that you downloaded and unzipped in the previous step into your `Desktop/News_Design_Tutorial` folder.

###### Files to Download for Option 1

If you chose option 1 in [`Choose an Option for Completing the Introductory Tutorial`](setting-up-the-introductory-tutorial#Choose-an-Option-for-Completing-the-Introductory-Tutorial.md), download and unzip the following two files:

- [`News_Design_Tutorial_5_Galleries.zip`](https://developer.apple.comhttps://developer.apple.com/apple-news/download/News_Design_Tutorial_5_Galleries.zip). This ZIP file includes an `article.json` file and images, including a gallery and mosaic.
- [`News_Design_Tutorial_1_Article_Structure.zip`](https://developer.apple.comhttps://developer.apple.com/apple-news/download/ANF_Design_Tutorial_1_Article_Structure.zip). This ZIP file includes an `article.json` file and a header image for the basic structure of an article.

> **Note**:  You can’t preview this article yet, because it doesn’t contain sufficient content. You’ll add this missing content as you work through the tutorial.

###### Files to Download for Option 2

If you chose option 2 in [`Choose an Option for Completing the Introductory Tutorial`](setting-up-the-introductory-tutorial#Choose-an-Option-for-Completing-the-Introductory-Tutorial.md), download and unzip the following five files. These example files contain the code and images for the article at the completion of each stage of this tutorial.

- [`News_Design_Tutorial_2_Components.zip`](https://developer.apple.comhttps://developer.apple.com/apple-news/download/News_Design_Tutorial_2_Components.zip). This ZIP file includes an article with text components, styles, and layout.
- [`News_Design_Tutorial_3_Images.zip`](https://developer.apple.comhttps://developer.apple.com/apple-news/download/News_Design_Tutorial_3_Images.zip). This ZIP file includes an article with a photo and captions.
- [`News_Design_Tutorial_4_Quotes.zip`](https://developer.apple.comhttps://developer.apple.com/apple-news/download/News_Design_Tutorial_4_Quotes.zip). This ZIP file includes an article with a pull quote.
- [`News_Design_Tutorial_5_Galleries.zip`](https://developer.apple.comhttps://developer.apple.com/apple-news/download/News_Design_Tutorial_5_Galleries.zip). This ZIP file includes an article with image collections, including a gallery and mosaic.
- [`News_Design_Tutorial_6_Embeds.zip`](https://developer.apple.comhttps://developer.apple.com/apple-news/download/News_Design_Tutorial_6_Embeds.zip). This ZIP file includes an article with embeds, including a tweet and a podcast.

##### Preview the Article Bundle Examples

Use [`News Preview`](https://developer.apple.comhttps://developer.apple.com/news-preview/) to preview articles.

1. Open News Preview, and agree to the license agreement if you’re prompted.
2. If you’re prompted to enter your channel ID, either enter it to see your channel when you preview articles, or dismiss the message without entering anything to preview articles using the News Preview default channel.
3. Click a device to preview a simulation of that device.
4. In Finder, locate `Desktop/News_Design_Tutorial/News_Design_Tutorial_5_Galleries/`.
5. Drag the article bundle folder `News_Design_Tutorial_5_Galleries` (or just the `article.json` file), and drop it on the specified area in the News Preview window.

The simulated device automatically opens Apple News and displays the article. The preview may take a minute to load. To see the article, you don’t need to open the News app, click Next on the News welcome screen, or do anything else on the simulated device.  For more information about viewing and controlling the simulated device in News Preview, see [`Simulator Help`](https://developer.apple.comhttps://help.apple.com/simulator/mac).

##### Update Your Article Preview

Your article preview will automatically update whenever you save changes to the `article.json` file.

For example:

1. If you’re not already doing so, start previewing `Desktop/News_Design_Tutorial/News_Design_Tutorial_5_Galleries/` as described in [`Preview the Article Bundle Examples`](setting-up-the-introductory-tutorial#Preview-the-Article-Bundle-Examples.md).
2. In any text editor, open `Desktop/News_Design_Tutorial/News_Design_Tutorial_5_Galleries/article.json`.
3. Find the text `By Urna Semper`, and replace the characters `Urna Semper` with your own name.
4. Save the file.

The preview updates. This may take a minute. The byline of the article now includes your name. A check mark in the News Preview window indicates that the update is complete. You don’t need to drag and drop the file again.

##### Troubleshoot Your Article Preview

If the article preview doesn’t automatically update when you save changes to the `article.json` file, there may be an error in your JSON code.

To view any errors, in News Preview, choose Window > Console.

If an error in your JSON was found, the console shows information that can help you fix the error. This information sometimes includes the line number in your code where the error was found.

##### Choose a Text Editor

It’s recommended that you choose a text editor designed for editing code. Although you can use any text editing software to edit your JSON files, software specifically intended for code has some important advantages:

- Color coding by data type makes your code easier to read.
- Line numbers make it easier to find JSON errors. See [`Troubleshoot Your Article Preview`](setting-up-the-introductory-tutorial#Troubleshoot-Your-Article-Preview.md).
- You can look closely at your code’s organization by hiding or folding the contents of a set of brackets (`[]`) or braces (`{}`).
- You can quickly reformat your code, for example changing between spaces and tabs for your indentation.

## See Also

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
- [Adding a Podcast](adding-a-podcast.md)
  Add a link to a podcast that displays the podcast artwork and the podcast show or episode information.
- [Viewing the Finished Article for the Introductory Design Tutorial](viewing-the-finished-article-for-the-introductory-design-tutorial.md)
  See the full JSON code from this tutorial.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/setting-up-the-introductory-tutorial)*