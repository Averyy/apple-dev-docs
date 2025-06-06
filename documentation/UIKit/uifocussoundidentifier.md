# UIFocusSoundIdentifier

**Framework**: UIKit  
**Kind**: struct

An identifier for a focus-related sound.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct UIFocusSoundIdentifier
```

## Mentions

- [Using custom sounds for focus movement](using-custom-sounds-for-focus-movement.md)

#### Overview

To assign an identifier to a custom sound file, call the [`register(_:forSoundIdentifier:)`](uifocussystem/register(_:forsoundidentifier:).md) method of [`UIFocusSystem`](uifocussystem.md).

## Topics

### Constants
- [static let `default`: UIFocusSoundIdentifier](uifocussoundidentifier/default.md)
  The identifier for the default system sound to play during focus updates.
- [static let none: UIFocusSoundIdentifier](uifocussoundidentifier/none.md)
  The identifier for disabling sound during a focus update.
### Initializers
- [init(String)](uifocussoundidentifier/init(_:).md)
  Creates an identifier for a focus sound.
- [init(rawValue: String)](uifocussoundidentifier/init(rawvalue:).md)
  Creates an identifier for a focus sound with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Using custom sounds for focus movement](using-custom-sounds-for-focus-movement.md)
  Customize the sounds users hear when focus moves.
- [func soundIdentifierForFocusUpdate(in: UIFocusUpdateContext) -> UIFocusSoundIdentifier?](uifocusenvironment/soundidentifierforfocusupdate(in:).md)
  Asks the delegate for the identifier of the sound to play when the object gains focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussoundidentifier)*