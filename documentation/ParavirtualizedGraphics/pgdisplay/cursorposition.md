# cursorPosition

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Required**: Yes

The current cursor location in the guest environment.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var cursorPosition: PGDisplayCoord_t { get }
```

#### Discussion

If the cursor isn’t on the display, this property’s value is `(0xFFFF, 0xFFFF)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/cursorposition)*