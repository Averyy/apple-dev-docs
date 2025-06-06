# isRelative

**Framework**: System  
**Kind**: property

Returns true if this path is not absolute (see `isAbsolute`).

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var isRelative: Bool { get }
```

#### Discussion

Examples:

- Unix: - `~/bar`
- `tmp/foo.txt`
- Windows: - `bar\baz`
- `C:Users\`
- `\Users`


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/isrelative)*