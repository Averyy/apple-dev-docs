# GCButtonElement

**Framework**: Game Controller  
**Kind**: protocol

The common properties of an element that represents a momentary switch, such as a push button.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCButtonElement : GCPhysicalInputElement
```

## Topics

### Getting input state
- [var touchedInput: (any GCTouchedStateInput)?](gcbuttonelement/touchedinput.md)
  The input object that provides the touch state of the element.
- [var pressedInput: any GCLinearInput & GCPressedStateInput](gcbuttonelement/pressedinput.md)
  The input object that provides the linear and press state of the element.
### Instance Properties
- [var forceInput: (any GCLinearInput)?](gcbuttonelement/forceinput.md)
  Get the input containing the measured force applied to the button.

## Relationships

### Inherits From
- [GCPhysicalInputElement](gcphysicalinputelement.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [struct GCPhysicalInputElementCollection](gcphysicalinputelementcollection-swift.struct.md)
  A collection of physical input elements.
- [protocol GCPhysicalInputElement](gcphysicalinputelement.md)
  The common properties of physical input elements.
- [protocol GCAxisElement](gcaxiselement.md)
  The common properties for an element that represents an absolute or relative input value along an axis.
- [protocol GCSwitchElement](gcswitchelement.md)
  The common properties for an element that represents a switch.
- [protocol GCDirectionPadElement](gcdirectionpadelement.md)
  The common properties of elements that represent directional pads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcbuttonelement)*