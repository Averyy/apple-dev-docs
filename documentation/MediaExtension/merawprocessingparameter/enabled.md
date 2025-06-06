# enabled

**Framework**: MediaExtension  
**Kind**: property

A Boolean value that indicates whether the extension enables the parameter.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var enabled: Bool { get set }
```

#### Discussion

This parameter can only be modified by the extension. From the application-facing interface, `VTRAWProcessingSession`, this is a read-only value which indicates whether the parameter should be grayed out and disabled in any UI being generated.

## See Also

- [var key: String](merawprocessingparameter/key.md)
  A unique key string identifying the parameter.
- [var longDescription: String](merawprocessingparameter/longdescription.md)
  A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.
- [var name: String](merawprocessingparameter/name.md)
  A localized human-readable name for the parameter, suitable for displaying in application UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/enabled)*