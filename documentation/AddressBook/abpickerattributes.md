# ABPickerAttributes

**Framework**: Address Book  
**Kind**: typealias  
**Role**: Type Alias

A bitfield used to specify the selection behavior for the values of multi-value properties.

**Availability**:
- macOS

## Declaration

```c
typedef OptionBits ABPickerAttributes;
```

## Discussion

Use the constants listed in [People-Picker Selection Behavior](./people-picker-selection-behavior.md).

When multiple behaviors are selected, the most restrictive behavior is used. The default behavior is single-value selection ([`kABPickerSingleValueSelection`](./kabpickersinglevalueselection.md)).

## See Also

### Miscellaneous
- [typealias ABPropertyType](./abpropertytype.md)
  These are the possible types of ABRecord properties.
- [typealias ABSearchComparison](./absearchcomparison.md)
  Constants used to specify the type of comparison beingmade.
- [typealias ABSearchConjunction](./absearchconjunction.md)
  Constants used to create compound search elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpickerattributes)*