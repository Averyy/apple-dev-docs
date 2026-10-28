# SecPolicySearchGetTypeID

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a `SecPolicySearch` object belongs.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CFTypeID SecPolicySearchGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [`SecPolicySearch`](./secpolicysearch.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [`SecPolicySearch`](./secpolicysearch.md) object. You can compare this value to the `CFTypeID` identifier obtained by calling the `CFGetTypeID` function on a specific object. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secpolicysearchgettypeid)*