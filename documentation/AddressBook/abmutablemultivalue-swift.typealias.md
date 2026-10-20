# ABMutableMultiValue

**Framework**: Address Book  
**Kind**: typealias  
**Role**: Type Alias

A reference to an ABMutableMultiValue object.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use NSMutableArray of CNLabeledValue

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
typealias ABMutableMultiValue = CFTypeRef
```

*macOS*

```swift
class ABMutableMultiValueRef
```

*iOS, iPadOS, Mac Catalyst*

```c
typedef CFTypeRef ABMutableMultiValueRef;
```

*macOS*

```c
typedef struct __ABMultiValue * ABMutableMultiValueRef;
```

## Relationships

### Inherits From
- [ABMultiValue](./abmultivalue-swift.typealias.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Data Types
- [class ABPersonRef](./abpersonref.md)
  A reference to an ABPerson object.
- [class ABGroupRef](./abgroupref.md)
  A reference to an ABGroup object.
- [typealias ABMultiValue](./abmultivalue-swift.typealias.md)
  A reference to an `ABMultiValue` or `ABMutableMultiValueobject`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmutablemultivalue-swift.typealias)*