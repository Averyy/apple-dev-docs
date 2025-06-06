# Captions

**Framework**: Media Accessibility

Coordinate the presentation of closed-captioned data for your app’s media files.

#### Overview

People can create custom styles for caption appearance in Accessibility settings. The Media Accessibility framework provides access to these user-captioning settings.

In macOS, choose System Settings > Accessibility > Captions to access these options.

![Screenshot of the Accessibility settings in macOS with Captions selected.](https://docs-assets.developer.apple.com/published/cf4c877230b565749de2dc221c1d7e44/media-3709928%402x.png)

When a person creates a custom caption style, the settings affect attributes, such as caption color, font, and language.

![Screenshot of the Captions settings for a custom style in macOS.](https://docs-assets.developer.apple.com/published/ebc6720d9ef8c9e762f4375c3f9a7414/media-3709929%402x.png)

By choosing custom styles for media text, people are requesting improved legibility. The Media Accessibility functions let you to tailor the user experience of your media content. You must be able to influence the caption-rendering process at time of delivery for the following functions to be useful. Retrieving a person’s preferences and dynamically rendering the captions for maximum readability provides the best user experience.

## Topics

### General settings
- [let kMACaptionAppearanceSettingsChangedNotification: CFString](kmacaptionappearancesettingschangednotification.md)
  A notification that occurs when any user-defined caption settings change.
- [func MACaptionAppearanceDidDisplayCaptions(CFArray)](macaptionappearancediddisplaycaptions(_:).md)
  Informs accessibility clients when captions display onscreen.
- [func MACaptionAppearanceCopyPreferredCaptioningMediaCharacteristics(MACaptionAppearanceDomain) -> Unmanaged<CFArray>](macaptionappearancecopypreferredcaptioningmediacharacteristics(_:).md)
  Returns the preferences for captioning sounds.
- [func MACaptionAppearanceGetDisplayType(MACaptionAppearanceDomain) -> MACaptionAppearanceDisplayType](macaptionappearancegetdisplaytype(_:).md)
  Returns the preferred type of captions to display.
- [func MACaptionAppearanceSetDisplayType(MACaptionAppearanceDomain, MACaptionAppearanceDisplayType)](macaptionappearancesetdisplaytype(_:_:).md)
  Sets the preference for the type of caption.
### Language settings
- [func MACaptionAppearanceAddSelectedLanguage(MACaptionAppearanceDomain, CFString) -> Bool](macaptionappearanceaddselectedlanguage(_:_:).md)
  Adds a preference for caption language to the stack of languages.
- [func MACaptionAppearanceCopySelectedLanguages(MACaptionAppearanceDomain) -> Unmanaged<CFArray>](macaptionappearancecopyselectedlanguages(_:).md)
  Returns the preferred caption languages.
### Text settings
- [func MACaptionAppearanceCopyFontDescriptorForStyle(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?, MACaptionAppearanceFontStyle) -> Unmanaged<CTFontDescriptor>](macaptionappearancecopyfontdescriptorforstyle(_:_:_:).md)
  Returns the preferred font for the specified style of type.
- [func MACaptionAppearanceCopyForegroundColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](macaptionappearancecopyforegroundcolor(_:_:).md)
  Returns the preference for text color.
- [func MACaptionAppearanceGetForegroundOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetforegroundopacity(_:_:).md)
  Returns the preference for text opacity.
- [func MACaptionAppearanceGetRelativeCharacterSize(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetrelativecharactersize(_:_:).md)
  Returns the preference for font scaling.
- [func MACaptionAppearanceGetTextEdgeStyle(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> MACaptionAppearanceTextEdgeStyle](macaptionappearancegettextedgestyle(_:_:).md)
  Returns the preference for text edge style.
### Text highlight settings
- [func MACaptionAppearanceCopyBackgroundColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](macaptionappearancecopybackgroundcolor(_:_:).md)
  Returns the preference for the text highlight color.
- [func MACaptionAppearanceGetBackgroundOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetbackgroundopacity(_:_:).md)
  Returns the preference for the text highlight opacity.
### Caption window settings
- [func MACaptionAppearanceCopyWindowColor(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> Unmanaged<CGColor>](macaptionappearancecopywindowcolor(_:_:).md)
  Returns the preference for the caption window’s color.
- [func MACaptionAppearanceGetWindowOpacity(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetwindowopacity(_:_:).md)
  Returns the preference for the overlay’s opacity.
- [func MACaptionAppearanceGetWindowRoundedCornerRadius(MACaptionAppearanceDomain, UnsafeMutablePointer<MACaptionAppearanceBehavior>?) -> CGFloat](macaptionappearancegetwindowroundedcornerradius(_:_:).md)
  Returns the radius of the caption window’s corners.
### Image captioning settings
- [func MAImageCaptioningCopyCaption(CFURL, UnsafeMutablePointer<CFError?>?) -> CFString?](maimagecaptioningcopycaption(_:_:).md)
  Returns an accessibility caption from an image’s metadata.
- [func MAImageCaptioningSetCaption(CFURL, CFString?, UnsafeMutablePointer<CFError?>?) -> Bool](maimagecaptioningsetcaption(_:_:_:).md)
  Sets the accessibility caption for an image’s metadata.
- [func MAImageCaptioningCopyMetadataTagPath() -> CFString](maimagecaptioningcopymetadatatagpath().md)
  Returns the metadata tag path.
### Audible media selection settings
- [let kMAAudibleMediaSettingsChangedNotification: CFString](kmaaudiblemediasettingschangednotification.md)
  A notification that occurs when any user-defined audible media settings change.
- [func MAAudibleMediaCopyPreferredCharacteristics() -> Unmanaged<CFArray>](maaudiblemediacopypreferredcharacteristics().md)
  Returns the preference for audible media characteristics.
- [let MAMediaCharacteristicDescribesVideoForAccessibility: CFString](mamediacharacteristicdescribesvideoforaccessibility.md)
  A media characteristic that indicates that a track or media selection option includes audible content that describes a video for accessibility.
- [let MAMediaCharacteristicDescribesMusicAndSoundForAccessibility: CFString](mamediacharacteristicdescribesmusicandsoundforaccessibility.md)
  A media characteristic that indicates that a track includes legible content in the language of its specified locale that describes music and sound other than spoken dialog.
- [let MAMediaCharacteristicTranscribesSpokenDialogForAccessibility: CFString](mamediacharacteristictranscribesspokendialogforaccessibility.md)
  A media characteristic that indicates that a track includes legible content in the language of its specified locale that transcribes spoken dialog and identifies the speakers.
### Constants
- [enum MACaptionAppearanceDomain](macaptionappearancedomain.md)
  A value that specifies which domain to retrieve a preference setting from.
- [enum MACaptionAppearanceDisplayType](macaptionappearancedisplaytype.md)
  A value that specifies the type of captions to display.
- [enum MACaptionAppearanceBehavior](macaptionappearancebehavior.md)
  A value that indicates the preferred behavior for a preference setting.
- [enum MACaptionAppearanceFontStyle](macaptionappearancefontstyle.md)
  A value that specifies a font style.
- [enum MACaptionAppearanceTextEdgeStyle](macaptionappearancetextedgestyle.md)
  A value that specifies a style for the outside of the text.

## See Also

- [Flashing lights](flashing-lights.md)
  Detect, mitigate, and inform people about flashing lights in media content.
- [Music Haptics](music-haptics.md)
  Play haptic tracks along with known music tracks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/captions)*