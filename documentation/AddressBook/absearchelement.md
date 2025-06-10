# ABSearchElement

**Framework**: Address Book  
**Kind**: class

An object you use to specify a search query for records in the Address Book database.

**Availability**:
- macOS ?+

## Declaration

```swift
class ABSearchElement
```

#### Overview

The `ABSearchElement` class is “toll-free bridged” with its procedural C opaque-type counterpart. This means that the `ABSearchElementRef` type is interchangeable in function or method calls with instances of the `ABSearchElement` class.

## Topics

### Searching
- [init!(forConjunction: ABSearchConjunction, children: [Any]!)](absearchelement/init(forconjunction:children:).md)
  Returns a compound search element, created by combining the search elements in an array with the given conjunction.
### Matching
- [func matchesRecord(ABRecord!) -> Bool](absearchelement/matchesrecord(_:).md)
  Tests whether or not a record matches a search element.
### Constants
- [typealias ABSearchConjunction](absearchconjunction.md)
  Constants used to create compound search elements.
- [typealias ABSearchComparison](absearchcomparison.md)
  Constants used to specify the type of comparison beingmade.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class ABSearchElementRef](absearchelementref.md)
  A reference to an ABSearchElement object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/absearchelement)*