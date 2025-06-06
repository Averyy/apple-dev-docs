# UILaunchImageSize

**Framework**: Bundle Resources  
**Kind**: typealias

A string containing the width and height of the image.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- tvOS 9.0+

#### Discussion

This string represents the size of the display for which the image is intended. You must specify the width and height with respect to the device in a portrait orientation. In other words, portrait and landscape images targeting the same device would have the same width and height.

The format of this string is {`width, height`} where width and height are the size of the image in points. For example, the string {320, 480} specifies an image that can be used on an iPhone 4 or iPhone 4S.

If you do not specify this key, the image size is assumed to be {320, 480}.

## See Also

- [UILaunchImageMinimumOSVersion](information-property-list/uilaunchimages/uilaunchimageminimumosversion.md)
  A string representing the minimum iOS version number for which the image is intended.
- [UILaunchImageName](information-property-list/uilaunchimages/uilaunchimagename.md)
  A string containing the name of the image file.
- [UILaunchImageOrientation](information-property-list/uilaunchimages/uilaunchimageorientation.md)
  A string containing the orientation of the image


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchimages/uilaunchimagesize)*