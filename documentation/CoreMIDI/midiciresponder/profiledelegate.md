# profileDelegate

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The profile delegate.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported for CoreMIDI

## Declaration

```swift
var profileDelegate: any MIDICIProfileResponderDelegate { get }
```

```objc
@property (nonatomic, retain, readonly) id<MIDICIProfileResponderDelegate> profileDelegate;
```

## See Also

### Setting a Responder Delegate
- [protocol MIDICIProfileResponderDelegate](../midiciprofileresponderdelegate.md)
  A protocol that defines the methods to respond to MIDI-CI responder life-cycle events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciresponder/profiledelegate)*