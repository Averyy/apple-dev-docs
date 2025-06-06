# inputBusses

**Framework**: Audio Toolbox  
**Kind**: property

An array containing the audio unit’s input connection points.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var inputBusses: AUAudioUnitBusArray { get }
```

#### Discussion

Subclasses must override this property’s getter. The audio unit should return the same object every time it is asked for it, since hosts can install KVO observers on it.

## See Also

- [var outputBusses: AUAudioUnitBusArray](auaudiounit/outputbusses.md)
  An array containing the audio unit’s output connection points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/inputbusses)*