# default

**Framework**: AppKit  
**Kind**: property

The default paragraph style.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@NSCopying
class var `default`: NSParagraphStyle { get }
```

#### Discussion

The default paragraph style has the following default values:

| Subattribute | Default |
| --- | --- |
| Alignment | `NSNaturalTextAlignment` |
| Tab stops | 12 left-aligned tabs, spaced by `28.0` points |
| Line break mode | `NSLineBreakByWordWrapping` |
| All others | `0.0` |

See individual method descriptions for explanations of each subattribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsparagraphstyle/default)*