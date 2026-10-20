# ABAddressBookErrorDomain

**Framework**: Address Book  
**Kind**: var  
**Role**: Global Variable

Error domain returning errors reported by an address book object.

**Availability**:
- iOS 2.0+ - Deprecated in 9.0
- iPadOS 2.0+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+

> **Deprecated**: use CNErrorDomain

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
let ABAddressBookErrorDomain: CFString!
```

*macOS*

```swift
let ABAddressBookErrorDomain: String
```

*iOS, iPadOS, Mac Catalyst*

```c
extern CFStringRef const ABAddressBookErrorDomain;
```

*macOS*

```c
extern NSString * ABAddressBookErrorDomain;
```

## See Also

### Errors
- [Error Codes](./error-codes.md)
  Errors codes used by the Address Book framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbookerrordomain)*