# PHAssetBurstSelectionType

**Framework**: Photos  
**Kind**: struct  
**Role**: Structure

Bit mask values indicating whether and how an asset is marked as a favorite member of a burst photo sequence. Used by the [`burstSelectionTypes`](./phasset/burstselectiontypes.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct PHAssetBurstSelectionType
```

```c
enum PHAssetBurstSelectionType : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./phassetburstselectiontype/init%28rawvalue%29.md)
  Creates an asset burst selection type from a raw value.
### Constants
- [static var autoPick: PHAssetBurstSelectionType](./phassetburstselectiontype/autopick.md)
  Photos has automatically identified the asset as a potential user favorite.
- [static var userPick: PHAssetBurstSelectionType](./phassetburstselectiontype/userpick.md)
  The user has marked the asset as a favorite member of its burst sequence.
- [PHAssetBurstSelectionTypeNone](./phassetburstselectiontype/phassetburstselectiontypenone.md)
  The asset is not marked as a favorite member of its burst sequence or is not a member of a burst sequence.

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

## See Also

### Working with Burst Photo Assets
- [var burstIdentifier: String?](./phasset/burstidentifier.md)
  The unique identifier shared by photo assets from the same burst sequence.
- [var burstSelectionTypes: PHAssetBurstSelectionType](./phasset/burstselectiontypes.md)
  The selection type of the asset in a burst photo sequence.
- [var representsBurst: Bool](./phasset/representsburst.md)
  A Boolean value that indicates whether the asset is the representative photo from a burst photo sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetburstselectiontype)*