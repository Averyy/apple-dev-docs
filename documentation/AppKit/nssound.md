# NSSound

**Framework**: AppKit  
**Kind**: class

A simple interface for loading and playing audio files.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSSound
```

#### Overview

You create a sound object with an audio file or data, which can be in any format that Core Audio supports. Customize the sound by configuring its properties, such as setting its playback volume and looping behavior. Call the sound’s [`play()`](nssound/play().md) method to begin playback. The system executes this call asynchronously so that it doesn’t interrupt the functioning of your app.

If you want to play the system beep sound, use the [`beep()`](nssound/beep().md) (Swift) or [`NSBeep`](nsbeep.md) (Objective-C) function.

## Topics

### Detecting When a Sound Finishes Playing
- [var delegate: (any NSSoundDelegate)?](nssound/delegate.md)
  The sound’s delegate.
- [protocol NSSoundDelegate](nssounddelegate.md)
  A set of optional methods implemented by delegates of [`NSSound`](nssound.md) objects.
### Creating Sounds
- [class func canInit(with: NSPasteboard) -> Bool](nssound/caninit(with:).md)
  Indicates whether the receiver can create an instance of itself from the data in a pasteboard.
- [init?(contentsOfFile: String, byReference: Bool)](nssound/init(contentsoffile:byreference:).md)
  Initializes the receiver with the audio data located at a given filepath.
- [init?(contentsOf: URL, byReference: Bool)](nssound/init(contentsof:byreference:).md)
  Initializes the receiver with the audio data located at a given URL.
- [init?(data: Data)](nssound/init(data:).md)
  Initializes the receiver with a given audio data.
- [init?(pasteboard: NSPasteboard)](nssound/init(pasteboard:).md)
  Initializes the receiver with data from a pasteboard. The pasteboard should contain a type returned by [`NSSound`](nssound.md). `NSSound` expects the data to have a proper magic number, sound header, and data for the formats it supports.
### Configuring Sounds
- [var name: NSSound.Name?](nssound/name-swift.property.md)
  The name assigned to the sound.
- [typealias Name](nssound/name-swift.typealias.md)
- [func setName(NSSound.Name?) -> Bool](nssound/setname(_:).md)
- [var volume: Float](nssound/volume.md)
  The volume of the sound.
- [var currentTime: TimeInterval](nssound/currenttime.md)
  The sound’s playback progress, in seconds.
- [var loops: Bool](nssound/loops.md)
  A Boolean that indicates whether the sound restarts playback when it reaches the end of its content.
- [var playbackDeviceIdentifier: NSSound.PlaybackDeviceIdentifier?](nssound/playbackdeviceidentifier-swift.property.md)
  Identifies the sound’s output device
- [typealias PlaybackDeviceIdentifier](nssound/playbackdeviceidentifier-swift.typealias.md)
### Getting Sound Information
- [class var soundUnfilteredTypes: [String]](nssound/soundunfilteredtypes.md)
  Provides the file types the `NSSound` class understands.
- [init?(named: NSSound.Name)](nssound/init(named:).md)
  Returns the `NSSound` instance associated with a given name.
- [var duration: TimeInterval](nssound/duration.md)
  The duration of the sound, in seconds.
### Playing Sounds
- [static func beep()](nssound/beep.md)
  Plays the system beep.
- [var isPlaying: Bool](nssound/isplaying.md)
  A Boolean that indicates whether the sound is playing its audio data.
- [func pause() -> Bool](nssound/pause.md)
  Pauses audio playback.
- [func play() -> Bool](nssound/play.md)
  Initiates audio playback.
- [func resume() -> Bool](nssound/resume.md)
  Resumes audio playback.
- [func stop() -> Bool](nssound/stop.md)
  Concludes audio playback.
### Writing Sounds
- [func write(to: NSPasteboard)](nssound/write(to:).md)
  Writes the receiver’s data to a pasteboard.
### Constants
- [NSPasteboard Type for Sound Data](nspasteboard-type-for-sound-data.md)
  The `NSSound` class defines this common pasteboard data type.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSPasteboardReading](nspasteboardreading.md)
- [NSPasteboardWriting](nspasteboardwriting.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Transferable](../CoreTransferable/Transferable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound)*