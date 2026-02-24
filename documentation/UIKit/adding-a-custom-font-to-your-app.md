# Adding a custom font to your app

**Framework**: UIKit

Add a custom font to your app and use it in your app’s interface.

#### Overview

Your app isn’t limited to the custom fonts provided by iOS. If your company has its own branded font, for example, you can use it in your app. Add the font file that contains your font to your app bundle, then use your font the same way you use any of the iOS-provided custom fonts.

##### Add the Font File to Your Xcode Project

To add a font file to your Xcode project, select *File > Add Files to “Your Project Name”* from the menu bar, or drag the file from Finder and drop it into your Xcode project. You can add True Type Font (.ttf) and Open Type Font (.otf) files.

![A screenshot of the Project Navigator showing the custom font files added to the CustomFont project.](https://docs-assets.developer.apple.com/published/16adcb2425ff69c1754dac73fdc4ab7b/adding-a-custom-font-to-your-app-1%402x.png)

Also, make sure the font file is a target member of your app; otherwise, the project will not distribute the font file as part of your app.

![A screenshot of the File Inspector showing that the selected font file is a member of the CustomFont target.](https://docs-assets.developer.apple.com/published/d6e6408416bdd2136be6d6f9d4bc0261/adding-a-custom-font-to-your-app-2%402x.png)

##### Register Your Font File with Ios

After adding the font file to your project, you need to let iOS know about the font. To do this, add the key “Fonts provided by application” to the information property list (the raw key name is `UIAppFonts`). Xcode creates an array value for the key; add the names of each font file as items of the array. Be sure to include the file extension as part of the name.

![Screenshot of Xcode showing the contents of the Info.plist file. The 'Fonts provided by application' key contains the filenames of two font files.](https://docs-assets.developer.apple.com/published/c26b6e009ff7648d7b3108a0362511de/adding-a-custom-font-to-your-app-3%402x.png)

Include each font file you add to your project in this array; otherwise, the font will not be available to your app.

##### Use Your Custom Font in Interface Builder

After you add the font file to your Xcode project and its *Info.plist*, you can begin assigning the font to UI objects like [`UILabel`](uilabel.md) and [`UITextField`](uitextfield.md). If you’re using Interface Builder, assign the UI object’s *Font* setting to your custom font using the Attribute Inspector.

![Screenshot of Interface Builder showing that the font for the label is 'CustomFont 17.0.'](https://docs-assets.developer.apple.com/published/da57e8ce6b34b8e2896a97931995291d/adding-a-custom-font-to-your-app-4%402x.png)

##### Use Your Custom Font in Source Code

You can create an instance of your custom font in source code. To do this, you need to know the font name.  However, the name of the font isn’t always obvious, and rarely matches the font file name. A quick way to find the font name is to get the list of fonts available to your app, which you can do with the following code:

```swift
for family in UIFont.familyNames.sorted() {
    let names = UIFont.fontNames(forFamilyName: family)
    print("Family: \(family) Font names: \(names)")
}
```

Once you know the font name, create an instance of the custom font using [`UIFont`](uifont.md). If your app supports Dynamic Type, you can also get a scaled instance of your font, as shown here:

```swift
guard let customFont = UIFont(name: "CustomFont-Light", size: UIFont.labelFontSize) else {
    fatalError("""
        Failed to load the "CustomFont-Light" font.
        Make sure the font file is included in the project and the font name is spelled correctly.
        """
    )
}
label.font = UIFontMetrics.default.scaledFont(for: customFont)
label.adjustsFontForContentSizeCategory = true
```

For more information on using scaled fonts, see [`Scaling fonts automatically`](scaling-fonts-automatically.md).

## See Also

- [Scaling fonts automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [class UIFont](uifont.md)
  An object that provides access to the font’s characteristics.
- [class UIFontDescriptor](uifontdescriptor.md)
  A collection of attributes that describes a font.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [class UIFontMetrics](uifontmetrics.md)
  A utility object for obtaining custom fonts that scale to support Dynamic Type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/adding-a-custom-font-to-your-app)*