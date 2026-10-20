# attachColorList(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the list of `NSColor` objects specified to all the color pickers in the receiver that display color lists by invoking [`attachColorList(_:)`](./attachcolorlist%28_%29.md) on all color pickers in the application.

**Availability**:
- macOS

## Declaration

```swift
func attachColorList(_ colorList: NSColorList)
```

```objc
- (void) attachColorList:(NSColorList *) colorList;
```

#### Discussion

An application should use this method to add an `NSColorList` saved with a document in its file package or in a directory other than `NSColorList`’s standard search directories.

## Parameters

- `colorList`: The list of colors to add to the color pickers in the receiver.

## See Also

### Managing color lists
- [func detachColorList(NSColorList)](./detachcolorlist%28_%29.md)
  Removes the list of colors from all the color pickers in the receiver that display color lists by invoking [`detachColorList(_:)`](./detachcolorlist%28_%29.md) on all color pickers in the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpanel/attachcolorlist(_:))*