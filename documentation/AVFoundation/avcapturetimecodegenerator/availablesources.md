# availableSources

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of available timecode synchronization sources that can be used by the timecode generator.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var availableSources: [AVCaptureTimecode.Source] { get }
```

```objc
@property (atomic, copy, readonly) NSArray<AVCaptureTimecodeSource *> * availableSources;
```

## Return Value

A read-only array of [`AVCaptureTimecode.Source`](../avcapturetimecode/source.md) objects representing the available timecode synchronization sources.

## Discussion

This property provides a list of [`AVCaptureTimecode.Source`](../avcapturetimecode/source.md) objects representing the available timecode sources with which the generator can synchronize. The sources may include built-in options such as the frame counter and real-time clock, as well as dynamically detected sources such as connected MIDI or HID devices.

This array is key-value observable, allowing you to monitor changes in real-time. For example, when a new MIDI device is connected, the array is updated to include the corresponding timecode source.

## See Also

### Managing sources
- [var currentSource: AVCaptureTimecode.Source](./currentsource.md)
  The active timecode source used by [`AVCaptureTimecodeGenerator`](../avcapturetimecodegenerator.md) to maintain clock synchronization for accurate timecode generation.
- [class var frameCountSource: AVCaptureTimecode.Source](./framecountsource.md)
  A frame counter timecode source that operates independently of any internal or external synchronization.
- [class var realTimeClockSource: AVCaptureTimecode.Source](./realtimeclocksource.md)
  A predefined timecode source synchronized to the real-time system clock.
- [func startSynchronization(source: AVCaptureTimecode.Source)](./startsynchronization%28source%29.md)
  Synchronizes the generator with the specified timecode source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturetimecodegenerator/availablesources)*