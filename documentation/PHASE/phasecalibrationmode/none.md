# PHASECalibrationMode.none

**Framework**: PHASE  
**Kind**: case

An option that specifies no loudness calibration.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case none
```

#### Discussion

For a consistent user experience across platforms and output devices, avoid [`PHASECalibrationMode.none`](phasecalibrationmode/none.md) by correcting loudness with [`PHASECalibrationMode.absoluteSpl`](phasecalibrationmode/absolutespl.md) or [`PHASECalibrationMode.relativeSpl`](phasecalibrationmode/relativespl.md).

## See Also

- [PHASECalibrationMode.absoluteSpl](phasecalibrationmode/absolutespl.md)
  A sound pressure level based on the current output device.
- [PHASECalibrationMode.relativeSpl](phasecalibrationmode/relativespl.md)
  A sound pressure level that’s tuned for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasecalibrationmode/none)*