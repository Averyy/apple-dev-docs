# errSecCSUnsupportedGuestAttributes

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

Cannot locate guest code using this attribute set.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var errSecCSUnsupportedGuestAttributes: OSStatus { get }
```

```c
errSecCSUnsupportedGuestAttributes
```

#### Discussion

When calling the [`SecHostCreateGuest`](./sechostcreateguest.md) function or the [`SecCodeCopyGuestWithAttributes(_:_:_:_:)`](./seccodecopyguestwithattributes%28_,_,_,_%29.md) function, you passed a key that either isn’t understood, recognized, or supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errseccsunsupportedguestattributes)*