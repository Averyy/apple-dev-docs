# SecGuestRef

**Framework**: Security  
**Kind**: typealias

A reference to a guest object, which identifies a particular block of guest code in the context of its code signing host.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias SecGuestRef = UInt32
```

#### Discussion

Guest handles are assigned by the host at will, with [`kSecNoGuest`](ksecnoguest.md) being reserved as the `NULL` value. They can be reused for new children if desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secguestref)*