# SecAccessGetTypeID()

**Framework**: Security  
**Kind**: func

Returns the unique identifier of the opaque type to which an access instance belongs.

**Availability**:
- macOS 10.2+

## Declaration

```swift
func SecAccessGetTypeID() -> CFTypeID
```

#### Return Value

A value that identifies the opaque type of a [`SecAccess`](secaccess.md) instance.

#### Discussion

This method returns a value that uniquely identifies the opaque type of a [`SecAccess`](secaccess.md) instance. You can compare this value to the [`CFTypeID`](https://developer.apple.com/documentation/CoreFoundation/CFTypeID) identifier obtained by calling the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFGetTypeID(_:)) method on a specific object. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secaccessgettypeid())*