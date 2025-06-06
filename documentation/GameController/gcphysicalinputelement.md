# GCPhysicalInputElement

**Framework**: Game Controller  
**Kind**: protocol

The common properties of physical input elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCPhysicalInputElement : NSObjectProtocol
```

## Topics

### Getting a localized name
- [var localizedName: String?](gcphysicalinputelement/localizedname.md)
  The localized name for the element.
### Displaying a symbol
- [var sfSymbolsName: String?](gcphysicalinputelement/sfsymbolsname.md)
  A system symbol for the element.
### Accessing elements by key
- [var aliases: Set<String>](gcphysicalinputelement/aliases.md)
  The element’s aliases to use when accessing it with the subscript notation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [GCAxisElement](gcaxiselement.md)
- [GCButtonElement](gcbuttonelement.md)
- [GCDirectionPadElement](gcdirectionpadelement.md)
- [GCSwitchElement](gcswitchelement.md)
### Conforming Types
- [GCGearShifterElement](gcgearshifterelement.md)
- [GCSteeringWheelElement](gcsteeringwheelelement.md)

## See Also

- [struct GCPhysicalInputElementCollection](gcphysicalinputelementcollection-swift.struct.md)
  A collection of physical input elements.
- [protocol GCButtonElement](gcbuttonelement.md)
  The common properties of an element that represents a momentary switch, such as a push button.
- [protocol GCAxisElement](gcaxiselement.md)
  The common properties for an element that represents an absolute or relative input value along an axis.
- [protocol GCSwitchElement](gcswitchelement.md)
  The common properties for an element that represents a switch.
- [protocol GCDirectionPadElement](gcdirectionpadelement.md)
  The common properties of elements that represent directional pads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputelement)*