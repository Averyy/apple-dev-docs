# name

**Framework**: Paravirtualized Graphics  
**Kind**: property

The display’s name as seen in the guest operating environment.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var name: String? { get set }
```

#### Discussion

The default value is `Apple Virtual`. The framework truncates the name to 13 characters.

The device propagates the display name into the guest environment, so the name may be visible in the guest operating system’s user interface.

## See Also

- [var sizeInMillimeters: NSSize](pgdisplaydescriptor/sizeinmillimeters.md)
  The size in millimeters of the virtual display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor/name)*