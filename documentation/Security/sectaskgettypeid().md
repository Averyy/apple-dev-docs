# SecTaskGetTypeID()

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the unique identifier of the opaque type to which a task object belongs.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTaskGetTypeID() -> CFTypeID
```

```c
CFTypeID SecTaskGetTypeID();
```

## Return Value

A value that identifies the opaque type of a [`SecTask`](./sectask.md) object.

## Discussion

This function returns a value that uniquely identifies the opaque type of a [`SecTask`](./sectask.md) object. You can compare this value to the [`CFTypeID`](../CoreFoundation/cftypeid.md) identifier obtained by calling the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function on a specific object. These values might change from release to release or platform to platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectaskgettypeid())*