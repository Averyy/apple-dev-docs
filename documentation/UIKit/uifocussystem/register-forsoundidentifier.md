# register(_:forSoundIdentifier:)

**Framework**: UIKit  
**Kind**: method

Registers the specified sound file with the focus engine.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
@MainActor
class func register(_ soundFileURL: URL, forSoundIdentifier identifier: UIFocusSoundIdentifier)
```

## Mentions

- [Using custom sounds for focus movement](using-custom-sounds-for-focus-movement.md)

#### Discussion

Use this method to register custom sounds that you want played in response to focus changes. Register sound files early in your app’s life cycle so that the focus system has time to process those files and make them ready for playback. You must register sound files before attempting to play them.

To play your custom sounds, override the [`soundIdentifierForFocusUpdate(in:)`](uifocusenvironment/soundidentifierforfocusupdate(in:).md) method in the focus-related objects of your interface and return the associated identifier. You can play the standard UIKit sounds or play your custom sounds when the object gains or loses focus.

## Parameters

- `soundFileURL`: A URL specifying the location of a sound file. The sound file must be local to the current device and must not point to a resource on a remote server. Sound files must be less than 30 seconds in length and must be in a format recognized by the system.
- `identifier`: The identifier for the sound. You use this value later to tell the focus engine which sounds you want to play. Do not specify one of the UIKit sound identifiers (such as  ); doing so will cause an immediate assertion failure and crash your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem/register(_:forsoundidentifier:))*