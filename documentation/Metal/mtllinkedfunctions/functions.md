# functions

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

An array of function objects to link to the new function.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var functions: [any MTLFunction]? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<id<MTLFunction>> * functions;
```

## See Also

### Specifying related functions
- [var binaryFunctions: [any MTLFunction]?](./binaryfunctions.md)
  An array of function objects already compiled to a binary representation to link.
- [var groups: [String : [any MTLFunction]]?](./groups.md)
  An optional list of groups specifying which functions your shader can call at each call site.
- [var privateFunctions: [any MTLFunction]?](./privatefunctions.md)
  An array of function objects to link to the new function, without exporting the functions publicly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllinkedfunctions/functions)*