# SCNConsistencyElementIDErrorKey

**Framework**: SceneKit  
**Kind**: var  
**Role**: Global Variable

The identifier of the scene file element where the error occurred.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
let SCNConsistencyElementIDErrorKey: String
```

```c
extern NSString * const SCNConsistencyElementIDErrorKey;
```

#### Discussion

The value for this key is a [`NSString`](../Foundation/nsstring.md) object containing an identifier.

If the element in which the error occurred does not have an identifier, the value for this key is the identifier of the closest parent element with an identifier.

## See Also

### Constants
- [let SCNConsistencyElementTypeErrorKey: String](./scnconsistencyelementtypeerrorkey.md)
  The type of scene file element in which the error occurred.
- [let SCNConsistencyLineNumberErrorKey: String](./scnconsistencylinenumbererrorkey.md)
  The line number in the scene file in which the error occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnconsistencyelementiderrorkey)*