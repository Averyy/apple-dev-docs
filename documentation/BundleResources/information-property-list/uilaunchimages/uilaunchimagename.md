# UILaunchImageName

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A string containing the name of the image file.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 13.0

## Details

- **Name**: `UILaunchImageName`
- **Type**: string

#### Discussion

The image file must reside at the top level of the app bundle. The name you specify for this key should not include a filename extension, nor should it include modifiers such as `@2x`, `-568h`, `~iphone`, or `~ipad`.

On disk, your image filenames may still include the modifiers as appropriate, although they are not required. The system automatically considers such modifiers when choosing which file to load.

## See Also

### Launch Image Configuration
- [UILaunchImageMinimumOSVersion](./uilaunchimageminimumosversion.md)
  A string representing the minimum iOS version number for which the image is intended.
- [UILaunchImageOrientation](./uilaunchimageorientation.md)
  A string containing the orientation of the image
- [UILaunchImageSize](./uilaunchimagesize.md)
  A string containing the width and height of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchimages/uilaunchimagename)*