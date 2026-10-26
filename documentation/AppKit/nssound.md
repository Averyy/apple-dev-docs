# NSSound

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A simple interface for loading and playing audio files.

**Availability**:
- macOS

## Declaration

```swift
class NSSound
```

```objc
@interface NSSound : NSObject
```

#### Overview

You create a sound object with an audio file or data, which can be in any format that Core Audio supports. Customize the sound by configuring its properties, such as setting its playback volume and looping behavior. Call the sound’s [`play()`](./nssound/play%28%29.md) method to begin playback. The system executes this call asynchronously so that it doesn’t interrupt the functioning of your app.

If you want to play the system beep sound, use the [`beep()`](./nssound/beep%28%29.md) (Swift) or [`NSBeep`](./nsbeep.md) (Objective-C) function.

## Topics

### Detecting When a Sound Finishes Playing
- [var delegate: (any NSSoundDelegate)?](./nssound/delegate.md)
  The sound’s delegate.
- [protocol NSSoundDelegate](./nssounddelegate.md)
  A set of optional methods implemented by delegates of [`NSSound`](./nssound.md) objects.
### Creating Sounds
- [class func canInit(with: NSPasteboard) -> Bool](./nssound/caninit%28with%29.md)
  Indicates whether the receiver can create an instance of itself from the data in a pasteboard.
- [init?(contentsOfFile: String, byReference: Bool)](./nssound/init%28contentsoffile,byreference%29.md)
  Initializes the receiver with the audio data located at a given filepath.
- [init?(contentsOf: URL, byReference: Bool)](./nssound/init%28contentsof,byreference%29.md)
  Initializes the receiver with the audio data located at a given URL.
- [init?(data: Data)](./nssound/init%28data%29.md)
  Initializes the receiver with a given audio data.
- [init?(pasteboard: NSPasteboard)](./nssound/init%28pasteboard%29.md)
  Initializes the receiver with data from a pasteboard. The pasteboard should contain a type returned by [`NSSound`](./nssound.md). `NSSound` expects the data to have a proper magic number, sound header, and data for the formats it supports.
### Configuring Sounds
- [var name: NSSound.Name?](./nssound/name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](./nssound/name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](./nssound/setname%28_%29.md)
- [var volume: Float](./nssound/volume.md)
  The volume of the sound.
- [var currentTime: TimeInterval](./nssound/currenttime.md)
  The sound’s playback progress, in seconds.
- [var loops: Bool](./nssound/loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](./nssound/playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](./nssound/playbackdeviceidentifier-swift.typealias.md)
### Getting Sound Information
- [class var soundUnfilteredTypes: [String]](./nssound/soundunfilteredtypes.md)
  Provides the file types the `NSSound` class understands.
- [init?(named: NSSound.Name)](./nssound/init%28named%29.md)
  Returns the `NSSound` instance associated with a given name.
- [var duration: TimeInterval](./nssound/duration.md)
  The duration of the sound, in seconds.
### Playing Sounds
- [static func beep()](./nssound/beep%28%29.md)
  Plays the system beep.
- [var isPlaying: Bool](./nssound/isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func pause() -> Bool](./nssound/pause%28%29.md)
  Pauses audio playback.
- [func play() -> Bool](./nssound/play%28%29.md)
  Initiates audio playback.
- [func resume() -> Bool](./nssound/resume%28%29.md)
  Resumes audio playback.
- [func stop() -> Bool](./nssound/stop%28%29.md)
  Concludes audio playback.
### Writing Sounds
- [func write(to: NSPasteboard)](./nssound/write%28to%29.md)
  Writes the receiver’s data to a pasteboard.
### Constants
- [NSPasteboard Type for Sound Data](./nspasteboard-type-for-sound-data.md)
  The `NSSound` class defines this common pasteboard data type.
### Initializers
- [init?(coder: NSCoder)](./nssound/init%28coder%29.md)
- [init?(contentsOfURL: URL, byReference: Bool)](./nssound/init%28contentsofurl,byreference%29.md)
- [init?(pasteboardPropertyList: Any, ofType: NSPasteboard.PasteboardType)](./nssound/init%28pasteboardpropertylist,oftype%29.md)
### Deprecated
- [- channelMapping](./nssound/channelmapping.md)
  Provides the receiver’s channel map.
- [- setChannelMapping:](./nssound/setchannelmapping_.md)
  Specifies the receiver’s channel map.
- [+ soundUnfilteredFileTypes](./nssound/soundunfilteredfiletypes.md)
  Provides the list of file types the [`NSSound`](./nssound.md) class understands.
- [+ soundUnfilteredPasteboardTypes](./nssound/soundunfilteredpasteboardtypes.md)
  Provides a list of the pasteboard types that the `NSSound` class can accept.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSPasteboardReading](./nspasteboardreading.md)
- [NSPasteboardWriting](./nspasteboardwriting.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Transferable](../CoreTransferable/transferable.md)

## See Also

### Sounds
- [NSBeep](./nsbeep.md)
  Plays the system beep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound)*