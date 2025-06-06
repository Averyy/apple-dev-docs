# headerToolTip

**Framework**: AppKit  
**Kind**: property

The string that’s displayed in a help tag over the table column header.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
var headerToolTip: String? { get set }
```

#### Discussion

When the value of this property is `nil`, the table column header doesn’t display a help tag (also known as a tooltip). Otherwise, the string is displayed in a help tag when the pointer pauses over the header of the table column. The default value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/headertooltip)*