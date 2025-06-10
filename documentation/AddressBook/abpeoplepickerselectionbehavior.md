# ABPeoplePickerSelectionBehavior

**Framework**: Address Book  
**Kind**: struct

Constants indicating the possible value selection behaviors.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ABPeoplePickerSelectionBehavior
```

#### Overview

These constants are of the type [`ABPeoplePickerSelectionBehavior`](abpeoplepickerselectionbehavior.md) and are used by [`valueSelectionBehavior`](abpeoplepickerview/valueselectionbehavior.md).

## Topics

### Selection Behaviors
- [var ABNoValueSelection: ABPeoplePickerSelectionBehavior](abnovalueselection.md)
  The user cannot select individual values.
- [var ABSingleValueSelection: ABPeoplePickerSelectionBehavior](absinglevalueselection.md)
  The user can select a single value.
- [var ABMultipleValueSelection: ABPeoplePickerSelectionBehavior](abmultiplevalueselection.md)
  The user can select multiple values.
### Initializers
- [init(UInt32)](abpeoplepickerselectionbehavior/init(_:).md)
  Initializes a constant from an integer value that represents a picker selection behavior.
- [init(rawValue: UInt32)](abpeoplepickerselectionbehavior/init(rawvalue:).md)
  Initializes a constant from a raw value that represents a picker selection behavior.
### Instance Properties
- [var rawValue: UInt32](abpeoplepickerselectionbehavior/rawvalue.md)
  The raw integer value of a possible selection behavior constant.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var valueSelectionBehavior: ABPeoplePickerSelectionBehavior](abpeoplepickerview/valueselectionbehavior.md)
  The current selection behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerselectionbehavior)*