# kAuthorizationContextFlagSticky

**Framework**: Security  
**Kind**: case  
**Role**: Enumeration Case

This data persists through an interrupted or failed evaluation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
kAuthorizationContextFlagSticky
```

## Discussion

This flag can be used to propagate an error condition from a downstream plug-in to an upstream one. It is not remembered in the authorization reference (see [Authorization Services](../authorization-services.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationcontextflags/kauthorizationcontextflagsticky)*