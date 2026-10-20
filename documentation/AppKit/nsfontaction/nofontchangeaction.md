# NSFontAction.noFontChangeAction

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

No action; the font is returned unchanged.

**Availability**:
- macOS

## Declaration

```swift
case noFontChangeAction
```

```c
NSNoFontChangeAction
```

## See Also

### Constants
- [NSFontAction.viaPanelFontAction](./viapanelfontaction.md)
  Converts the font according to the `NSFontPanel` method `panelConvertFont:`.
- [NSFontAction.addTraitFontAction](./addtraitfontaction.md)
  Converts the font to have an additional trait using [`convert(_:toHaveTrait:)`](../nsfontmanager/convert%28_,tohavetrait%29.md).
- [NSFontAction.sizeUpFontAction](./sizeupfontaction.md)
  Converts the font to a larger size using [`convert(_:toSize:)`](../nsfontmanager/convert%28_,tosize%29.md).
- [NSFontAction.sizeDownFontAction](./sizedownfontaction.md)
  Converts the font to a smaller size using [`convert(_:toSize:)`](../nsfontmanager/convert%28_,tosize%29.md).
- [NSFontAction.heavierFontAction](./heavierfontaction.md)
  Converts the font to a heavier weight using [`convertWeight(_:of:)`](../nsfontmanager/convertweight%28_,of%29.md).
- [NSFontAction.lighterFontAction](./lighterfontaction.md)
  Converts the font to a lighter weight using [`convertWeight(_:of:)`](../nsfontmanager/convertweight%28_,of%29.md).
- [NSFontAction.removeTraitFontAction](./removetraitfontaction.md)
  Converts the font to remove a trait using [`convert(_:toNotHaveTrait:)`](../nsfontmanager/convert%28_,tonothavetrait%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontaction/nofontchangeaction)*