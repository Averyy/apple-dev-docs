# SecACLGetTypeID()

**Framework**: Security  
**Kind**: func

Returns the unique identifier of the opaque type to which an ACL entry belongs.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SecACLGetTypeID() -> CFTypeID
```

#### Return Value

A value that identifies the opaque type of a [`SecACL`](secacl.md) object.

#### Discussion

This function returns a value that uniquely identifies the opaque type of a [`SecACL`](secacl.md) instance. You can compare this value to the [`CFTypeID`](https://developer.apple.com/documentation/CoreFoundation/CFTypeID) identifier obtained by calling the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFGetTypeID(_:)) method on a specific instance. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclgettypeid())*