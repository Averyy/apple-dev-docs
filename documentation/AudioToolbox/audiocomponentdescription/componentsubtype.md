# componentSubType

**Framework**: Audio Toolbox  
**Kind**: property

A 4-byte code that you can use to indicate the purpose of a component. For example, you could use `lpas` or `lowp` as a mnemonic indication that an audio unit is a low-pass filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var componentSubType: OSType
```

## See Also

- [var componentType: OSType](audiocomponentdescription/componenttype.md)
  A unique 4-byte code identifying the interface for the component.
- [var componentManufacturer: OSType](audiocomponentdescription/componentmanufacturer.md)
  The unique vendor identifier, registered with Apple, for the audio component.
- [var componentFlags: UInt32](audiocomponentdescription/componentflags.md)
  Set this value to zero.
- [var componentFlagsMask: UInt32](audiocomponentdescription/componentflagsmask.md)
  Set this value to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/componentsubtype)*