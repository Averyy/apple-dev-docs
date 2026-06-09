# segments

**Framework**: Network Extension  
**Kind**: property

The number of path levels to preserve when parsing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
var segments: UInt
```

#### Discussion

With a path of `/a/b/c/d`, setting `segments` to `2` keeps `/a/b`.

Use a value of `0` to keep all path segments.

## See Also

- [var excluded: Bool](neurlfiltermanager/parsingconfiguration/pathoptions/excluded.md)
  A Boolean value that indicates whether to exlude the path component from URL parsing.
- [var enumerateHierarchy: Bool](neurlfiltermanager/parsingconfiguration/pathoptions/enumeratehierarchy.md)
  A Boolean value that indicates whether the parser walks the path hierarchy for matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/pathoptions/segments)*