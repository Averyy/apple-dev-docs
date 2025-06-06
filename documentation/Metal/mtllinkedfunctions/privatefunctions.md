# privateFunctions

**Framework**: Metal  
**Kind**: property

An array of function objects to link to the new function, without exporting the functions publicly.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var privateFunctions: [any MTLFunction]? { get set }
```

#### Discussion

These functions are not exported by the pipeline state as [`MTLFunctionHandle`](mtlfunctionhandle.md) objects. The Metal device object doesn’t need to support function pointers to link private functions.

## See Also

- [var functions: [any MTLFunction]?](mtllinkedfunctions/functions.md)
  An array of function objects to link to the new function.
- [var binaryFunctions: [any MTLFunction]?](mtllinkedfunctions/binaryfunctions.md)
  An array of function objects already compiled to a binary representation to link.
- [var groups: [String : [any MTLFunction]]?](mtllinkedfunctions/groups.md)
  An optional list of groups specifying which functions your shader can call at each call site.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllinkedfunctions/privatefunctions)*