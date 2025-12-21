# groups

**Framework**: Metal  
**Kind**: property

An optional list of groups specifying which functions your shader can call at each call site.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var groups: [String : [any MTLFunction]]? { get set }
```

#### Discussion

The default value is `nil`.

The default behavior is conservative and assumes that your shader can call any linked function from every call site. If you know that the shader can only call a limited subset of functions at a call site, you can annotate those sites in the shader with a name of a group and then specify the list of functions for that call site using this property. Specifying call sites and callable functions more precisely can improve performance.

For more information on how to specify call site groups, see [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

The value of this property is a dictionary whose keys are call site names and values are arrays specifying the list of functions that the shader can call from each site.

## See Also

- [var functions: [any MTLFunction]?](mtllinkedfunctions/functions.md)
  An array of function objects to link to the new function.
- [var binaryFunctions: [any MTLFunction]?](mtllinkedfunctions/binaryfunctions.md)
  An array of function objects already compiled to a binary representation to link.
- [var privateFunctions: [any MTLFunction]?](mtllinkedfunctions/privatefunctions.md)
  An array of function objects to link to the new function, without exporting the functions publicly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtllinkedfunctions/groups)*