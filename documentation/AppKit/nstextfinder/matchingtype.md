# NSTextFinder.MatchingType

**Framework**: AppKit  
**Kind**: enum

The following constants indicate the type of search anchor an action should perform.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum MatchingType
```

## Topics

### Constants
- [NSTextFinder.MatchingType.contains](nstextfinder/matchingtype/contains.md)
  The match contains the string.
- [NSTextFinder.MatchingType.startsWith](nstextfinder/matchingtype/startswith.md)
  The match begins with the string.
- [NSTextFinder.MatchingType.fullWord](nstextfinder/matchingtype/fullword.md)
  The match exactly matches the string.
- [NSTextFinder.MatchingType.endsWith](nstextfinder/matchingtype/endswith.md)
  The match ends with the string.
### Initializers
- [init?(rawValue: Int)](nstextfinder/matchingtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [NSTextFinder.Action](nstextfinder/action.md)
  These constants specify the user interface item tags that correspond find action. These constants are passed to the [`performTextFinderAction(_:)`](nsresponder/performtextfinderaction(_:).md) method, the responder will call the appropriate method for the tag. That method will, in turn, determine the desired action and invoke the appropriate method in the `NSTextFinder` object’s `NSTextFinderClient` protocol.
- [Text Finder Options For The Pasteboard](text-finder-options-for-the-pasteboard.md)
  The following keys are used for communicating `NSTextFinder` search options via pasteboard. Use the [`textFinderOptions`](nspasteboard/pasteboardtype/textfinderoptions.md) type


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/matchingtype)*