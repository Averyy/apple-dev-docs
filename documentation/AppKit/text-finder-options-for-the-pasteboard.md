# Text Finder Options For The Pasteboard

**Framework**: AppKit

The following keys are used for communicating `NSTextFinder` search options via pasteboard. Use the [`textFinderOptions`](nspasteboard/pasteboardtype/textfinderoptions.md) type

## Topics

### Constants
- [static let textFinderCaseInsensitiveKey: NSPasteboard.PasteboardType.TextFinderOptionKey](nspasteboard/pasteboardtype/textfinderoptionkey/textfindercaseinsensitivekey.md)
  A Boolean value indicating whether the search is case insensitive.
- [static let textFinderMatchingTypeKey: NSPasteboard.PasteboardType.TextFinderOptionKey](nspasteboard/pasteboardtype/textfinderoptionkey/textfindermatchingtypekey.md)
  A number object containing the match type to use.

## See Also

- [NSTextFinder.Action](nstextfinder/action.md)
  These constants specify the user interface item tags that correspond find action. These constants are passed to the [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) method, the responder will call the appropriate method for the tag. That method will, in turn, determine the desired action and invoke the appropriate method in the `NSTextFinder` object’s `NSTextFinderClient` protocol.
- [NSTextFinder.MatchingType](nstextfinder/matchingtype.md)
  The following constants indicate the type of search anchor an action should perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/text-finder-options-for-the-pasteboard)*