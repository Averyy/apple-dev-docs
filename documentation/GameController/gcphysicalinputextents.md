# GCPhysicalInputExtents

**Framework**: Game Controller  
**Kind**: protocol

Physical extents scale the normalized value reported by `GCLinearInput` into physical units.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+

## Declaration

```swift
protocol GCPhysicalInputExtents : NSObjectProtocol
```

## Topics

### Instance Properties
- [var maximumValue: Double](gcphysicalinputextents/maximumvalue.md)
  The maximum value for the physical extent of the input.
- [var minimumValue: Double](gcphysicalinputextents/minimumvalue.md)
  The minimum value for the physical extent of the input.
- [var scaledValue: Double](gcphysicalinputextents/scaledvalue.md)
  The value of the input, scaled into physical units.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputextents)*