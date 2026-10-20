# kSecCFErrorResourceAdded

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a URL pointing to the resource on disk that is not included in the signed resources for the code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCFErrorResourceAdded: CFString
```

```c
extern CFStringRef const kSecCFErrorResourceAdded;
```

#### Discussion

This key is present when an unsealed resource is found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccferrorresourceadded)*