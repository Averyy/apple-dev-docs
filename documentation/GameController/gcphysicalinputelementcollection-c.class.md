# GCPhysicalInputElementCollection

**Framework**: Game Controller  
**Kind**: class  
**Role**: Class

A collection of physical input elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
@interface GCPhysicalInputElementCollection : NSObject
```

## Topics

### Getting elements in the collection
- [- elementEnumerator](./gcphysicalinputelementcollection-c.class/elementenumerator.md)
  Returns an enumerator to iterate the elements in the collection.
- [count](./gcphysicalinputelementcollection-c.class/count.md)
  The number of elements in the collection.
### Accessing elements by key and alias
- [- objectForKeyedSubscript:](./gcphysicalinputelementcollection-c.class/objectforkeyedsubscript_.md)
  Returns the element in the collection for the specified key.
- [- elementForAlias:](./gcphysicalinputelementcollection-c.class/elementforalias_.md)
  Returns the element in the collection that uses the specified alias.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSFastEnumeration](../Foundation/nsfastenumeration.md)

## See Also

### Elements
- [protocol GCPhysicalInputElement](./gcphysicalinputelement.md)
  The common properties of physical input elements.
- [protocol GCButtonElement](./gcbuttonelement.md)
  The common properties of an element that represents a momentary switch, such as a push button.
- [protocol GCAxisElement](./gcaxiselement.md)
  The common properties for an element that represents an absolute or relative input value along an axis.
- [protocol GCSwitchElement](./gcswitchelement.md)
  The common properties for an element that represents a switch.
- [protocol GCDirectionPadElement](./gcdirectionpadelement.md)
  The common properties of elements that represent directional pads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputelementcollection-c.class)*