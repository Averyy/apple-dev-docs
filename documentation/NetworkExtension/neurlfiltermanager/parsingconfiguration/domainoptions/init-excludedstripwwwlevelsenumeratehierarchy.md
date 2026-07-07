# init(excluded:stripWWW:levels:enumerateHierarchy:)

**Framework**: Network Extension  
**Kind**: init

Creates a new domain options configuration with default values.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
init(excluded: Bool = false, stripWWW: Bool = true, levels: UInt = 0, enumerateHierarchy: Bool = true)
```

#### Discussion

The domain options default behavior is as follows:

- Parsing includes the domain.
- Parsing strips the `www` subdomain if it is present.
- Parsing includes all domain levels.
- Parsing enables enumeration of the domain hierarchy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltermanager/parsingconfiguration/domainoptions/init(excluded:stripwww:levels:enumeratehierarchy:))*