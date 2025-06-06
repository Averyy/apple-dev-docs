# binaryFunctions

**Framework**: Metal  
**Kind**: property

An array of function objects already compiled to a binary representation to link.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var binaryFunctions: [any MTLFunction]? { get set }
```

## See Also

- [var functions: [any MTLFunction]?](mtllinkedfunctions/functions.md)
  An array of function objects to link to the new function.
- [var groups: [String : [any MTLFunction]]?](mtllinkedfunctions/groups.md)
  An optional list of groups specifying which functions your shader can call at each call site.
- [var privateFunctions: [any MTLFunction]?](mtllinkedfunctions/privatefunctions.md)
  An array of function objects to link to the new function, without exporting the functions publicly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllinkedfunctions/binaryfunctions)*