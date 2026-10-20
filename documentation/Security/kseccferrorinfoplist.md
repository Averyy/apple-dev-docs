# kSecCFErrorInfoPlist

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Core Foundation object identifying the invalid component or key in the dictionary.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCFErrorInfoPlist: CFString
```

```c
extern CFStringRef const kSecCFErrorInfoPlist;
```

#### Discussion

This key is present when the `Info.plist` dictionary or other component has been found to be invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccferrorinfoplist)*