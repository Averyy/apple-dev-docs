# AUGenericViewDisplayFlags

**Framework**: CoreAudioKit  
**Kind**: struct  
**Role**: Structure

Flags that describe the display of a generic view.

**Availability**:
- macOS

## Declaration

```swift
struct AUGenericViewDisplayFlags
```

```c
enum AUGenericViewDisplayFlags : UInt32;
```

## Topics

### Display Flags
- [static var viewParametersDisplayFlag: AUGenericViewDisplayFlags](./augenericviewdisplayflags/viewparametersdisplayflag.md)
  If set, the generic view displays the audio unit parameters of the audio unit.
- [static var viewPropertiesDisplayFlag: AUGenericViewDisplayFlags](./augenericviewdisplayflags/viewpropertiesdisplayflag.md)
  If set, the generic view displays the audio unit properties of the audio unit.
- [static var viewTitleDisplayFlag: AUGenericViewDisplayFlags](./augenericviewdisplayflags/viewtitledisplayflag.md)
  If set, the generic view displays the title and manufacturer of the audio unit.
### Initializers
- [init(rawValue: UInt32)](./augenericviewdisplayflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/augenericviewdisplayflags)*