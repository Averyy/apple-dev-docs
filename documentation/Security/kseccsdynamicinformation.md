# kSecCSDynamicInformation

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

Dynamic validity information about running code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kSecCSDynamicInformation: UInt32 { get }
```

```c
kSecCSDynamicInformation
```

## Discussion

This information cannot be returned for code on disk (represented by a [`SecStaticCode`](./secstaticcode.md) object).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccsdynamicinformation)*