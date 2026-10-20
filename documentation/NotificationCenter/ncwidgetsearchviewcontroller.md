# NCWidgetSearchViewController

**Framework**: Notification Center  
**Kind**: class  
**Role**: Class

An object that provides a default search view within a macOS Today widget.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
class NCWidgetSearchViewController
```

```objc
@interface NCWidgetSearchViewController : NSViewController
```

#### Overview

The `NCWidgetSearchViewController` class provides a default search view within a Today widget. A search view controller works together with its delegate to perform searches on the user’s input and display results from which a user can choose. To learn about the search view controller delegate methods, see [`NCWidgetSearchViewDelegate`](./ncwidgetsearchviewdelegate.md).

When a widget is in editing mode, it can enable search for new content by instantiating an `NCWidgetSearchViewController` object and presenting it using [`present(inWidget:)`](../AppKit/nsviewcontroller/present%28inwidget%29.md). The search view controller displays the default search field and a list of results. It uses its [`delegate`](./ncwidgetsearchviewcontroller/delegate.md) to perform the search itself.

## Topics

### Enabling Search
- [var delegate: (any NCWidgetSearchViewDelegate)?](./ncwidgetsearchviewcontroller/delegate.md)
  The search view controller’s delegate or `nil` if the receiver doesn’t have a delegate.
- [protocol NCWidgetSearchViewDelegate](./ncwidgetsearchviewdelegate.md)
  The interface for enabling user searches in the search view controller of a macOS Today widget.
### Displaying the Search Interface
- [var searchDescription: String?](./ncwidgetsearchviewcontroller/searchdescription.md)
  A localized description of the nature of the search.
- [var searchResultsPlaceholderString: String?](./ncwidgetsearchviewcontroller/searchresultsplaceholderstring.md)
  A localized phrase displayed in the results list when no search results are available.
### Displaying Search Results
- [var searchResultKeyPath: String?](./ncwidgetsearchviewcontroller/searchresultkeypath.md)
  A key path for the string property to display for each object in the search results array.
- [var searchResults: [Any]?](./ncwidgetsearchviewcontroller/searchresults.md)
  An array of search results.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Search View
- [protocol NCWidgetSearchViewDelegate](./ncwidgetsearchviewdelegate.md)
  The interface for enabling user searches in the search view controller of a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller)*