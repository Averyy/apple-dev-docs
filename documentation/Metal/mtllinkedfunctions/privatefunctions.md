# privateFunctions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<id<MTLFunction>> * privateFunctions;
```

#### Discussion

The pipeline doesn’t export these functions as [`MTLFunctionHandle`](../mtlfunctionhandle.md) instances because the Metal device doesn’t need to support function pointers to link private functions.

## See Also

### Specifying related functions
- [var functions: [any MTLFunction]?](./functions.md)
  An array of function objects to link to the new function.
- [var binaryFunctions: [any MTLFunction]?](./binaryfunctions.md)
  An array of function objects already compiled to a binary representation to link.
- [var groups: [String : [any MTLFunction]]?](./groups.md)
  An optional list of groups specifying which functions your shader can call at each call site.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllinkedfunctions/privatefunctions)*