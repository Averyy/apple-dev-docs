# SecRequirementGetTypeID()

**Framework**: Security  
**Kind**: func

Returns the unique identifier of the opaque type to which a code requirement object belongs.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecRequirementGetTypeID() -> CFTypeID
```

#### Return Value

A value that identifies the opaque type of a [`SecRequirement`](secrequirement.md) object.

#### Discussion

You can compare the value returned by this function to the [`CFTypeID`](https://developer.apple.com/documentation/CoreFoundation/CFTypeID) identifier obtained by calling the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFGetTypeID(_:)) function on a specific object. These values might change from release to release or platform to platform.

## See Also

- [func SecRequirementCreateWithString(CFString, SecCSFlags, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](secrequirementcreatewithstring(_:_:_:).md)
  Creates a code requirement object by compiling a valid text representation of a code requirement.
- [func SecRequirementCreateWithStringAndErrors(CFString, SecCSFlags, UnsafeMutablePointer<Unmanaged<CFError>?>?, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](secrequirementcreatewithstringanderrors(_:_:_:_:).md)
  Creates a code requirement object by compiling a valid text representation of a code requirement and returns detailed error information in the case of failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequirementgettypeid())*