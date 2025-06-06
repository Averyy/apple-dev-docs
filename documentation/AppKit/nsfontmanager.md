# NSFontManager

**Framework**: AppKit  
**Kind**: class

The center of activity for the font-conversion system.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSFontManager
```

#### Overview

The font manager records the currently selected font, updates the Font panel and Font menu to reflect the selected font, initiates font changes, and converts fonts in response to requests from text-bearing objects. In a more prosaic role, [`NSFontManager`](nsfontmanager.md) can be queried for the fonts available to the application and for the particular attributes of a font, such as whether it’s condensed or extended.

You typically set up a font manager and the Font menu using Interface Builder. However, you can also do so programmatically by getting the shared font manager instance and having it create the standard Font menu at runtime:

```objc
NSFontManager *fontManager = [NSFontManager sharedFontManager];
NSMenu *fontMenu = [fontManager fontMenu:YES];
```

You can then add the Font menu to your app’s main menu. After the Font menu is installed, your app automatically gains the functionality of both the Font menu and the Font panel.

Font collections are managed by [`NSFontManager`](nsfontmanager.md).

## Topics

### Getting the Shared Font Manager
- [class var shared: NSFontManager](nsfontmanager/shared.md)
  Returns the shared instance of the font manager for the application, creating it if necessary.
### Changing the Default Font Conversion Classes
- [class func setFontManagerFactory(AnyClass?)](nsfontmanager/setfontmanagerfactory(_:).md)
  Sets the class that creates the shared font manager object.
- [class func setFontPanelFactory(AnyClass?)](nsfontmanager/setfontpanelfactory(_:).md)
  Sets the class that creates the shared Font panel object.
### Getting Available Fonts
- [var availableFonts: [String]](nsfontmanager/availablefonts.md)
  The names of the fonts available in the system (not the [`NSFont`](nsfont.md) objects themselves).
- [var availableFontFamilies: [String]](nsfontmanager/availablefontfamilies.md)
  The names of the font families available in the system.
- [func availableFontNames(with: NSFontTraitMask) -> [String]?](nsfontmanager/availablefontnames(with:).md)
  Returns the names of the fonts available in the system whose traits are described exactly by the given font trait mask (not the `NSFont` objects themselves).
- [func availableMembers(ofFontFamily: String) -> [[Any]]?](nsfontmanager/availablemembers(offontfamily:).md)
  Returns an array with one entry for each available member of a font family.
### Setting and Examining the Selected Font
- [func setSelectedFont(NSFont, isMultiple: Bool)](nsfontmanager/setselectedfont(_:ismultiple:).md)
  Records the specified font as the currently selected font and updates the Font panel.
- [var selectedFont: NSFont?](nsfontmanager/selectedfont.md)
  The currently selected font object.
- [var isMultiple: Bool](nsfontmanager/ismultiple.md)
  A Boolean value that indicates whether the currently selected font has multiple fonts.
- [func sendAction() -> Bool](nsfontmanager/sendaction.md)
  A Boolean value that indicates whether a responder handled the font manager’s action message.
- [func localizedName(forFamily: String, face: String?) -> String](nsfontmanager/localizedname(forfamily:face:).md)
  Returns a localized string with the name of the specified font family and face, if one exists.
### Sending Action Methods
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
- [enum NSFontAction](nsfontaction.md)
  Actions that modify a font.
### Converting Fonts Automatically
- [func convert(NSFont) -> NSFont](nsfontmanager/convert(_:).md)
  Converts the given font according to the object that initiated a font change, typically the Font panel or Font menu.
### Converting Fonts Manually
- [func convert(NSFont, toFace: String) -> NSFont?](nsfontmanager/convert(_:toface:).md)
  Returns a font whose traits are as similar as possible to those of the given font except for the typeface, which is changed to the given typeface.
- [func convert(NSFont, toFamily: String) -> NSFont](nsfontmanager/convert(_:tofamily:).md)
  Returns a font whose traits are as similar as possible to those of the given font except for the font family, which is changed to the given family.
- [func convert(NSFont, toHaveTrait: NSFontTraitMask) -> NSFont](nsfontmanager/convert(_:tohavetrait:).md)
  Returns a new version of the font object containing a single additional trait.
- [func convert(NSFont, toNotHaveTrait: NSFontTraitMask) -> NSFont](nsfontmanager/convert(_:tonothavetrait:).md)
  Returns a new version of a font object without the specified traits.
- [func convert(NSFont, toSize: CGFloat) -> NSFont](nsfontmanager/convert(_:tosize:).md)
  Returns a font object whose traits are the same as those of the given font, except for the size, which is changed to the given size.
- [func convertWeight(Bool, of: NSFont) -> NSFont](nsfontmanager/convertweight(_:of:).md)
  Returns a font object whose weight is greater or lesser than that of the given font.
- [var currentFontAction: NSFontAction](nsfontmanager/currentfontaction.md)
  The current font conversion action.
- [func convertFontTraits(NSFontTraitMask) -> NSFontTraitMask](nsfontmanager/convertfonttraits(_:).md)
  Converts font traits to a new traits mask value.
### Getting a Particular Font
- [func font(withFamily: String, traits: NSFontTraitMask, weight: Int, size: CGFloat) -> NSFont?](nsfontmanager/font(withfamily:traits:weight:size:).md)
  Attempts to load a font with the specified characteristics.
### Examining Fonts
- [func traits(of: NSFont) -> NSFontTraitMask](nsfontmanager/traits(of:).md)
  Returns the traits of the given font.
- [func fontNamed(String, hasTraits: NSFontTraitMask) -> Bool](nsfontmanager/fontnamed(_:hastraits:).md)
  Indicates whether the given font has all the specified traits.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [func weight(of: NSFont) -> Int](nsfontmanager/weight(of:).md)
  Returns an approximation of the specified font’s weight.
### Managing the Font Panel and Font Menu
- [var isEnabled: Bool](nsfontmanager/isenabled.md)
  A Boolean value that indicates whether the font conversion system’s Font panel and Font menu items are enabled.
- [func fontPanel(Bool) -> NSFontPanel?](nsfontmanager/fontpanel(_:).md)
  Returns the application’s shared Font panel object, creating it if necessary.
- [func setFontMenu(NSMenu)](nsfontmanager/setfontmenu(_:).md)
  Records the given menu as the application’s Font menu.
- [func fontMenu(Bool) -> NSMenu?](nsfontmanager/fontmenu(_:).md)
  Returns the menu that’s connected to the font conversion system, creating it if necessary.
### Accessing the Action Property
- [var action: Selector](nsfontmanager/action.md)
  The action sent to the first responder when the user selects a new font from the Font panel or chooses a command from the Font menu.
- [var target: AnyObject?](nsfontmanager/target.md)
  The object that receives action messages related to the font manager.
### Setting Attributes
- [func setSelectedAttributes([String : Any], isMultiple: Bool)](nsfontmanager/setselectedattributes(_:ismultiple:).md)
  Informs the Font panel that the specified font attributes changed for the selected text.
- [func convertAttributes([String : Any]) -> [String : Any]](nsfontmanager/convertattributes(_:).md)
  Converts attributes in response to an object initiating an attribute change, typically the Font panel or Font menu.
### Deprecated
- [Deprecated Symbols](nsfontmanager-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSFontCollection](nsfontcollection.md)
  A font collection, which is a group of font descriptors taken together as a single object.
- [class NSMutableFontCollection](nsmutablefontcollection.md)
  A mutable collection of font descriptors taken together as a single object.
- [struct NSFontCollectionOptions](nsfontcollectionoptions.md)
  Constants that support font collection management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontmanager)*