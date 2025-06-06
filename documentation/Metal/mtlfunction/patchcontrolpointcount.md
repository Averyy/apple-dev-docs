# patchControlPointCount

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The number of patch control points in the post-tessellation vertex function.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var patchControlPointCount: Int { get }
```

#### Discussion

This value is `-1` if the number of patch control points wasn’t specified or if the function isn’t a post-tessellation vertex function.

## See Also

- [var patchType: MTLPatchType](mtlfunction/patchtype.md)
  The tessellation patch type of a post-tessellation vertex function.
- [enum MTLPatchType](mtlpatchtype.md)
  Types of tessellation patches that can be inputs of a post-tessellation vertex function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlfunction/patchcontrolpointcount)*