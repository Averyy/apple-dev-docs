# TVML

**Framework**: Tvml

Use Apple TV Markup Language to create individual pages inside of a client-server app.

> **Note**: TVML is deprecated in tvOS 18 and later. Instead, develop apps for tvOS with [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI) or [`UIKit`](https://developer.apple.com/documentation/UIKit).

#### Overview

Every page in a client-server app is built on an Apple TV Markup Language (TVML) template. TVML templates define what elements can be used and in what order. Each template is designed to display information in a specific way. For example, `loadingTemplate` shows a spinner and a quick description of what is happening, while `ratingTemplate` shows the rating for a product. You create a new TVML file that contains a single template for each page in a client-server app. Each template page occupies the entire TV screen.

Each template page uses compound and simple elements. Compound elements contain other elements, while simple elements are single lines of TVML. Elements contain the information and images that are displayed on the screen.

Every template has a default presentation theme associated with it. You can set a specific theme for your app setting [`UIUserInterfaceStyle`](https://developer.apple.com/documentation/UIKit/UIUserInterfaceStyle) in the `info.plist` file. Themes provide a consistent look inside of a template.

You control the flow of a client-server app through a JavaScript file that is called by your binary app. Your JavaScript file needs to be able to load TVML pages and respond to user input. For more information on available JavaScript APIs, see [`TVMLKit JS`](https://developer.apple.com/documentation/tvmljs).

## Topics

### Full-Page Templates
- [alertTemplate](alerttemplate.md)
  Displays important information to the user.
- [catalogTemplate](catalogtemplate.md)
  Displays groups of items along one side of a page and images of a group’s contents on the other side.
- [compilationTemplate](compilationtemplate.md)
  Displays information about a single media item and its components.
- [descriptiveAlertTemplate](descriptivealerttemplate.md)
  Displays large amounts of important information to the user.
- [divTemplate](divtemplate.md)
  Provides the ability to create pages that don’t conform to a layout defined by another template.
- [formTemplate](formtemplate.md)
  Provides the ability to gather information from the user.
- [listTemplate](listtemplate.md)
  Displays a list of items along one side of a page and the corresponding image on the other side.
- [loadingTemplate](loadingtemplate.md)
  Displays a spinner and description on the screen.
- [mainTemplate](maintemplate.md)
  Displays user options for a media item.
- [menuBarTemplate](menubartemplate.md)
  Creates a page with items along the top and related information below.
- [oneupTemplate](oneuptemplate.md)
  Creates a page that allows users to navigate between full-screen images.
- [paradeTemplate](paradetemplate.md)
  Displays a groups of items along one side of a page and scrolling images on the other side.
- [productBundleTemplate](productbundletemplate.md)
  Displays information for a group of related media items.
- [productTemplate](producttemplate.md)
  Displays detailed information about a single product.
- [ratingTemplate](ratingtemplate.md)
  Displays a rating for an item.
- [searchTemplate](searchtemplate.md)
  Searches for a media item based on user input.
- [showcaseTemplate](showcasetemplate.md)
  Displays images the user can navigate between.
- [stackTemplate](stacktemplate.md)
  Displays groups of products.
- [Displaying a Product or Bundle in a Full-Page Template](displaying-a-product-or-bundle-in-a-full-page-template.md)
  Specify scrollable and fixed regions in a product page.
### Compound Elements
- [Background Elements](background-elements.md)
  Control background images and media items that play in the background.
- [Banner and Header Elements](banner-and-header-elements.md)
  Provide initial descriptive information for other elements.
- [Information Elements](information-elements.md)
  Group and display content in the form best suited for the information.
- [Layout Elements](layout-elements.md)
  Organize and display multiple elements in a structured layout.
- [Lockup Elements](lockup-elements.md)
  Combine several elements so that they can be treated as a single element.
### Simple Elements
- [Display Elements](display-elements.md)
  Display a visual element, such as an image, badge, or progress overlay.
- [Multimedia Elements](multimedia-elements.md)
  Provide the user the ability to stream audio and search for information stored on a server.
- [Text Elements](text-elements.md)
  Display text onscreen.
### Styles
- [Color Styles](color-styles.md)
  Provide the ability to customize an element’s color.
- [Text Styles](text-styles.md)
  Change the text characteristics for an element.
- [Element Shaping](element-shaping.md)
  Modify the size and shape of an element.
- [Element Alignment and Spacing](element-alignment-and-spacing.md)
  Modify the alignment and spacing between elements.
- [tv-placeholder](tv-placeholder.md)
  Sets a default image for an `img` or `monogram` element.
- [tv-rating-style](tv-rating-style.md)
  Sets the displayed image for rating a product.
- [tv-transition](tv-transition.md)
  Specifies how an element transitions on and off the screen.
- [tv-text-highlight-style](tv-text-highlight-style.md)
  Specifies how an element looks when it comes into focus.
- [tv-scrollable-bounds-inset](tv-scrollable-bounds-inset.md)
  Creates an unscrollable region of a specified size at the top and bottom of the stack template.
### Attributes
- [Image Attributes](image-attributes.md)
  Retrieve images from a server and specify how they fit into an element.
- [Text Attributes](text-attributes.md)
  Modify how text is displayed, entered, and laid out.
- [Focus Attributes](focus-attributes.md)
  Define how an element acts when it comes into focus.
- [Binding and DOM Manipulation](binding-and-dom-manipulation.md)
  Implement binding and impove DOM manipulation options.
- [Inline Playback](inline-playback.md)
  Set when and how inline playback is initiated.
- [Alignment, Scrolling, and Coloring](alignment-scrolling-and-coloring.md)
  Align elements within a shelf, set how your app reacts to scrolling, and set the overall color scheme for your app.
### Queries
- [Media Queries](media-queries.md)
  Change the look and layout of a page based on the user’s preferences.
- [Data Binding Queries](data-binding-queries.md)
  Compare a value from a JSON file to another value.
### Resource Icons
- [Adding Resource Icons](adding-resource-icons.md)
  Add Apple-provided icons to buttons and as independent images.
- [Button Icons](button-icons.md)
  Icons that indicate the function of a button.
- [Movie Rating Icons (United States)](movie-rating-icons-united-states.md)
  Icons that pertain to United States movie ratings.
- [Television Rating Icons (United States)](television-rating-icons-united-states.md)
  Icons that pertain to United States television ratings.
- [Rating Icons (New Zealand)](rating-icons-new-zealand.md)
  Icons that pertain to New Zealand movie ratings.
- [Rating Icons (United Kingdom)](rating-icons-united-kingdom.md)
  Icons that pertain to United Kingdom movie ratings.
- [Rating Icons (Brazil)](rating-icons-brazil.md)
  Icons that pertain to Brazil movie ratings.
- [Rotten Tomatoes Rating Icons](rotten-tomatoes-rating-icons.md)
  Icons pertaining to the Rotten Tomatoes rating system.
- [Miscellaneous Icons](miscellaneous-icons.md)
  Miscellaneous icons that don’t fall into a specific category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TVML)*