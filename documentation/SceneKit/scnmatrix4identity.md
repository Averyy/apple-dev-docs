# SCNMatrix4Identity

**Framework**: SceneKit  
**Kind**: var  
**Role**: Global Variable

The 4 x 4 identity matrix.

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
let SCNMatrix4Identity: SCNMatrix4
```

```c
extern const SCNMatrix4 SCNMatrix4Identity;
```

#### Discussion

Elements on the diagonal of this matrix are `1.0`; all other elements are `0.0`. Multiplying another matrix by the identity matrix or multiplying the identity matrix by another matrix yields the other matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmatrix4identity)*