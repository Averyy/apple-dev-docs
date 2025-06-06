# NSFontAction

**Framework**: AppKit  
**Kind**: enum

Actions that modify a font.

**Availability**:
- macOS ?+

## Declaration

```swift
enum NSFontAction
```

## Topics

### Constants
- [NSFontAction.noFontChangeAction](nsfontaction/nofontchangeaction.md)
  No action; the font is returned unchanged.
- [NSFontAction.viaPanelFontAction](nsfontaction/viapanelfontaction.md)
  Converts the font according to the `NSFontPanel` method `panelConvertFont:`.
- [NSFontAction.addTraitFontAction](nsfontaction/addtraitfontaction.md)
  Converts the font to have an additional trait using [`convert(_:toHaveTrait:)`](nsfontmanager/convert(_:tohavetrait:).md).
- [NSFontAction.sizeUpFontAction](nsfontaction/sizeupfontaction.md)
  Converts the font to a larger size using [`convert(_:toSize:)`](nsfontmanager/convert(_:tosize:).md).
- [NSFontAction.sizeDownFontAction](nsfontaction/sizedownfontaction.md)
  Converts the font to a smaller size using [`convert(_:toSize:)`](nsfontmanager/convert(_:tosize:).md).
- [NSFontAction.heavierFontAction](nsfontaction/heavierfontaction.md)
  Converts the font to a heavier weight using [`convertWeight(_:of:)`](nsfontmanager/convertweight(_:of:).md).
- [NSFontAction.lighterFontAction](nsfontaction/lighterfontaction.md)
  Converts the font to a lighter weight using [`convertWeight(_:of:)`](nsfontmanager/convertweight(_:of:).md).
- [NSFontAction.removeTraitFontAction](nsfontaction/removetraitfontaction.md)
  Converts the font to remove a trait using [`convert(_:toNotHaveTrait:)`](nsfontmanager/convert(_:tonothavetrait:).md).
### Initializers
- [init?(rawValue: UInt)](nsfontaction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func addFontTrait(Any?)](nsfontmanager/addfonttrait(_:).md)
  Adds a trait to the font.
- [func removeFontTrait(Any?)](nsfontmanager/removefonttrait(_:).md)
  Removes a trait from the font.
- [func modifyFont(Any?)](nsfontmanager/modifyfont(_:).md)
  Modifies a trait of the font.
- [func modifyFontViaPanel(Any?)](nsfontmanager/modifyfontviapanel(_:).md)
  Modifies a font trait using input from the Font panel.
- [func orderFrontStylesPanel(Any?)](nsfontmanager/orderfrontstylespanel(_:).md)
  Opens the Font Styles panel.
- [func orderFrontFontPanel(Any?)](nsfontmanager/orderfrontfontpanel(_:).md)
  Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontaction)*