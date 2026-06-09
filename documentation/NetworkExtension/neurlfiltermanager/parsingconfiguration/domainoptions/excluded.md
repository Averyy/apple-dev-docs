# excluded

**Framework**: Network Extension  
**Kind**: property

A Boolean value that indicates whether to exclude the domain component from URL parsing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)

## Declaration

```swift
var excluded: Bool
```

#### Discussion

When this value is `true`, parsing ignores all other domain options.

## See Also

- [var stripWWW: Bool](neurlfiltermanager/parsingconfiguration/domainoptions/stripwww.md)
  A Boolean value that indicates whether to strip the `www` subdomain when parsing.
- [var levels: UInt](neurlfiltermanager/parsingconfiguration/domainoptions/levels.md)
  The number of domain levels to preserve when parsing.
- [var enumerateHierarchy: Bool](neurlfiltermanager/parsingconfiguration/domainoptions/enumeratehierarchy.md)
  A Boolean value that indicates whether the parser walks the domain hierarchy for matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/domainoptions/excluded)*