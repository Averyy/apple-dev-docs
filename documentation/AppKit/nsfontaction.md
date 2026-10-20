# NSFontAction

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Actions that modify a font.

**Availability**:
- macOS

## Declaration

```swift
enum NSFontAction
```

```c
enum NSFontAction : NSUInteger;
```

## Topics

### Constants
- [NSFontAction.noFontChangeAction](./nsfontaction/nofontchangeaction.md)
  No action; the font is returned unchanged.
- [NSFontAction.viaPanelFontAction](./nsfontaction/viapanelfontaction.md)
  Converts the font according to the `NSFontPanel` method `panelConvertFont:`.
- [NSFontAction.addTraitFontAction](./nsfontaction/addtraitfontaction.md)
  Converts the font to have an additional trait using [`convert(_:toHaveTrait:)`](./nsfontmanager/convert%28_,tohavetrait%29.md).
- [NSFontAction.sizeUpFontAction](./nsfontaction/sizeupfontaction.md)
  Converts the font to a larger size using [`convert(_:toSize:)`](./nsfontmanager/convert%28_,tosize%29.md).
- [NSFontAction.sizeDownFontAction](./nsfontaction/sizedownfontaction.md)
  Converts the font to a smaller size using [`convert(_:toSize:)`](./nsfontmanager/convert%28_,tosize%29.md).
- [NSFontAction.heavierFontAction](./nsfontaction/heavierfontaction.md)
  Converts the font to a heavier weight using [`convertWeight(_:of:)`](./nsfontmanager/convertweight%28_,of%29.md).
- [NSFontAction.lighterFontAction](./nsfontaction/lighterfontaction.md)
  Converts the font to a lighter weight using [`convertWeight(_:of:)`](./nsfontmanager/convertweight%28_,of%29.md).
- [NSFontAction.removeTraitFontAction](./nsfontaction/removetraitfontaction.md)
  Converts the font to remove a trait using [`convert(_:toNotHaveTrait:)`](./nsfontmanager/convert%28_,tonothavetrait%29.md).
### Initializers
- [init?(rawValue: UInt)](./nsfontaction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sending Action Methods
- [func addFontTrait(Any?)](./nsfontmanager/addfonttrait%28_%29.md)
  Adds a trait to the font.
- [func removeFontTrait(Any?)](./nsfontmanager/removefonttrait%28_%29.md)
  Removes a trait from the font.
- [func modifyFont(Any?)](./nsfontmanager/modifyfont%28_%29.md)
  Modifies a trait of the font.
- [func modifyFontViaPanel(Any?)](./nsfontmanager/modifyfontviapanel%28_%29.md)
  Modifies a font trait using input from the Font panel.
- [func orderFrontStylesPanel(Any?)](./nsfontmanager/orderfrontstylespanel%28_%29.md)
  Opens the Font Styles panel.
- [func orderFrontFontPanel(Any?)](./nsfontmanager/orderfrontfontpanel%28_%29.md)
  Opens the Font panel, creating it if necessary, and displays that panel in front of the app’s windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontaction)*