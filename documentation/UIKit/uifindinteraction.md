# UIFindInteraction

**Framework**: UIKit  
**Kind**: class

An interaction that provides text finding and replacing operations using a system find panel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIFindInteraction
```

## Mentions

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)

#### Overview

Use a find interaction to add text-finding capabilities to your view.

When invoking the interaction, the system displays a find panel for entering a string to search, with buttons for navigating between results. When supporting replacement, this also includes a field for the text replacing matches. The find panel presents as a part of the onscreen keyboard when visible, or inline as part of the receiver’s view hierarchy.

Input from a hardware keyboard triggers a find interaction using standard system shortcuts such as Command+F for find, Command+G for find next, and Command+Shift+G for find previous. Adding the interaction also enables these commands in the menu bar on macOS when your view becomes first responder. You can also trigger the interaction by calling the [`presentFindNavigator(showingReplace:)`](uifindinteraction/presentfindnavigator(showingreplace:).md) method on the interaction object, providing access to find and replace operations programatically.

Some classes, such as [`UITextView`](uitextview.md), [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView), and [`PDFView`](https://developer.apple.com/documentation/PDFKit/PDFView), support built-in find interactions. To enable the interaction on these views, set [`isFindInteractionEnabled`](uitextview/isfindinteractionenabled.md) to `true`.

```swift
textView.isFindInteractionEnabled = true
```

To add find and replace operations to other views:

1. Create the find interaction object, passing a delegate into the default initializer.
2. Add the interaction by calling the [`addInteraction(_:)`](uiview/addinteraction(_:).md) method on the view.
3. Provide a [`UIFindSession`](uifindsession.md) object to manage the search performed on the content displayed in the view. You return this object through the [`findInteraction(_:sessionFor:)`](uifindinteractiondelegate/findinteraction(_:sessionfor:).md) method on the delegate.

The following example creates a find interaction for a view that presents searchable content for a document.

```swift
let document = Document(string: "")
lazy var interactionView = InteractionView(document: document)

lazy var findInteraction = UIFindInteraction(sessionDelegate: self)

override func viewDidLoad() {
    super.viewDidLoad()

    // Add the find interaction.
    interactionView.addInteraction(findInteraction)
}

func findInteraction(_ interaction: UIFindInteraction, sessionFor view: UIView) -> UIFindSession? {
    // Return a searchable object.
    return UITextSearchingFindSession(searchableObject: document)
}
```

Implement the [`UITextSearching`](uitextsearching-53wjq.md) protocol on the class that encapsulates the searchable content for your view to use an instance of [`UITextSearchingFindSession`](uitextsearchingfindsession.md) as the session object. Alternatively, you can subclass [`UIFindSession`](uifindsession.md) when you want to manage the details of the session using a custom class.

> **Note**:  Session 10071: [`Adopt desktop-class editing interactions`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10071)

 Session 10071: [`Adopt desktop-class editing interactions`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10071)

## Topics

### Creating a find interaction
- [init(sessionDelegate: any UIFindInteractionDelegate)](uifindinteraction/init(sessiondelegate:).md)
  Initializes a find interaction object with the delegate object you specify.
### Managing find interactions
- [var delegate: (any UIFindInteractionDelegate)?](uifindinteraction/delegate.md)
  An object that updates your app’s presentation and provides the session object for managing the interaction’s search.
- [func presentFindNavigator(showingReplace: Bool)](uifindinteraction/presentfindnavigator(showingreplace:).md)
  Begins a search, displaying the find panel.
- [func dismissFindNavigator()](uifindinteraction/dismissfindnavigator.md)
  Dismisses the find panel, if present.
- [func findNext()](uifindinteraction/findnext.md)
  Highlights the next found result in the content, relative to the currently highlighted result.
- [func findPrevious()](uifindinteraction/findprevious.md)
  Highlights the previously found result in the document, relative to the currently highlighted result.
### Configuring the find panel
- [var isFindNavigatorVisible: Bool](uifindinteraction/isfindnavigatorvisible.md)
  A Boolean value that indicates when the find panel displays onscreen.
- [var searchText: String?](uifindinteraction/searchtext.md)
  The search query with which to prepopulate the find panel’s search text field.
- [var replacementText: String?](uifindinteraction/replacementtext.md)
  The replacement string with which to prepopulate the find panel’s replace text field.
- [var optionsMenuProvider: (([UIMenuElement]) -> UIMenu?)?](uifindinteraction/optionsmenuprovider.md)
  A closure that populates the search options for a find interaction.
### Managing the search
- [var activeFindSession: UIFindSession?](uifindinteraction/activefindsession.md)
  The object that manages the state, presentation, and behavior of an active search.
- [func updateResultCount()](uifindinteraction/updateresultcount.md)
  Updates the results the interface displays for the active search.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](uiinteraction.md)

## See Also

- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
  Optimize your iPad app’s user experience by adopting desktop-class enhancements for multitasking with Stage Manager, document interactions, text editing, search, and more.
- [protocol UIFindInteractionDelegate](uifindinteractiondelegate.md)
  A delegate object that provides a session object to manage the search state for a find interaction and receives notifications of search session lifetimes.
- [class UIFindSession](uifindsession.md)
  An abstract base class that manages the state, presentation, and behavior for a search that the find interaction initiates.
- [class UITextSearchingFindSession](uitextsearchingfindsession.md)
  A find session object that wraps a searchable object implementing the text-searching protocol.
- [protocol UITextSearching](uitextsearching-3wkjv.md)
  The methods you use on a find session’s searchable objects to perform search operations and decorate the found text results.
- [class UITextSearchOptions](uitextsearchoptions.md)
  An object containing the configurable options for a text search.
- [enum UITextSearchFoundTextStyle](uitextsearchfoundtextstyle.md)
  Constants that describe the style a find session uses to decorate the text.
- [UITextSearchOptions.WordMatchMethod](uitextsearchoptions/wordmatchmethod-swift.enum.md)
  Constants that describe the method to use when searching text for words that match a string.
- [UIFindSession.SearchResultDisplayStyle](uifindsession/searchresultdisplaystyle-swift.enum.md)
  Constants that describe the results summary the find panel UI includes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction)*