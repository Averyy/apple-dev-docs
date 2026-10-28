# sharedFontPanelExists

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether the shared Font panel has been created.

**Availability**:
- macOS

## Declaration

```swift
class var sharedFontPanelExists: Bool { get }
```

```objc
@property (class, readonly) BOOL sharedFontPanelExists;
```

## Discussion

The value is [`true`](../../Swift/true.md) if the shared Font panel has been created, and [`false`](../../Swift/false.md) if it hasn’t.

## See Also

### Getting the Font Panel
- [class var shared: NSFontPanel](./shared.md)
  Returns the single `NSFontPanel` instance for the application, creating it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontpanel/sharedfontpanelexists)*