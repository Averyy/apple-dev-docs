# sizeInMillimeters

**Framework**: Paravirtualized Graphics  
**Kind**: property

The size in millimeters of the virtual display.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var sizeInMillimeters: NSSize { get set }
```

#### Discussion

The device propagates the display size to the guest operating system. The app can scale the resulting screen data to a different size in its user interface.

## See Also

- [var name: String?](pgdisplaydescriptor/name.md)
  The display’s name as seen in the guest operating environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplaydescriptor/sizeinmillimeters)*