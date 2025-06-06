# attachColorList(_:)

**Framework**: AppKit  
**Kind**: method

Adds the list of `NSColor` objects specified to all the color pickers in the receiver that display color lists by invoking [`attachColorList(_:)`](nscolorpanel/attachcolorlist(_:).md) on all color pickers in the application.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func attachColorList(_ colorList: NSColorList)
```

#### Discussion

An application should use this method to add an `NSColorList` saved with a document in its file package or in a directory other than `NSColorList`’s standard search directories.

## Parameters

- `colorList`: The list of colors to add to the color pickers in the receiver.

## See Also

- [func detachColorList(NSColorList)](nscolorpanel/detachcolorlist(_:).md)
  Removes the list of colors from all the color pickers in the receiver that display color lists by invoking [`detachColorList(_:)`](nscolorpanel/detachcolorlist(_:).md) on all color pickers in the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/attachcolorlist(_:))*