# levels

**Framework**: Network Extension  
**Kind**: property

The number of domain levels to preserve when parsing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
var levels: UInt
```

#### Discussion

A value of `2` for the domain `www.sub.example.com` keeps the `example.com`.

Use a value of `0` to keep all domain levels.

## See Also

- [var excluded: Bool](neurlfiltermanager/parsingconfiguration/domainoptions/excluded.md)
  A Boolean value that indicates whether to exclude the domain component from URL parsing.
- [var stripWWW: Bool](neurlfiltermanager/parsingconfiguration/domainoptions/stripwww.md)
  A Boolean value that indicates whether to strip the `www` subdomain when parsing.
- [var enumerateHierarchy: Bool](neurlfiltermanager/parsingconfiguration/domainoptions/enumeratehierarchy.md)
  A Boolean value that indicates whether the parser walks the domain hierarchy for matching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/domainoptions/levels)*