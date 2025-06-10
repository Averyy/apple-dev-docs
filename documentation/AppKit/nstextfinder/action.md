# NSTextFinder.Action

**Framework**: AppKit  
**Kind**: enum

These constants specify the user interface item tags that correspond find action. These constants are passed to the [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) method, the responder will call the appropriate method for the tag. That method will, in turn, determine the desired action and invoke the appropriate method in the `NSTextFinder` object’s `NSTextFinderClient` protocol.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum Action
```

## Topics

### Constants
- [NSTextFinder.Action.showFindInterface](nstextfinder/action/showfindinterface.md)
  The find bar interface is displayed.
- [NSTextFinder.Action.nextMatch](nstextfinder/action/nextmatch.md)
  The next match, if any, is displayed.
- [NSTextFinder.Action.previousMatch](nstextfinder/action/previousmatch.md)
  The previous match, if any, is displayed.
- [NSTextFinder.Action.replaceAll](nstextfinder/action/replaceall.md)
  All occurrences of the string are replaced.
- [NSTextFinder.Action.replace](nstextfinder/action/replace.md)
  Replaces a single instance of the string.
- [NSTextFinder.Action.replaceAndFind](nstextfinder/action/replaceandfind.md)
  Replaces a single instance of the string and searches for the next match.
- [NSTextFinder.Action.setSearchString](nstextfinder/action/setsearchstring.md)
  Sets the search string.
- [NSTextFinder.Action.replaceAllInSelection](nstextfinder/action/replaceallinselection.md)
  Replaces all occurrences of the string within the current selection.
- [NSTextFinder.Action.selectAll](nstextfinder/action/selectall.md)
  Selects all matching search strings.
- [NSTextFinder.Action.selectAllInSelection](nstextfinder/action/selectallinselection.md)
  Selects all matching search strings within the current selection.
- [NSTextFinder.Action.hideFindInterface](nstextfinder/action/hidefindinterface.md)
  Hides the find bar interface.
- [NSTextFinder.Action.showReplaceInterface](nstextfinder/action/showreplaceinterface.md)
  Displays the find bar interface including the replace functionality.
- [NSTextFinder.Action.hideReplaceInterface](nstextfinder/action/hidereplaceinterface.md)
  Displays the find bar interface including the replace functionality.
### Initializers
- [init?(rawValue: Int)](nstextfinder/action/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Text Finder Options For The Pasteboard](text-finder-options-for-the-pasteboard.md)
  The following keys are used for communicating `NSTextFinder` search options via pasteboard. Use the [`textFinderOptions`](nspasteboard/pasteboardtype/textfinderoptions.md) type
- [NSTextFinder.MatchingType](nstextfinder/matchingtype.md)
  The following constants indicate the type of search anchor an action should perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/action)*