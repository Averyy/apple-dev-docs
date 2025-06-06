# TVUIKit

**Framework**: TVUIKit  
**Kind**: module

Show common user interface elements from Apple TV in your native app.

**Availability**:
- tvOS 12.0+

#### Overview

When you build an app for tvOS with [`UIKit`](https://developer.apple.com/documentation/UIKit), you can use [`TVUIKit`](TVUIKit.md) to refine the display of your content for a TV environment. Use the [`TV Services`](https://developer.apple.com/documentation/TVServices) framework to provide deeper integration between your app and Apple TV.

For more information about combining Apple technologies to build a great Apple TV experience, see [`Planning your tvOS app`](https://developer.apple.comhttps://developer.apple.com/tvos/planning/#build-the-data-structures-youll-use-in-your-app).

![A figure containing a hexagonal UIKit framework icon, an arrow pointing to the right, a hexagon with the label TVUIKit, an arrow pointing to the right, and a TV screen. The TV screen shows a centered image of a palm tree, with other images partially visible on either side of the palm tree.](https://docs-assets.developer.apple.com/published/0ac9f4c161a4bb424a89960bc2d42e7a/media-4133629%402x.png)

## Topics

### Collections of content
- [Creating immersive experiences using a full-screen layout](creating-immersive-experiences-using-a-full-screen-layout.md)
  Display content with a collection view that maximizes the tvOS experience.
- [class TVCollectionViewFullScreenLayout](tvcollectionviewfullscreenlayout.md)
  A collection view layout that organizes items into a browsable, full-screen display format.
- [protocol TVCollectionViewDelegateFullScreenLayout](tvcollectionviewdelegatefullscreenlayout.md)
  Methods that send notifications of events during cell transitions.
- [class TVCollectionViewFullScreenCell](tvcollectionviewfullscreencell.md)
  A full-screen cell to use in full-screen display format.
- [class TVCollectionViewFullScreenLayoutAttributes](tvcollectionviewfullscreenlayoutattributes.md)
  Attributes to manage the appearance of the collection view’s layout.
### Content views
- [class TVMediaItemContentView](tvmediaitemcontentview.md)
  A view that represents media content, such as movies and TV shows.
- [class TVMonogramContentView](tvmonogramcontentview.md)
  A view that contains a circular image of a person or the person’s initials.
### Numeric input
- [class TVDigitEntryViewController](tvdigitentryviewcontroller.md)
  A view controller that enables the user to enter digits, like a passcode, in your app.
### Lockup views
- [class TVLockupView](tvlockupview.md)
  A focusable view that presents main content, like a movie poster, and an optional header and footer.
- [protocol TVLockupViewComponent](tvlockupviewcomponent.md)
  The protocol for responding to lockup view state changes.
- [class TVLockupHeaderFooterView](tvlockupheaderfooterview.md)
  A view that contains header and footer information.
- [class TVCardView](tvcardview.md)
  A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- [class TVPosterView](tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVCaptionButtonView](tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TVUIKit)*