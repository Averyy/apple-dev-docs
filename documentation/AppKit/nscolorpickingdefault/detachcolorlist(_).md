# detachColorList(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the receiver to detach the given color list, unless the receiver isn’t displaying the list.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func detachColorList(_ colorList: NSColorList)
```

```objc
- (void) detachColorList:(NSColorList *) colorList;
```

#### Discussion

You never invoke this method; it’s invoked automatically by the `NSColorPanel` object when its [`detachColorList(_:)`](../nscolorpanel/detachcolorlist%28_%29.md) method is invoked. Because the `NSColorPanel` list mode manages `NSColorList` objects, this method need only be implemented by a custom color picker that manages `NSColorList` objects itself.

## Parameters

- `colorList`: The color list to detach.

## See Also

### Managing Color Lists
- [func attachColorList(NSColorList)](./attachcolorlist%28_%29.md)
  Tells the receiver to attach the given color list, if it isn’t already displaying the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingdefault/detachcolorlist(_:))*