# Planning the Layout for Your Article

**Framework**: Apple News

Define a layout that supports the look you want for your article.

#### Overview

To create a unique look for your News article, you start by defining your layout. Apple News Format uses a column system that provides different horizontal locations for aligning the components in your design — your title, headings, body text, images, pull quotes, and so on.

You might be familiar with  as a text formatting term, but in Apple News Format a column is used for aligning entire components, not the text within a component. The column system is a set of equal-width, vertical segments you use to align components in your layout. The number of columns you choose for your layout determines your options for positioning components.

For example, a layout with one column provides only one location for alignment, so all components align to a single horizontal position at the far left.

##### Decide How Many Columns You Need

Consider the components you plan to include and their horizontal locations relative to each other. Consider how your design will look in landscape and portrait and on different-sized devices. Is your design symmetrical or asymmetrical? Do you want your images aligned to the same position as your headings and body text, or to a different position?

Once you know the general horizontal placements you need, imagine overlaying equal-width columns on your design. How many equal columns do you need to get all the horizontal alignments you want for your design?

Layouts with 5 to 20 columns provide enough flexibility to support most designs. If you create a layout with fewer than 5 columns, Apple News Format may not have enough information to maintain your intended design on smaller devices. A layout with 7 columns usually provides enough layout information to resize your design for iPad, iPhone, Mac, and Apple Vision Pro. A layout with 20 columns helps with readability and results in a better user experience.

##### Understand Automatic Resizing

News uses this column system when it automatically scales down your article for people to read on smaller screens. It takes the number of columns you specified for your layout along with the width of your article to determine an optimal column width. Then, on smaller devices, it automatically uses fewer columns. Consider the following figures.

The first figure shows an article on three different devices. In this example, there are 10 columns on the iPad Pro, 7 on the iPad in portrait, and 3 on the iPhone in portrait.

![Screenshots showing the layout of an article on iPad Pro, iPad, and iPhone.](https://docs-assets.developer.apple.com/published/c5704ae71cfad5437b2b0484597cbb1b/media-4087466%402x.png)

![Screenshots showing the layout of an article with fewer columns on iPad Pro, iPad, and iPhone. ](https://docs-assets.developer.apple.com/published/a11d6a46e5a1107ea711964c44b5b0d1/media-4087467%402x.png)

The News app doesn’t scale up. The number of columns decreases on narrower displays, but never increases. In the previous figure, the layout with 7 columns designed for iPad in landscape still has 7 columns on iPad Pro —even though iPad Pro has an extra 300 points in landscape. News doesn’t increase the number of columns, but instead increases the margins on the left and right sides. The width of the gutter between columns remains fixed.

##### Set Up the Layout for Your Article

To set the layout for your article, use a [`Layout`](https://developer.apple.com/documentation/applenewsformat/layout) object to specify the following:

- `columns`. Default: 7. Number of columns in the article.
- `width`. Default: 1024 pts. Width the article is designed for in points (iPad in landscape orientation).
- `margin`. Default: 60 pts each. Size of the left and right margin in points.
- `gutter`. Default: 20 pts. Gutter width in points.

The following figure shows an article that uses the default values. With 7 columns and a 60-point margin on each side, this layout offers flexibility for a variety of designs and easily scales down to iPhones.

![Labeled screenshot of an article layout that conforms to the rules for article layout.](https://docs-assets.developer.apple.com/published/3bc53dc195e7f19be2df6cd99d3c0a3d/media-4099658%402x.png)

Your next step is to position each component. See [`Positioning the Content in Your Article`](positioning-the-content-in-your-article.md).

## See Also

- [Creating a Floating Caption](creating-a-floating-caption.md)
  Position a caption in the wide right margin of your article.
- [Creating a Sidebar](creating-a-sidebar.md)
  Create a box with an HTML bulleted list in the margin.
- [Positioning the Content in Your Article](positioning-the-content-in-your-article.md)
  Align article components with columns in your layout.
- [Wrapping Text Around a Component](wrapping-text-around-a-component.md)
  Define the layout of a text component to wrap around another component.
- [object Layout](../applenewsformat/layout.md)
  The object for defining columns, gutters, and margins for your article’s designed width.
- [object ComponentLayout](../applenewsformat/componentlayout.md)
  The object for defining the positioning for a specific component within the article’s column system.
- [object Anchor](../applenewsformat/anchor.md)
  The object for anchoring one component to another component in your article’s layout.
- [object Margin](../applenewsformat/margin.md)
  The object for defining the space above and below a component.
- [object AutoPlacementLayout](../applenewsformat/autoplacementlayout.md)
  The object for defining the margin above and below advertising components.
- [object AdvertisingLayout](../applenewsformat/advertisinglayout.md)
  The object for defining the margin above and below advertising components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applenews/planning-the-layout-for-your-article)*