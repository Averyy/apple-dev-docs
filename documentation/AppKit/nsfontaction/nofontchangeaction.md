# NSFontAction.noFontChangeAction

**Framework**: AppKit  
**Kind**: case

No action; the font is returned unchanged.

**Availability**:
- macOS ?+

## Declaration

```swift
case noFontChangeAction
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontaction/nofontchangeaction)*