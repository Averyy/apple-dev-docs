# localizedTitle

**Framework**: Media Player  
**Kind**: property

A localized string used to describe the context of a command.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 7.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var localizedTitle: String { get set }
```

#### Discussion

Use this property to store the text you want shown to the user in conjunction with this command. For example, you might assign the string “I like this” to this property for the command associated with a Like button. The text you specify is displayed to the user at appropriate times by the system.

## See Also

- [var isActive: Bool](mpfeedbackcommand/isactive.md)
  A Boolean value that indicates whether the feedback’s action is on or off.
- [var localizedShortTitle: String](mpfeedbackcommand/localizedshorttitle.md)
  A shortened version of the string used to describe the context of a command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpfeedbackcommand/localizedtitle)*