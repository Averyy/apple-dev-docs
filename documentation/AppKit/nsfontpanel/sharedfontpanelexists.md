# sharedFontPanelExists

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the shared Font panel has been created.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var sharedFontPanelExists: Bool { get }
```

#### Discussion

The value is [`true`](https://developer.apple.com/documentation/Swift/true) if the shared Font panel has been created, and [`false`](https://developer.apple.com/documentation/Swift/false) if it hasn’t.

## See Also

- [class var shared: NSFontPanel](nsfontpanel/shared.md)
  Returns the single `NSFontPanel` instance for the application, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel/sharedfontpanelexists)*