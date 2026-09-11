# init(excluded:segments:enumerateHierarchy:)

**Framework**: Network Extension  
**Kind**: init

Creates a new path options configuration with default values.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
init(excluded: Bool = false, segments: UInt = 0, enumerateHierarchy: Bool = true)
```

#### Discussion

The path options default behavior is as follows:

- Parsing includes the path.
- Parsing preserves all path segments.
- Parsing enables path hierarchy enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/pathoptions/init(excluded:segments:enumeratehierarchy:))*