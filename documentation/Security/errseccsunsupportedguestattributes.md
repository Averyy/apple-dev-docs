# errSecCSUnsupportedGuestAttributes

**Framework**: Security  
**Kind**: var

Cannot locate guest code using this attribute set.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var errSecCSUnsupportedGuestAttributes: OSStatus { get }
```

#### Discussion

When calling the [`SecHostCreateGuest`](sechostcreateguest.md) function or the [`SecCodeCopyGuestWithAttributes(_:_:_:_:)`](seccodecopyguestwithattributes(_:_:_:_:).md) function, you passed a key that either isn’t understood, recognized, or supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errseccsunsupportedguestattributes)*