# printInfo

**Framework**: AppKit  
**Kind**: property

The information associated with the running Print panel.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var printInfo: NSPrintInfo { get }
```

#### Discussion

The value in this property is `nil` if the Print panel is not currently running.

## See Also

- [class NSPrintInfo](nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [NSPrintPanel.Result](nsprintpanel/result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/printinfo)*