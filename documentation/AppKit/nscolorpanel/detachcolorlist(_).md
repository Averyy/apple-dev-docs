# detachColorList(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the list of colors from all the color pickers in the receiver that display color lists by invoking [`detachColorList(_:)`](./detachcolorlist%28_%29.md) on all color pickers in the application.

**Availability**:
- macOS

## Declaration

```swift
func detachColorList(_ colorList: NSColorList)
```

```objc
- (void) detachColorList:(NSColorList *) colorList;
```

#### Discussion

Your application should use this method to remove an `NSColorList` saved with a document in its file package or in a directory other than `NSColorList`’s standard search directories.

## Parameters

- `colorList`: The list of `NSColor` objects to remove from the color pickers in the color panel.

## See Also

### Managing color lists
- [func attachColorList(NSColorList)](./attachcolorlist%28_%29.md)
  Adds the list of `NSColor` objects specified to all the color pickers in the receiver that display color lists by invoking [`attachColorList(_:)`](./attachcolorlist%28_%29.md) on all color pickers in the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/detachcolorlist(_:))*