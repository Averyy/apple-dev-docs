# SecRequirementGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a code requirement object belongs.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecRequirementGetTypeID() -> CFTypeID
```

```c
CFTypeID SecRequirementGetTypeID();
```

#### Return Value

A value that identifies the opaque type of a [`SecRequirement`](./secrequirement.md) object.

#### Discussion

You can compare the value returned by this function to the [`CFTypeID`](../CoreFoundation/cftypeid.md) identifier obtained by calling the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function on a specific object. These values might change from release to release or platform to platform.

## See Also

### Related Documentation
- [func SecRequirementCreateWithString(CFString, SecCSFlags, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](./secrequirementcreatewithstring%28_,_,_%29.md)
  Creates a code requirement object by compiling a valid text representation of a code requirement.
- [func SecRequirementCreateWithStringAndErrors(CFString, SecCSFlags, UnsafeMutablePointer<Unmanaged<CFError>?>?, UnsafeMutablePointer<SecRequirement?>) -> OSStatus](./secrequirementcreatewithstringanderrors%28_,_,_,_%29.md)
  Creates a code requirement object by compiling a valid text representation of a code requirement and returns detailed error information in the case of failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrequirementgettypeid())*