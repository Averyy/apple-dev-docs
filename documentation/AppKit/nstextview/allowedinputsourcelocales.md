# allowedInputSourceLocales

**Framework**: AppKit  
**Kind**: property

An array of locale identifiers representing input sources that are allowed to be enabled when the receiver has the keyboard focus.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var allowedInputSourceLocales: [String]? { get set }
```

#### Discussion

You can use the meta-locale identifier, [`NSAllRomanInputSourcesLocaleIdentifier`](nsallromaninputsourceslocaleidentifier.md), to specify input sources that are limited for Roman script editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/allowedinputsourcelocales)*