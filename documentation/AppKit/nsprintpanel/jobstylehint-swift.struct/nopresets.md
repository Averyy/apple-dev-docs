# noPresets

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Output excludes all graphics printing.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let noPresets: NSPrintPanel.JobStyleHint
```

```c
extern NSPrintPanelJobStyleHint const NSPrintNoPresetsJobStyleHint;
```

#### Discussion

Equivalent to Core Printing’s `kPMPresetGraphicsTypeNone`.

## See Also

### Constants
- [static let photo: NSPrintPanel.JobStyleHint](./photo.md)
  Output contains photographic data.
- [static let allPresets: NSPrintPanel.JobStyleHint](./allpresets.md)
  Output appropriate to all graphics types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/jobstylehint-swift.struct/nopresets)*