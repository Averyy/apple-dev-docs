# TV Services

**Framework**: TV Services  
**Kind**: module

Display content and descriptions, provide channel guides, and support multiple users on Apple TV.

**Availability**:
- tvOS 9.0+

#### Overview

Use the TVServices framework to display content prominently on the screen and to speed up user login. You can highlight media and other information from your app in the . For example, a video playback app might show the user’s most recently viewed videos. The system displays your media items when the user selects your app on the tvOS Home Screen; your app doesn’t need to be running. You provide top shelf content using a Top Shelf app extension, which you include in the bundle of your tvOS app.

Apps that manage multiple user profiles can accelerate the login process by retaining the profile for each Apple TV user. Apple TV supports multiple user accounts, and these accounts are separate from the profiles your app manages. Mapping the system accounts to your own profiles lets users skip profile selection screens and go straight to their content, which provides a better user experience.

> ❗ **Important**:  Don’t perform memory-intensive operations from your TVServices app extension. The memory limits for app extensions are significantly lower than for apps, and using too much memory might cause the system to terminate your extension. Instead, generate top shelf content and perform other memory-intensive operations on your server.

## Topics

### Top shelf app extensions
- [Building a Full Screen Top Shelf Extension](building-a-full-screen-top-shelf-extension.md)
  Highlight content from your Apple TV application by building a full screen Top Shelf extension.
- [class TVTopShelfContentProvider](tvtopshelfcontentprovider.md)
  The main interface for your Top Shelf app extension, which you use to provide content for the top shelf area of the tvOS Home Screen.
- [Legacy Extension](legacy-extension.md)
  Help users discover your app by providing top shelf content and a description of your tvOS app.
### Carousel content
- [class TVTopShelfCarouselItem](tvtopshelfcarouselitem.md)
  An item containing images, video, and other information that you want to display using a carousel-based interface.
- [class TVTopShelfCarouselContent](tvtopshelfcarouselcontent.md)
  A set of items you present using a carousel-style interface in the top shelf.
### Sectioned and inset content
- [class TVTopShelfSectionedItem](tvtopshelfsectioneditem.md)
  An item to display in a section-based interface.
- [class TVTopShelfItemCollection](tvtopshelfitemcollection.md)
  A group of items that you display together in a sectioned interface in the top shelf.
- [class TVTopShelfSectionedContent](tvtopshelfsectionedcontent.md)
  The set of items you want to present using a section-based interface in the top shelf.
- [class TVTopShelfInsetContent](tvtopshelfinsetcontent.md)
  A set of items to present using an inset-style interface in the top shelf.
### Multiple users
- [Personalizing Your App for Each User on Apple TV](personalizing-your-app-for-each-user-on-apple-tv.md)
  Use account-specific storage to segregate data on a multiuser system.
- [Supporting Multiple Users in Your tvOS App](supporting-multiple-users-in-your-tvos-app.md)
  Store separate data for each user with the new Runs as Current User capability.
- [Mapping Apple TV users to app profiles](mapping-apple-tv-users-to-app-profiles.md)
  Adapt the content of your app for the current viewer by using an entitlement and simplifying sign-in flows.
- [class TVUserManager](tvusermanager.md)
  An object that indicates how to store preferences for multiple people on a shared device.
### Channel guide
- [Providing Channel Navigation](providing-channel-navigation.md)
  Support browsing an electronic program guide (EPG) and changing channels with specialized remote buttons.
- [let TVUserActivityTypeBrowsingChannelGuide: String](tvuseractivitytypebrowsingchannelguide.md)
  An activity for viewing your app’s channel guide.
### Common types
- [class TVTopShelfItem](tvtopshelfitem.md)
  An item that uses an image to represent a movie, show, or other content in the top shelf.
- [class TVTopShelfAction](tvtopshelfaction.md)
  An action to perform in response to user interactions with an item in the top shelf.
- [protocol TVTopShelfContent](tvtopshelfcontent.md)
  The protocol that objects adopt to provide content for the top shelf.
- [class TVTopShelfObject](tvtopshelfobject.md)
  An abstract base class for describing top shelf items and item collections.
### Variables
- [let TVUserActivityTypeBrowsingEntertainmentContent: String](tvuseractivitytypebrowsingentertainmentcontent.md)
  The activity type used to open the main screen of the TV Provider app


---

*[View on Apple Developer](https://developer.apple.com/documentation/TVServices)*