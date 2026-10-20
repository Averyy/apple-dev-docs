# NSTextFinder.MatchingType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The following constants indicate the type of search anchor an action should perform.

**Availability**:
- macOS 10.7+

## Declaration

```swift
enum MatchingType
```

```c
enum NSTextFinderMatchingType : NSInteger;
```

## Topics

### Constants
- [NSTextFinder.MatchingType.contains](./matchingtype/contains.md)
  The match contains the string.
- [NSTextFinder.MatchingType.startsWith](./matchingtype/startswith.md)
  The match begins with the string.
- [NSTextFinder.MatchingType.fullWord](./matchingtype/fullword.md)
  The match exactly matches the string.
- [NSTextFinder.MatchingType.endsWith](./matchingtype/endswith.md)
  The match ends with the string.
### Initializers
- [init?(rawValue: Int)](./matchingtype/init%28rawvalue%29.md)

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
- [NSTextFinder.Action](./action.md)
  These constants specify the user interface item tags that correspond find action. These constants are passed to the [`performTextFinderAction(_:)`](../nsresponder/performtextfinderaction%28_%29.md) method, the responder will call the appropriate method for the tag. That method will, in turn, determine the desired action and invoke the appropriate method in the `NSTextFinder` object’s `NSTextFinderClient` protocol.
- [Text Finder Options For The Pasteboard](../text-finder-options-for-the-pasteboard.md)
  The following keys are used for communicating `NSTextFinder` search options via pasteboard. Use the [`textFinderOptions`](../nspasteboard/pasteboardtype/textfinderoptions.md) type


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinder/matchingtype)*