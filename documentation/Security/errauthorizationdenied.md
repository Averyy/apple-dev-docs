# errAuthorizationDenied

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

The Security Server denied authorization for one or more requested rights.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var errAuthorizationDenied: OSStatus { get }
```

```c
errAuthorizationDenied
```

## Discussion

This error is also returned if there was no definition found in the policy database, or a definition could not be created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errauthorizationdenied)*