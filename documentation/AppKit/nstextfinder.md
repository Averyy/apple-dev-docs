# NSTextFinder

**Framework**: AppKit  
**Kind**: class

An optional search-and-replace find interface inside a view, usually a scroll view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class NSTextFinder
```

#### Overview

The class serves as a controller for the standard Cocoa find bar. The `NSTextFinder` class interacts heavily with a `client` object which supports the [`NSTextFinderClient`](nstextfinderclient.md) protocol. The client object provides access to the content being searched and provides visual feedback for a search operation.

All menu items related to finding (Find…, Find Next, Find Previous, Use Selection for Find, etc.) should have the same action, [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md), which gets sent down the responder chain in the standard method.

> **Note**:  Before OS X v10.7, the default action for these menu items was [`performFindPanelAction(_:)`](nstextview/performfindpanelaction(_:).md). Applications that wish to use OS X v10.7 should adopt the new behavior, if appropriate.

##### Implementing a Find Bar

A responder of [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) is responsible for creating and owning an instance of `NSTextFinder`. Before any other messages are sent to the `NSTextFinder`, you should set its [`client`](nstextfinder/client.md) property to an object which implements the [`NSTextFinderClient`](nstextfinderclient.md) protocol.

Each user interface item used for finding has a different tag value , which corresponds to the appropriate value in [`NSTextFinder.Action`](nstextfinder/action.md). Upon receipt of the  [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) message, the responder should call the following on its `NSTextFinder` instance:

```objc
- (void)performAction:(NSTextFinderAction)action;
```

This method will determine the desired action from the tag and make various callbacks to [`client`](nstextfinder/client.md) to perform that action. These callbacks are defined in the [`NSTextFinderClient`](nstextfinderclient.md) protocol.

Validation occurs by a similar pattern. The responder should implement [`validateUserInterfaceItem(_:)`](nsuserinterfacevalidations/validateuserinterfaceitem(_:).md) and, when the item’s action is the [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) method, it should pass the item’s tag to the following method and return the result:

```objc
- (BOOL)validateAction:(NSTextFinderAction)action;
```

This method will invoke the required client methods to determine what the appropriate response should be. These callbacks are also defined in the [`NSTextFinderClient`](nstextfinderclient.md) protocol.

When an action is performed, the text finder will ask its client for the string to search. There are two ways the client can provide this string. It can either implement the `string` method, and simply return an `NSString` instance, or it can implement the following methods: [`string(at:effectiveRange:endsWithSearchBoundary:)`](nstextfinderclient/string(at:effectiverange:endswithsearchboundary:).md) and [`stringLength()`](nstextfinderclient/stringlength().md).

These methods make it possible to use the text finder with data that cannot be easily or efficiently flattened into a single string. In the first method, the client should return the string which contains the character at the given index in as conceptual concatenation of all strings that are to be searched.

For example, if a client had the strings “The quick”, “brown fox” , “jumped over the lazy”, and “dog”, and a `NSTextFinder` instance requests the string at index 17, then the client should return “brown fox”. If all the strings were concatenated together, this would be the ‘x’ in “fox”. Additionally, the client should return, by-reference through the `outRange` parameter, the effective range of the string that is returned. In this example, the range of “brown fox” is {9, 9}, because, in the imagined concatenation, the substring starts at index 9 and is 9 characters long.

In some cases, it is not desirable for a match to be found which overlaps multiple strings returned by the [`string(at:effectiveRange:endsWithSearchBoundary:)`](nstextfinderclient/string(at:effectiverange:endswithsearchboundary:).md) method. For example, suppose a client has a list of names like “John Doe”, and “Jane Doe”, etc. Normally, if the string is concatenated together like so: “John Doe Jane Doe”, then a search for “Doe Jane” would succeed. To prevent this often undesirable behavior, the client should return [`true`](https://developer.apple.com/documentation/Swift/true), by-reference, through the `outFlag` parameter, when returning each individual string. This indicates that there is a boundary between the current string and the next string that should not be crossed when searching for a match.

One of the two approaches (implementing the `string` method the [`string(at:effectiveRange:endsWithSearchBoundary:)`](nstextfinderclient/string(at:effectiverange:endswithsearchboundary:).md) and [`stringLength()`](nstextfinderclient/stringlength().md) methods) must be implemented by the client or the `NSTextFinder` instance will not function. If all three methods are implemented, [`string(at:effectiveRange:endsWithSearchBoundary:)`](nstextfinderclient/string(at:effectiverange:endswithsearchboundary:).md) will be used by default.

The text finder may require additional information from the [`client`](nstextfinder/client.md) object to perform an action, or it may require the `client` to perform some parts of the action on its behalf. The  methods and properties described in [`Text Finder Client Implementation Requirements`](nstextfinder#Text-Finder-Client-Implementation-Requirements.md) describes the hooks the text finder requires for each of the actions it supports. If the client does not implement one of these methods or properties, then the action that requires it will be disabled.

###### Text Finder Client Implementation Requirements

The text finder’s client may implement the following properties for by the [`validateAction(_:)`](nstextfinder/validateaction(_:).md) method: [`isSelectable`](nstextfinderclient/isselectable.md), [`allowsMultipleSelection`](nstextfinderclient/allowsmultipleselection.md), and `editable`. If any of these properties is not implemented, a value of [`true`](https://developer.apple.com/documentation/Swift/true) is assumed. Returning [`false`](https://developer.apple.com/documentation/Swift/false) from any of these methods will disable the actions that require them. For more information about these properties see [`NSTextFinderClient`](nstextfinderclient.md).

The following implementation’s are required by the text client to support the specified actions:

- The [`NSTextFinderClient`](nstextfinderclient.md) protocol must implement the [`firstSelectedRange`](nstextfinderclient/firstselectedrange.md) property to support the following functionality: [`NSTextFinder.Action.nextMatch`](nstextfinder/action/nextmatch.md), [`NSTextFinder.Action.previousMatch`](nstextfinder/action/previousmatch.md), [`NSTextFinder.Action.replace`](nstextfinder/action/replace.md), [`NSTextFinder.Action.replaceAndFind`](nstextfinder/action/replaceandfind.md), and [`NSTextFinder.Action.setSearchString`](nstextfinder/action/setsearchstring.md) actions. The `client` implementation of [`firstSelectedRange`](nstextfinderclient/firstselectedrange.md) needs to return its first selected range, or {index, 0} to indicate the location of the insertion point if there is no selection.
- The [`selectedRanges`](nstextfinderclient/selectedranges.md) property is required for the [`NSTextFinder.Action.replaceAllInSelection`](nstextfinder/action/replaceallinselection.md), [`NSTextFinder.Action.selectAll`](nstextfinder/action/selectall.md), and [`NSTextFinder.Action.selectAllInSelection`](nstextfinder/action/selectallinselection.md) actions. The array should contain `NSRange` structures wrapped in `NSValue` instances.
- The [`scrollRangeToVisible(_:)`](nstextfinderclient/scrollrangetovisible(_:).md) method is used by many actions, but is not strictly required by any to perform correctly.
- The client protocol’s [`shouldReplaceCharacters(inRanges:with:)`](nstextfinderclient/shouldreplacecharacters(inranges:with:).md), [`replaceCharacters(in:with:)`](nstextfinderclient/replacecharacters(in:with:).md) and [`didReplaceCharacters()`](nstextfinderclient/didreplacecharacters().md) methods are used by the [`NSTextFinder.Action.replace`](nstextfinder/action/replace.md), [`NSTextFinder.Action.replaceAll`](nstextfinder/action/replaceall.md), [`NSTextFinder.Action.replaceAllInSelection`](nstextfinder/action/replaceallinselection.md), and [`NSTextFinder.Action.replaceAndFind`](nstextfinder/action/replaceandfind.md) actions. The NSTextFinder instance does not have the ability to directly make changes to the [`client`](nstextfinder/client.md) content, so the `client` is responsible for performing replace operations in these methods.
- Before a replace operation is performed, the `NSTextFinder` instance calls the [`shouldReplaceCharacters(inRanges:with:)`](nstextfinderclient/shouldreplacecharacters(inranges:with:).md) method to determine if a replacement should take place. If it returns [`false`](https://developer.apple.com/documentation/Swift/false), then the given range will not be replaced. If the method returns [`true`](https://developer.apple.com/documentation/Swift/true), or is not implemented, then the `NSTextFinder` instance will call the [`replaceCharacters(in:with:)`](nstextfinderclient/replacecharacters(in:with:).md) method, instructing the `client` to carry out the replacement. Finally, the [`didReplaceCharacters()`](nstextfinderclient/didreplacecharacters().md) method will be called, if implemented, to indicate that the replacement was completed. For [`NSTextFinder.Action.replaceAll`](nstextfinder/action/replaceall.md) actions, these methods may be called multiple times, starting from the end of the string and moving toward the beginning, in order to preserve the indexes of the matches which precede the current one.

##### Incremental Search Support

A common feature used in conjunction with the find bar is incremental search. This feature allows users to find matches immediately as they are typing. In OS X v10.7, the text finder provides this feature for its clients with minimal additional API.

Incremental searching can be enabled by setting the [`isIncrementalSearchingEnabled`](nstextfinder/isincrementalsearchingenabled.md) property [`true`](https://developer.apple.com/documentation/Swift/true). This property alone is sufficient to start searching incrementally.

For improved responsiveness, when a document is sufficiently long, the text finder will search the document in the background. To ensure thread-safety, a client using incremental search must call the [`noteClientStringWillChange()`](nstextfinder/noteclientstringwillchange().md) method before any changes are made to the string provided to the text finder.

During incremental search, all visible matches are highlighted. If the `client` object that conforms to the [`NSTextFinderClient`](nstextfinderclient.md) protocol implements the read-only [`visibleCharacterRanges`](nstextfinderclient/visiblecharacterranges.md) property, then by default a gray overlay will appear over your find bar container’s content view with transparent areas for each match. This view should be a superview of all subviews reported by the text finder client. The `NSScrollView` class already implements this property, so you only need to implement this property when using a different container class.

Finally, this mode also requires the same two [`NSTextFinderClient`](nstextfinderclient.md) protocol methods that are used to display the find indicator: [`contentView(at:effectiveCharacterRange:)`](nstextfinderclient/contentview(at:effectivecharacterrange:).md) and [`rects(forCharacterRange:)`](nstextfinderclient/rects(forcharacterrange:).md) be implemented. However, the implementation of these methods is identical for both purposes, so no additional work is required to support incremental search.

##### Replacing Text

The text replacement methods:[`NSTextFinder.Action`](nstextfinder/action.md), [`findIndicatorNeedsUpdate`](nstextfinder/findindicatorneedsupdate.md), and [`validateAction(_:)`](nstextfinder/validateaction(_:).md) are used by the replace, replace all, replace all in section, and replace and find actions.

Before a replace operation is performed, the `NSTextFinder` instance calls the `client` object’s [`NSTextFinder.Action`](nstextfinder/action.md) method to determine if a replacement should take place. If it returns [`false`](https://developer.apple.com/documentation/Swift/false), then the characters in the given ranges will not be replaced. If the method returns [`true`](https://developer.apple.com/documentation/Swift/true), or is not implemented, then the second method, [`findIndicatorNeedsUpdate`](nstextfinder/findindicatorneedsupdate.md), instructing the client to carry out the replacement. Finally, [`validateAction(_:)`](nstextfinder/validateaction(_:).md), if implemented, is invoked to indicate that the replacement was completed.

For replace all actions, these methods will be called multiple times, starting from the last match and moving toward the first, in order to preserve the indexes of the matches which precede the current one.

##### The Text Finder Container

In order to display the find bar, a container for the find bar must be specified. The container is an object that conforms to the [`NSTextFinderBarContainer`](nstextfinderbarcontainer.md) protocol. You specify a find bar container using the following NSTextFinder class’s [`findBarContainer`](nstextfinder/findbarcontainer.md) property.

When a new NSTextFinder instance is created and instructed to display the find bar, it will create a view for the find bar and assign that to the container via the [`NSTextFinderBarContainer`](nstextfinderbarcontainer.md) class’s [`findBarView`](nstextfinderbarcontainer/findbarview.md) property. The container then owns that view and should release it when the container is deallocated. The container should make the find bar visible when the container’s [`isFindBarVisible`](nstextfinderbarcontainer/isfindbarvisible.md) property is set to [`true`](https://developer.apple.com/documentation/Swift/true). The container should implement the [`findBarViewDidChangeHeight()`](nstextfinderbarcontainer/findbarviewdidchangeheight().md) method so it can reposition the find bar when its height changes, usually in response to user action.

> **Note**:  The container is free to modify the width of the find bar view, but it should never modify its height directly.

##### Implementation By Appkit Classes

Two AppKit classes already provide support for the `NSTextFinder` class, including: the [`NSScrollView`](nsscrollview.md) and [`NSTextView`](nstextview.md) classes.

###### Scroll View Support for the Find Bar

The [`NSScrollView`](nsscrollview.md) class conforms to [`NSTextFinderBarContainer`](nstextfinderbarcontainer.md) protocol in order to support the find bar for any document view searched by the find bar. The find bar can be positioned either above or below the document view by assigning one of the values of the [`NSScrollView.FindBarPosition`](nsscrollview/findbarposition-swift.enum.md) constants to the [`findBarPosition`](nsscrollview/findbarposition-swift.property.md) property.

> **Note**:  The actual values for the constants `NSScrollViewFindBarPosition` constants will change from the current values.

###### Text View Support for the Find Bar

The [`NSTextView`](nstextview.md) class also supports the find bar. The find bar can be enabled or disabled on a text view with the [`usesFindBar`](nstextview/usesfindbar.md) property.

Since OS X v10.5, the `NSTextView` class has used an animated find indicator to give feedback to the user about a successful find action. The find indicator could be activated manually on an text view via the [`showFindIndicator(for:)`](nstextview/showfindindicator(for:).md) method.

To provide this functionality for text finder clients in OS X v10.7, the `NSTextFinder` class shows the find indicator at the appropriate time automatically when performing a find. However, text finder needs to know where to show the indicator and it needs assistance in drawing the text contents of the find indicator. During incremental search the `NSTextFinder` class needs also to know the locations of all the visible matches so it can highlight them as well. The following method additions to the `NSTextFinderClient` protocol provide these capabilities: [`contentView(at:effectiveCharacterRange:)`](nstextfinderclient/contentview(at:effectivecharacterrange:).md) and [`rects(forCharacterRange:)`](nstextfinderclient/rects(forcharacterrange:).md).

The [`contentView(at:effectiveCharacterRange:)`](nstextfinderclient/contentview(at:effectivecharacterrange:).md) method is called to determine what view the content is displayed in, that is, over which the find indicator will be displayed. Since content may potentially be spread over multiple views (like the [`NSLayoutManager`](nslayoutmanager.md) class , which supports multiple text views), the method asks for the view at a given index, and the full range of the string that is contained by that view.

In the [`rects(forCharacterRange:)`](nstextfinderclient/rects(forcharacterrange:).md) method, the client should determine and return the rectangles in which the content with the given range is displayed in its `contentView`. The given range is guaranteed not to span multiple content views. The returned rectangles tell the `NSTextFinder` instance where the matched range is found, so it can show the find indicator there.

The `NSTextFinder` and [`NSView`](nsview.md) classes will handle the find indicator correctly when the [`contentView()`](nstextfinderbarcontainer/contentview().md) is resized, moved, or removed from the view hierarchy. If your content view’s scrolling is done by an [`NSScrollView`](nsscrollview.md) object, the find indicator will also be handled for you during scrolling. Beyond these cases, there may be some circumstances where the find indicator should be immediately cancelled and hidden, such as when the view’s content or selection is changed without the knowledge of the text finder . The find indicator can be cancelled using the `NSTextFinder` [`cancelFindIndicator()`](nstextfinder/cancelfindindicator().md) method. If your document is not scrolled by `NSScrollView`, then you should set the [`findIndicatorNeedsUpdate`](nstextfinder/findindicatorneedsupdate.md) property to [`true`](https://developer.apple.com/documentation/Swift/true).

`NSTextFinder` is responsible for drawing the yellow find indicator background bezel, but the view must provide the contents. `NSTextFinder` also sets up a drawing context and causes the content view to draw into it. There are two ways this can happen.

- The `NSTextFinder` instance invokes the `client` object’s [`drawCharacters(in:forContentView:)`](nstextfinderclient/drawcharacters(in:forcontentview:).md) method, if implemented. The client should then draw the requested characters (or ask the containing view to draw the characters, which is provided as a convenience) at the origin of the current context. If the requested character range partially intersects a glyph range, the client may draw the entire glyph, if necessary for performance.
- If [`drawCharacters(in:forContentView:)`](nstextfinderclient/drawcharacters(in:forcontentview:).md) method is not implemented, then the `NSTextFinder` instance uses the normal view drawing mechanisms. The `contentView` does not need take any additional action to make this happen

In OS X v10.7, the [`NSTextView`](nstextview.md) class also provides incremental search support. It is disabled by default, but can be enabled by setting the [`isIncrementalSearchingEnabled`](nstextview/isincrementalsearchingenabled.md) property to [`true`](https://developer.apple.com/documentation/Swift/true). Also, because incremental searching requires the find bar, [`usesFindBar`](nstextview/usesfindbar.md) must be set to [`true`](https://developer.apple.com/documentation/Swift/true) for incremental searching to be occur.

## Topics

### Initializing the Text Finder
- [init()](nstextfinder/init.md)
  Initializes and returns a new `NSTextFinder` instance.
### Validating and Performing Text Finding
- [func performAction(NSTextFinder.Action)](nstextfinder/performaction(_:).md)
  Performs the specified text finding action.
- [func validateAction(NSTextFinder.Action) -> Bool](nstextfinder/validateaction(_:).md)
  Allows validation of the find action before performing.
- [func cancelFindIndicator()](nstextfinder/cancelfindindicator.md)
  Cancels the find indicator immediately.
### Getting the Find Bar Container
- [var findBarContainer: (any NSTextFinderBarContainer)?](nstextfinder/findbarcontainer.md)
  Specifies the find bar container.
### Getting and Setting the Find Bar Client
- [var client: (any NSTextFinderClient)?](nstextfinder/client.md)
  The object that provides the target search string, find bar location, and feedback methods.
### Noting Changes in the Original Content
- [func noteClientStringWillChange()](nstextfinder/noteclientstringwillchange.md)
  Invoke this method when the searched content will change.
### Updating the Find Indicator
- [var findIndicatorNeedsUpdate: Bool](nstextfinder/findindicatorneedsupdate.md)
  Invoke to specify that the find indicator needs updating when not contained within a scroll view.
### Incremental Search Configuration
- [class func drawIncrementalMatchHighlight(in: NSRect)](nstextfinder/drawincrementalmatchhighlight(in:).md)
  Override this method to draw custom highlighting.
- [var incrementalMatchRanges: [NSValue]](nstextfinder/incrementalmatchranges.md)
  Array of incremental search matches posted on the main queue, which have been found during a background search.
- [var isIncrementalSearchingEnabled: Bool](nstextfinder/isincrementalsearchingenabled.md)
  Determines if incremental searching is enabled.
- [var incrementalSearchingShouldDimContentView: Bool](nstextfinder/incrementalsearchingshoulddimcontentview.md)
  Determines the type of incremental search feedback to be presented
### Constants
- [NSTextFinder.Action](nstextfinder/action.md)
  These constants specify the user interface item tags that correspond find action. These constants are passed to the [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) method, the responder will call the appropriate method for the tag. That method will, in turn, determine the desired action and invoke the appropriate method in the `NSTextFinder` object’s `NSTextFinderClient` protocol.
- [Text Finder Options For The Pasteboard](text-finder-options-for-the-pasteboard.md)
  The following keys are used for communicating `NSTextFinder` search options via pasteboard. Use the [`textFinderOptions`](nspasteboard/pasteboardtype/textfinderoptions.md) type
- [NSTextFinder.MatchingType](nstextfinder/matchingtype.md)
  The following constants indicate the type of search anchor an action should perform.
### Initializers
- [init(coder: NSCoder)](nstextfinder/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSTextFinderBarContainer](nstextfinderbarcontainer.md)
  A protocol that provides a container in which the find bar is displayed.
- [protocol NSTextFinderClient](nstextfinderclient.md)
  A set of methods implemented by objects that support searching using the [`NSTextFinder`](nstextfinder.md) class and the in-window text find bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder)*