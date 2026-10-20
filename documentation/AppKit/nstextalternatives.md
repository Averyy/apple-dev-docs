# NSTextAlternatives

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A list of alternative strings for a piece of text.

**Availability**:
- macOS 10.8+

## Declaration

```swift
class NSTextAlternatives
```

```objc
@interface NSTextAlternatives : NSObject
```

#### Overview

[`NSTextAlternatives`](./nstextalternatives.md) is an immutable value class that stores a list of alternatives for a piece of text and communicates the user’s selection of an alternative via a notification to your app. To support dictation, for example, you might use [`NSTextAlternatives`](./nstextalternatives.md) to present a list of alternative interpretations for a word or phrase the user speaks. If the user chooses to replace the initial interpretation with an alternative, [`NSTextAlternatives`](./nstextalternatives.md) notifies you of the choice so that you can update the text appropriately.

[`NSTextAlternatives`](./nstextalternatives.md) instances are attached to attributed strings as the value of a text attribute, [`NSTextAlternativesAttributeName`](./nstextalternativesattributename.md).

## Topics

### Initializing a Text Alternatives Object
- [init(primaryString: String, alternativeStrings: [String])](./nstextalternatives/init%28primarystring,alternativestrings%29.md)
  Initializes an `NSTextAlternatives` instance.
### Storing Alternative Text Strings
- [var primaryString: String](./nstextalternatives/primarystring.md)
  The text that was initially chosen as the input string.
- [var alternativeStrings: [String]](./nstextalternatives/alternativestrings.md)
  An array of alternative possible interpretations that the user might select.
### Selecting an Alternative String
- [func noteSelectedAlternativeString(String)](./nstextalternatives/noteselectedalternativestring%28_%29.md)
  Sent to the `NSTextAlternatives` object by the text view when the user chooses one of the alternative strings.
### Notifications
- [class let selectedAlternativeStringNotification: NSNotification.Name](./nstextalternatives/selectedalternativestringnotification.md)
  Posted when the user selects an alternate string.
### Structures
- [NSTextAlternatives.SelectedAlternativeStringMessage](./nstextalternatives/selectedalternativestringmessage.md)
### Initializers
- [init?(coder: NSCoder)](./nstextalternatives/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Text input
- [Adopting the system text cursor in custom text views](./adopting-the-system-text-cursor-in-custom-text-views.md)
  Incorporate the system text cursor into your custom text UI in AppKit.
- [class NSTextInputContext](./nstextinputcontext.md)
  An object that represents the Cocoa text input system.
- [protocol NSTextInputClient](./nstextinputclient.md)
  A set of methods that text views need to implement to interact properly with the text input management system.
- [protocol NSTextContent](./nstextcontent.md)
  A protocol that describes specific kinds of input content types.
- [class NSTextInsertionIndicator](./nstextinsertionindicator.md)
  A view that represents the insertion indicator in text.
- [NSTextInsertionIndicator.DisplayMode](./nstextinsertionindicator/displaymode-swift.enum.md)
  Constants that determine how to display the system text cursor in a custom text UI.
- [NSTextInsertionIndicator.AutomaticModeOptions](./nstextinsertionindicator/automaticmodeoptions-swift.struct.md)
  Options that affect the automatic display mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextalternatives)*