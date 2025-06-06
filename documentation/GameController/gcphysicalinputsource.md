# GCPhysicalInputSource

**Framework**: Game Controller  
**Kind**: protocol

A protocol for a description of an element without any system-level remapping of the controls.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
protocol GCPhysicalInputSource : NSObjectProtocol
```

#### Overview

If necessary, use the properties in this protocol to get the actual input element aliases, localized name, and symbols without the user’s remapping of the controls in the System Game Controller settings. Otherwise, use the [`localizedName`](gcphysicalinputelement/localizedname.md) and [`sfSymbolsName`](gcphysicalinputelement/sfsymbolsname.md) in the [`GCPhysicalInputElement`](gcphysicalinputelement.md) protocol in your interface.

## Topics

### Getting a localized name
- [var elementLocalizedName: String?](gcphysicalinputsource/elementlocalizedname.md)
  The localized name for the element without any system-level remapping of the controls.
### Displaying a symbol
- [var sfSymbolsName: String?](gcphysicalinputsource/sfsymbolsname.md)
  A system symbol for the element without any system-level remapping of the controls.
### Accessing elements by key
- [var elementAliases: Set<String>](gcphysicalinputsource/elementaliases.md)
  The element’s true aliases without any system-level remapping of the controls.
### Getting directions
- [var direction: GCPhysicalInputSourceDirection](gcphysicalinputsource/direction.md)
  The directional input, if any, that a physical input source involves.
- [struct GCPhysicalInputSourceDirection](gcphysicalinputsourcedirection.md)
  The directions that a physical input source involves.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputsource)*