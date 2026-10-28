# ABPeoplePickerSelectionBehavior

**Framework**: Address Book  
**Kind**: struct  
**Role**: Structure

Constants indicating the possible value selection behaviors.

**Availability**:
- macOS

## Declaration

```swift
struct ABPeoplePickerSelectionBehavior
```

```c
typedef enum { ... } ABPeoplePickerSelectionBehavior;
```

## Overview

These constants are of the type [`ABPeoplePickerSelectionBehavior`](./abpeoplepickerselectionbehavior.md) and are used by [`valueSelectionBehavior`](./abpeoplepickerview/valueselectionbehavior.md).

## Topics

### Selection Behaviors
- [var ABNoValueSelection: ABPeoplePickerSelectionBehavior](./abnovalueselection.md)
  The user cannot select individual values.
- [var ABSingleValueSelection: ABPeoplePickerSelectionBehavior](./absinglevalueselection.md)
  The user can select a single value.
- [var ABMultipleValueSelection: ABPeoplePickerSelectionBehavior](./abmultiplevalueselection.md)
  The user can select multiple values.
### Initializers
- [init(UInt32)](./abpeoplepickerselectionbehavior/init%28_%29.md)
  Initializes a constant from an integer value that represents a picker selection behavior.
- [init(rawValue: UInt32)](./abpeoplepickerselectionbehavior/init%28rawvalue%29.md)
  Initializes a constant from a raw value that represents a picker selection behavior.
### Instance Properties
- [var rawValue: UInt32](./abpeoplepickerselectionbehavior/rawvalue.md)
  The raw integer value of a possible selection behavior constant.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Specifying Selection Behavior
- [var valueSelectionBehavior: ABPeoplePickerSelectionBehavior](./abpeoplepickerview/valueselectionbehavior.md)
  The current selection behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerselectionbehavior)*