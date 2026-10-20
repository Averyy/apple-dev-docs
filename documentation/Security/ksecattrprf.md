# kSecAttrPRF

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the item’s pseudorandom function.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecAttrPRF: CFString
```

```c
extern CFStringRef const kSecAttrPRF;
```

#### Discussion

The corresponding value is of type [`CFString`](../CoreFoundation/cfstring.md) and indicates the pseudorandom function associated with this cryptographic key. See [Pseudorandom Function Values](./item-attribute-keys-and-values.md#Pseudorandom-Function-Values) for a list of valid values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrprf)*