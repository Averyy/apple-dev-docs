# TVTopShelfProvider

**Framework**: TV Services  
**Kind**: protocol

The interface for providing items to display in the main menu’s Top Shelf user interface on an Apple TV.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
protocol TVTopShelfProvider
```

#### Overview

You adopt this protocol in the principal class of your app’s TV Services extension. Apps that implement this extension can provide dynamic content to the Top Shelf element rather than having the system use the static image submitted with the app. The [`topShelfStyle`](tvtopshelfprovider/topshelfstyle.md) property specifies the interface style you want, and the [`topShelfItems`](tvtopshelfprovider/topshelfitems.md) property specifies the content items to display. Whenever you change the content provided by the extension, post a [`TVTopShelfItemsDidChangeNotification`](tvtopshelfitemsdidchangenotification.md) notification to prompt the system to reload your content.

## Topics

### Implementing TV Services Extension Properties
- [var topShelfItems: [TVContentItem]](tvtopshelfprovider/topshelfitems.md)
  Returns an array of content items to be displayed.
- [var topShelfStyle: TVTopShelfContentStyle](tvtopshelfprovider/topshelfstyle.md)
  The user interface style that should be used to display the content items.
- [enum TVTopShelfContentStyle](tvtopshelfcontentstyle.md)
  An enumerated type used to specify the style in which you want your content to be displayed.
### Notifying the System of Changes
- [static let TVTopShelfItemsDidChange: NSNotification.Name](../Foundation/NSNotification/Name-swift.struct/TVTopShelfItemsDidChange.md)
  A notification to post when your app’s Top Shelf content has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvservices/tvtopshelfprovider)*