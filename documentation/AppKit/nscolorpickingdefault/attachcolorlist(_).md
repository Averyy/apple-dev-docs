# attachColorList(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the receiver to attach the given color list, if it isn’t already displaying the list.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func attachColorList(_ colorList: NSColorList)
```

```objc
- (void) attachColorList:(NSColorList *) colorList;
```

#### Discussion

You never invoke this method; it’s invoked automatically by the `NSColorPanel` object when its [`attachColorList(_:)`](../nscolorpanel/attachcolorlist%28_%29.md) method is invoked. Because the `NSColorPanel` list mode manages `NSColorList` objects, this method need only be implemented by a custom color picker that manages `NSColorList` objects itself.

## Parameters

- `colorList`: The color list to display.

## See Also

### Managing Color Lists
- [func detachColorList(NSColorList)](./detachcolorlist%28_%29.md)
  Tells the receiver to detach the given color list, unless the receiver isn’t displaying the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/attachcolorlist(_:))*