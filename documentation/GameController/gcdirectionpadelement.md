# GCDirectionPadElement

**Framework**: Game Controller  
**Kind**: protocol

The common properties of elements that represent directional pads.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCDirectionPadElement : GCPhysicalInputElement
```

## Topics

### Directional buttons
- [var left: any GCLinearInput & GCPressedStateInput](gcdirectionpadelement/left.md)
  The input object that represents the left button on the directional pad.
- [var right: any GCLinearInput & GCPressedStateInput](gcdirectionpadelement/right.md)
  The input object that represents the right button on the directional pad.
- [var up: any GCLinearInput & GCPressedStateInput](gcdirectionpadelement/up.md)
  The input object that represents the up button on the directional pad.
- [var down: any GCLinearInput & GCPressedStateInput](gcdirectionpadelement/down.md)
  The input object that represents the down button on the directional pad.
### Axes
- [var xAxis: any GCAxisInput](gcdirectionpadelement/xaxis.md)
  The input object that represents the x-axis on the directional pad.
- [var yAxis: any GCAxisInput](gcdirectionpadelement/yaxis.md)
  The input object that represents the y-axis on the directional pad.
- [var xyAxes: any GCAxis2DInput](gcdirectionpadelement/xyaxes.md)
  The location of the directional pad represented as a point.
- [protocol GCAxis2DInput](gcaxis2dinput.md)
  The common properties of inputs that provide a normalized point in a two-dimensional coordinate system with a fixed origin.

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
- [protocol GCSwitchElement](gcswitchelement.md)
  The common properties for an element that represents a switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdirectionpadelement)*