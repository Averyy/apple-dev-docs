# groups

**Framework**: Metal  
**Kind**: property

Assigns groups of functions to match call-site attributes in shader code.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
var groups: [String : [MTL4FunctionDescriptor]]? { get set }
```

#### Discussion

Function groups help the compiler reduce the number of candidate functions it needs to evaluate for shader function calls, potentially increasing runtime performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4linkedfunctions/groups)*