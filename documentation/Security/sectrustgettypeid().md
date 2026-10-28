# SecTrustGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a trust object belongs.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecTrustGetTypeID() -> CFTypeID
```

```c
CFTypeID SecTrustGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [`SecTrust`](./sectrust.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [`SecTrust`](./sectrust.md) object. You can compare this value to the [`CFTypeID`](../CoreFoundation/cftypeid.md) identifier obtained by calling the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function on a specific object. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustgettypeid())*