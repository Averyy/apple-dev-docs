# SecTaskCopyValuesForEntitlements(_:_:_:)

**Framework**: Security  
**Kind**: func

Returns the values of multiple entitlements for the represented task.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func SecTaskCopyValuesForEntitlements(_ task: SecTask, _ entitlements: CFArray, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary?
```

#### Return Value

A dictionary containing the entitlement names as keys with the corresponding entitlements as the dictionary values, or `NULL` on error. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free this dictionary’s memory when you are done with it.

## Parameters

- `task`: The task whose entitlements you want.
- `entitlements`: An array of the names of the entitlement to be fetched.
- `error`: A pointer that the function uses to provide an error object with details if an error occurs. The caller becomes responsible for the object’s memory. Pass   to ignore the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectaskcopyvaluesforentitlements(_:_:_:))*