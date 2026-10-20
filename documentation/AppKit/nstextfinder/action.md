# NSTextFinder.Action

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

These constants specify the user interface item tags that correspond find action. These constants are passed to the [`performTextFinderAction(_:)`](../nsresponder/performtextfinderaction%28_%29.md) method, the responder will call the appropriate method for the tag. That method will, in turn, determine the desired action and invoke the appropriate method in the `NSTextFinder` object’s `NSTextFinderClient` protocol.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum Action
```

```c
enum NSTextFinderAction : NSInteger;
```

## Topics

### Constants
- [NSTextFinder.Action.showFindInterface](./action/showfindinterface.md)
  The find bar interface is displayed.
- [NSTextFinder.Action.nextMatch](./action/nextmatch.md)
  The next match, if any, is displayed.
- [NSTextFinder.Action.previousMatch](./action/previousmatch.md)
  The previous match, if any, is displayed.
- [NSTextFinder.Action.replaceAll](./action/replaceall.md)
  All occurrences of the string are replaced.
- [NSTextFinder.Action.replace](./action/replace.md)
  Replaces a single instance of the string.
- [NSTextFinder.Action.replaceAndFind](./action/replaceandfind.md)
  Replaces a single instance of the string and searches for the next match.
- [NSTextFinder.Action.setSearchString](./action/setsearchstring.md)
  Sets the search string.
- [NSTextFinder.Action.replaceAllInSelection](./action/replaceallinselection.md)
  Replaces all occurrences of the string within the current selection.
- [NSTextFinder.Action.selectAll](./action/selectall.md)
  Selects all matching search strings.
- [NSTextFinder.Action.selectAllInSelection](./action/selectallinselection.md)
  Selects all matching search strings within the current selection.
- [NSTextFinder.Action.hideFindInterface](./action/hidefindinterface.md)
  Hides the find bar interface.
- [NSTextFinder.Action.showReplaceInterface](./action/showreplaceinterface.md)
  Displays the find bar interface including the replace functionality.
- [NSTextFinder.Action.hideReplaceInterface](./action/hidereplaceinterface.md)
  Displays the find bar interface including the replace functionality.
### Initializers
- [init?(rawValue: Int)](./action/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [Text Finder Options For The Pasteboard](../text-finder-options-for-the-pasteboard.md)
  The following keys are used for communicating `NSTextFinder` search options via pasteboard. Use the [`textFinderOptions`](../nspasteboard/pasteboardtype/textfinderoptions.md) type
- [NSTextFinder.MatchingType](./matchingtype.md)
  The following constants indicate the type of search anchor an action should perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/action)*