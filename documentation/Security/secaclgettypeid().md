# SecACLGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which an ACL entry belongs.

**Availability**:
- macOS 10.3+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecACLGetTypeID() -> CFTypeID
```

```c
CFTypeID SecACLGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [`SecACL`](./secacl.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [`SecACL`](./secacl.md) instance. You can compare this value to the [`CFTypeID`](../CoreFoundation/cftypeid.md) identifier obtained by calling the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) method on a specific instance. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaclgettypeid())*