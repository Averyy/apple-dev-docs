# SecStaticCodeGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a static code object belongs.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecStaticCodeGetTypeID() -> CFTypeID
```

```c
CFTypeID SecStaticCodeGetTypeID();
```

#### Return Value

A value that identifies the opaque type of a [`SecStaticCode`](./secstaticcode.md) object.

#### Discussion

You can compare the value returned by this function to the [`CFTypeID`](../CoreFoundation/cftypeid.md) identifier obtained by calling the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function on a specific object. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secstaticcodegettypeid())*