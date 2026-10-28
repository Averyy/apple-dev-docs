# excluded

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to exlude the path component from URL parsing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
var excluded: Bool
```

## Discussion

When this value is `true`, parsing ignores all other path options.

## See Also

### Working with path options
- [var segments: UInt](./segments.md)
  The number of path levels to preserve when parsing.
- [var enumerateHierarchy: Bool](./enumeratehierarchy.md)
  A Boolean value that indicates whether the parser walks the path hierarchy for matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/pathoptions/excluded)*