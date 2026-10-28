# SecTrustedApplicationGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a trusted app instance belongs.

**Availability**:
- macOS 10.2+ - Deprecated in 10.10

> **Deprecated**: SecKeychain is deprecated

## Declaration

```swift
func SecTrustedApplicationGetTypeID() -> CFTypeID
```

```c
CFTypeID SecTrustedApplicationGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [`SecTrustedApplication`](./sectrustedapplication.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [`SecTrustedApplication`](./sectrustedapplication.md) instance. You can compare this value to the [`CFTypeID`](../CoreFoundation/cftypeid.md) identifier obtained by calling the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) method on a specific instance. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustedapplicationgettypeid())*