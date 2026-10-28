# headerLevel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The paragraph’s header level for HTML generation.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var headerLevel: Int { get }
```

```objc
@property (readonly) NSInteger headerLevel;
```

## Discussion

If the paragraph isn’t a header, the value is `0`. If the paragraph is a header, the value ranges from `1` to `6`, depending on the header’s level.

The default value is `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/headerlevel)*