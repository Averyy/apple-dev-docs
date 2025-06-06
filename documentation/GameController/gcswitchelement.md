# GCSwitchElement

**Framework**: Game Controller  
**Kind**: protocol

The common properties for an element that represents a switch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCSwitchElement : GCPhysicalInputElement
```

## Topics

### Getting input state
- [var positionInput: any GCSwitchPositionInput](gcswitchelement/positioninput.md)
  The input object that provides the position of the switch.

## Relationships

### Inherits From
- [GCPhysicalInputElement](gcphysicalinputelement.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct GCPhysicalInputElementCollection](gcphysicalinputelementcollection-swift.struct.md)
  A collection of physical input elements.
- [protocol GCPhysicalInputElement](gcphysicalinputelement.md)
  The common properties of physical input elements.
- [protocol GCButtonElement](gcbuttonelement.md)
  The common properties of an element that represents a momentary switch, such as a push button.
- [protocol GCAxisElement](gcaxiselement.md)
  The common properties for an element that represents an absolute or relative input value along an axis.
- [protocol GCDirectionPadElement](gcdirectionpadelement.md)
  The common properties of elements that represent directional pads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcswitchelement)*