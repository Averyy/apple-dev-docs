# detachColorList(_:)

**Framework**: AppKit  
**Kind**: method

Removes the list of colors from all the color pickers in the receiver that display color lists by invoking [`detachColorList(_:)`](nscolorpanel/detachcolorlist(_:).md) on all color pickers in the application.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func detachColorList(_ colorList: NSColorList)
```

#### Discussion

Your application should use this method to remove an `NSColorList` saved with a document in its file package or in a directory other than `NSColorList`’s standard search directories.

## Parameters

- `colorList`: The list of   objects to remove from the color pickers in the color panel.

## See Also

- [func attachColorList(NSColorList)](nscolorpanel/attachcolorlist(_:).md)
  Adds the list of `NSColor` objects specified to all the color pickers in the receiver that display color lists by invoking [`attachColorList(_:)`](nscolorpanel/attachcolorlist(_:).md) on all color pickers in the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/detachcolorlist(_:))*