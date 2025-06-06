# NCWidgetSearchViewController

**Framework**: Notification Center  
**Kind**: class

An object that provides a default search view within a macOS Today widget.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
class NCWidgetSearchViewController
```

#### Overview

The `NCWidgetSearchViewController` class provides a default search view within a Today widget. A search view controller works together with its delegate to perform searches on the user’s input and display results from which a user can choose. To learn about the search view controller delegate methods, see [`NCWidgetSearchViewDelegate`](ncwidgetsearchviewdelegate.md).

When a widget is in editing mode, it can enable search for new content by instantiating an `NCWidgetSearchViewController` object and presenting it using [`present(inWidget:)`](https://developer.apple.com/documentation/AppKit/NSViewController/present(inWidget:)). The search view controller displays the default search field and a list of results. It uses its [`delegate`](ncwidgetsearchviewcontroller/delegate.md) to perform the search itself.

## Topics

### Enabling Search
- [var delegate: (any NCWidgetSearchViewDelegate)?](ncwidgetsearchviewcontroller/delegate.md)
  The search view controller’s delegate or `nil` if the receiver doesn’t have a delegate.
- [protocol NCWidgetSearchViewDelegate](ncwidgetsearchviewdelegate.md)
  The interface for enabling user searches in the search view controller of a macOS Today widget.
### Displaying the Search Interface
- [var searchDescription: String?](ncwidgetsearchviewcontroller/searchdescription.md)
  A localized description of the nature of the search.
- [var searchResultsPlaceholderString: String?](ncwidgetsearchviewcontroller/searchresultsplaceholderstring.md)
  A localized phrase displayed in the results list when no search results are available.
### Displaying Search Results
- [var searchResultKeyPath: String?](ncwidgetsearchviewcontroller/searchresultkeypath.md)
  A key path for the string property to display for each object in the search results array.
- [var searchResults: [Any]?](ncwidgetsearchviewcontroller/searchresults.md)
  An array of search results.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol NCWidgetSearchViewDelegate](ncwidgetsearchviewdelegate.md)
  The interface for enabling user searches in the search view controller of a macOS Today widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller)*