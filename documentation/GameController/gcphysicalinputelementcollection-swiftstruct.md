# GCPhysicalInputElementCollection

**Framework**: Game Controller  
**Kind**: struct

A collection of physical input elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
struct GCPhysicalInputElementCollection<T> where T : GCPhysicalInputElement
```

## Topics

### Accessing elements by name
- [subscript(GCDirectionPadElementName) -> T?](gcphysicalinputelementcollection-swift.struct/subscript(_:)-1twjd.md)
  Accesses a contiguous subrange of a collection of direction pad elements.
- [subscript(GCAxisElementName) -> T?](gcphysicalinputelementcollection-swift.struct/subscript(_:)-8m218.md)
  Accesses a contiguous subrange of a collection of axis elements.
- [subscript(GCButtonElementName) -> T?](gcphysicalinputelementcollection-swift.struct/subscript(_:)-3l6nj.md)
  Accesses a contiguous subrange of a collection of button elements.
- [subscript(GCSwitchElementName) -> T?](gcphysicalinputelementcollection-swift.struct/subscript(_:)-4oje0.md)
  Accesses a contiguous subrange of a collection of switch elements.
- [subscript(GCPhysicalInputElementName) -> T?](gcphysicalinputelementcollection-swift.struct/subscript(_:)-85c13.md)
### Subscripts
- [subscript(String) -> T?](gcphysicalinputelementcollection-swift.struct/subscript(_:)-3tv91.md)
  Accesses a contiguous subrange of the collection’s elements.
- [subscript<Name>(Name) -> Name.PhysicalInputElement?](gcphysicalinputelementcollection-swift.struct/subscript(_:)-3womp.md)
  Accesses the collection’s elements using the element’s name.
- [subscript<Name>(Name) -> (any GCPhysicalInputElement)?](gcphysicalinputelementcollection-swift.struct/subscript(_:)-c5v9.md)
  Accesses the collection’s elements using the element’s name.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [protocol GCPhysicalInputElement](gcphysicalinputelement.md)
  The common properties of physical input elements.
- [protocol GCButtonElement](gcbuttonelement.md)
  The common properties of an element that represents a momentary switch, such as a push button.
- [protocol GCAxisElement](gcaxiselement.md)
  The common properties for an element that represents an absolute or relative input value along an axis.
- [protocol GCSwitchElement](gcswitchelement.md)
  The common properties for an element that represents a switch.
- [protocol GCDirectionPadElement](gcdirectionpadelement.md)
  The common properties of elements that represent directional pads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputelementcollection-swift.struct)*