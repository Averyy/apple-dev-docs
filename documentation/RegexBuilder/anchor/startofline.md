# startOfLine

**Framework**: RegexBuilder  
**Kind**: property

An anchor that matches at the start of a line, including the start of the input string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static var startOfLine: Anchor { get }
```

#### Discussion

This anchor is equivalent to `^` in regex syntax when the `m` option has been enabled or `anchorsMatchLineEndings(true)` has been called.

For example, the following regexes are all equivalent:

- `Regex { Anchor.startOfLine }`
- `/(?m)^/` or `/(?m:^)/`
- `/^/.anchorsMatchLineEndings(true)`


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/anchor/startofline)*