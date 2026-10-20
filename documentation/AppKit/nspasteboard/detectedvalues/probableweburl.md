# probableWebURL

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A string that the data detection system identifies as a probable web URL, suitable for implementing “Paste and Go”.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var probableWebURL: String { get }
```

## See Also

### Email and web values
- [var emailAddresses: [DDMatchEmailAddress]](./emailaddresses.md)
  An array of email addresses that the data detection system identifies.
- [var links: [DDMatchLink]](./links.md)
  An array of web links that the data detection system identifies.
- [var probableWebSearch: String](./probablewebsearch.md)
  A string that the data detection system identifies as a probable web search item, suitable for implementing “Paste and Search”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/detectedvalues/probableweburl)*