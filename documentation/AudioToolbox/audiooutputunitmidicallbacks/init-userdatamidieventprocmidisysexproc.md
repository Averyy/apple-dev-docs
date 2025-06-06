# init(userData:MIDIEventProc:MIDISysExProc:)

**Framework**: Audio Toolbox  
**Kind**: init

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(userData: UnsafeMutableRawPointer?, MIDIEventProc: (UnsafeMutableRawPointer?, UInt32, UInt32, UInt32, UInt32) -> Void, MIDISysExProc: (UnsafeMutableRawPointer?, UnsafePointer<UInt8>, UInt32) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiooutputunitmidicallbacks/init(userdata:midieventproc:midisysexproc:))*