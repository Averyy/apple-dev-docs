# componentManufacturer

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The unique vendor identifier, registered with Apple, for the audio component.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var componentManufacturer: OSType
```

```c
OSType componentManufacturer;
```

## See Also

### Properties
- [var componentType: OSType](./componenttype.md)
  A unique 4-byte code identifying the interface for the component.
- [var componentSubType: OSType](./componentsubtype.md)
  A 4-byte code that you can use to indicate the purpose of a component. For example, you could use `lpas` or `lowp` as a mnemonic indication that an audio unit is a low-pass filter.
- [var componentFlags: UInt32](./componentflags.md)
  Set this value to zero.
- [var componentFlagsMask: UInt32](./componentflagsmask.md)
  Set this value to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentdescription/componentmanufacturer)*