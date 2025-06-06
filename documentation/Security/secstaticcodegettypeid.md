# SecStaticCodeGetTypeID()

**Framework**: Security  
**Kind**: func

Returns the unique identifier of the opaque type to which a static code object belongs.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecStaticCodeGetTypeID() -> CFTypeID
```

#### Return Value

A value that identifies the opaque type of a [`SecStaticCode`](secstaticcode.md) object.

#### Discussion

You can compare the value returned by this function to the [`CFTypeID`](https://developer.apple.com/documentation/CoreFoundation/CFTypeID) identifier obtained by calling the [`CFGetTypeID(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFGetTypeID(_:)) function on a specific object. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secstaticcodegettypeid())*