# UILaunchImageName

**Framework**: Bundle Resources  
**Kind**: typealias

A string containing the name of the image file.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- tvOS 9.0+

#### Discussion

The image file must reside at the top level of the app bundle. The name you specify for this key should not include a filename extension, nor should it include modifiers such as `@2x`, `-568h`, `~iphone`, or `~ipad`.

On disk, your image filenames may still include the modifiers as appropriate, although they are not required. The system automatically considers such modifiers when choosing which file to load.

## See Also

- [UILaunchImageMinimumOSVersion](information-property-list/uilaunchimages/uilaunchimageminimumosversion.md)
  A string representing the minimum iOS version number for which the image is intended.
- [UILaunchImageOrientation](information-property-list/uilaunchimages/uilaunchimageorientation.md)
  A string containing the orientation of the image
- [UILaunchImageSize](information-property-list/uilaunchimages/uilaunchimagesize.md)
  A string containing the width and height of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchimages/uilaunchimagename)*