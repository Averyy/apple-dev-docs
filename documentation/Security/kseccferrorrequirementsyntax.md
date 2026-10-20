# kSecCFErrorRequirementSyntax

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a string containing a compilation error generated when parsing a requirement.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
let kSecCFErrorRequirementSyntax: CFString
```

```c
extern CFStringRef const kSecCFErrorRequirementSyntax;
```

#### Discussion

This key is present when a call to the [`SecRequirementCreateWithStringAndErrors(_:_:_:_:)`](./secrequirementcreatewithstringanderrors%28_,_,_,_%29.md) function results in a compilation error during the processing of the code requirement string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/kseccferrorrequirementsyntax)*