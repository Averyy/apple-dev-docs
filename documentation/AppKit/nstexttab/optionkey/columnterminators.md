# columnTerminators

**Framework**: AppKit  
**Kind**: property

The value is an `NSCharacterSet` object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let columnTerminators: NSTextTab.OptionKey
```

#### Discussion

The character set is used to determine the terminating character for a tab column. The tab and newline characters are implied even if they don’t exist in the character set. This attribute is optional.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexttab/optionkey/columnterminators)*