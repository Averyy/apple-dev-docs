# Picture Taker Keys

**Framework**: Quartz

Keys for customizing the picture taker appearance and behavior. These values are set by sending the picture taker instance `setValue:forKey`.

## Topics

### Constants
- [let IKPictureTakerAllowsVideoCaptureKey: String](ikpicturetakerallowsvideocapturekey.md)
  A key for allowing video capture.
- [let IKPictureTakerAllowsFileChoosingKey: String](ikpicturetakerallowsfilechoosingkey.md)
  A key for allowing the user to choose a file.
- [let IKPictureTakerUpdateRecentPictureKey: String](ikpicturetakerupdaterecentpicturekey.md)
  A key for allowing a recent picture to be updated.
- [let IKPictureTakerAllowsEditingKey: String](ikpicturetakerallowseditingkey.md)
  A key for allowing image editing.
- [let IKPictureTakerShowEffectsKey: String](ikpicturetakershoweffectskey.md)
  A key for showing effects.
- [let IKPictureTakerInformationalTextKey: String](ikpicturetakerinformationaltextkey.md)
  A key for informational text. The associated value is an `NSString` or `NSAttributedString` object whose default value is `"Drag Image Here"`.
- [let IKPictureTakerImageTransformsKey: String](ikpicturetakerimagetransformskey.md)
  A n image transformation key. The associated value is an `NSDictionary` object that can be serialized.
- [let IKPictureTakerOutputImageMaxSizeKey: String](ikpicturetakeroutputimagemaxsizekey.md)
  A key for the maximum size of the output image. The associated value is an `NSValue` object (`NSSize`).
- [let IKPictureTakerCropAreaSizeKey: String](ikpicturetakercropareasizekey.md)
  A key for the cropping area size. The associated value is an `NSValue` object (`NSSize`).
- [let IKPictureTakerShowAddressBookPictureKey: String](ikpicturetakershowaddressbookpicturekey.md)
  A key for showing the address book picture.
- [let IKPictureTakerShowEmptyPictureKey: String](ikpicturetakershowemptypicturekey.md)
  A key for showing an empty picture. The associated value is an `NSImage` object. The default value is `nil`. If set to an image, the picture taker automatically shows an image at the end of the Recent Pictures pop-up menu. that means “no picture.”
- [let IKPictureTakerRemainOpenAfterValidateKey: String](ikpicturetakerremainopenaftervalidatekey.md)
  A key that determines if the picture taker UI should remain open after the user selects done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/picture-taker-keys)*