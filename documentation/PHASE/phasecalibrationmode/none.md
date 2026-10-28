# PHASECalibrationMode.none

**Framework**: PHASE  
**Kind**: case  
**Role**: Case

An option that specifies no loudness calibration.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case none
```

```c
PHASECalibrationModeNone
```

## Discussion

For a consistent user experience across platforms and output devices, avoid [`PHASECalibrationMode.none`](./none.md) by correcting loudness with [`PHASECalibrationMode.absoluteSpl`](./absolutespl.md) or [`PHASECalibrationMode.relativeSpl`](./relativespl.md).

## See Also

### Modes
- [PHASECalibrationMode.absoluteSpl](./absolutespl.md)
  A sound pressure level based on the current output device.
- [PHASECalibrationMode.relativeSpl](./relativespl.md)
  A sound pressure level that’s tuned for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecalibrationmode/none)*