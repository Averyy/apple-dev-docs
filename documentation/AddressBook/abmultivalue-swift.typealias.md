# ABMultiValue

**Framework**: Address Book  
**Kind**: typealias  
**Role**: Type Alias

A reference to an `ABMultiValue` or `ABMutableMultiValueobject`.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS

> **Deprecated**: use NSArray of CNLabeledValue

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
typealias ABMultiValue = CFTypeRef
```

*macOS*

```swift
class ABMultiValueRef
```

*iOS, iPadOS, Mac Catalyst*

```c
typedef CFTypeRef ABMultiValueRef;
```

*macOS*

```c
typedef const struct __ABMultiValue * ABMultiValueRef;
```

## Relationships

### Inherited By
- [ABMutableMultiValue](./abmutablemultivalue-swift.typealias.md)
### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)

## See Also

### Data Types
- [class ABPersonRef](./abpersonref.md)
  A reference to an ABPerson object.
- [class ABGroupRef](./abgroupref.md)
  A reference to an ABGroup object.
- [typealias ABMutableMultiValue](./abmutablemultivalue-swift.typealias.md)
  A reference to an ABMutableMultiValue object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abmultivalue-swift.typealias)*