# soundIdentifierForFocusUpdate(in:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the identifier of the sound to play when the object gains focus.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
@MainActor
optional func soundIdentifierForFocusUpdate(in context: UIFocusUpdateContext) -> UIFocusSoundIdentifier?
```

## Mentions

- [Using custom sounds for focus movement](using-custom-sounds-for-focus-movement.md)

#### Return Value

The identifier of the sound to be played. Return `nil` if you want to let the parent focus environment determine which sound to play.

#### Discussion

Use this method to return a custom sound when the focus environment object gains focus. Return [`default`](uifocussoundidentifier/default.md) to play the default system sound, or return [`none`](uifocussoundidentifier/none.md) to avoid playing a sound altogether. If you previously registered custom sounds using the [`register(_:forSoundIdentifier:)`](uifocussystem/register(_:forsoundidentifier:).md) method of [`UIFocusSystem`](uifocussystem.md), you may also return an identifier for a sound that you registered.

If you do not implement this method, the system assumes a `nil` return value. If no ancestor environment defines a custom sound, the system plays the [`default`](uifocussoundidentifier/default.md) sound.

> ❗ **Important**:  You must register custom sounds before returning the associated identifiers from this method. Returning an identifier that is unknown to UIKit will result in an assertion failure and an immediate crash.

 You must register custom sounds before returning the associated identifiers from this method. Returning an identifier that is unknown to UIKit will result in an assertion failure and an immediate crash.

## Parameters

- `context`: The context object associated with the update.

## See Also

- [Using custom sounds for focus movement](using-custom-sounds-for-focus-movement.md)
  Customize the sounds users hear when focus moves.
- [struct UIFocusSoundIdentifier](uifocussoundidentifier.md)
  An identifier for a focus-related sound.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/soundidentifierforfocusupdate(in:))*