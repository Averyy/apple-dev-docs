# MPLanguageOptionCharacteristicContainsOnlyForcedSubtitles

**Framework**: Media Player  
**Kind**: var

Indicates that the language option presents only forced subtitles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
let MPLanguageOptionCharacteristicContainsOnlyForcedSubtitles: String
```

#### Discussion

Language options with forced-only subtitles are typically selected when the user hasn’t selected a legible option with an accessibility characteristic or an auxiliary purpose and its locale matches the locale of the selected audible language option. The system infers the presence of this characteristic for a legible language option from the format description of the associated track that presents the subtitle media.

## See Also

- [let MPLanguageOptionCharacteristicDescribesMusicAndSound: String](mplanguageoptioncharacteristicdescribesmusicandsound.md)
  Indicates that the language option includes legible content in the language of its specified locale that describes music and sound effects occurring in program audio.
- [let MPLanguageOptionCharacteristicDescribesVideo: String](mplanguageoptioncharacteristicdescribesvideo.md)
  Indicates that the language option includes audible content that describes the visual portion of the presentation.
- [let MPLanguageOptionCharacteristicDubbedTranslation: String](mplanguageoptioncharacteristicdubbedtranslation.md)
  Indicates that the language option includes content that contains a dubbed translation.
- [let MPLanguageOptionCharacteristicEasyToRead: String](mplanguageoptioncharacteristiceasytoread.md)
  Indicates that the language option provides legible content in the language of its specified locale and that the content was edited for ease of reading.
- [let MPLanguageOptionCharacteristicIsAuxiliaryContent: String](mplanguageoptioncharacteristicisauxiliarycontent.md)
  Indicates that the language option includes content that’s marked by the content author as auxiliary to the presentation of the language option.
- [let MPLanguageOptionCharacteristicIsMainProgramContent: String](mplanguageoptioncharacteristicismainprogramcontent.md)
  Indicates that the language option includes content that’s marked by the content author as intrinsic to the presentation of the language option.
- [let MPLanguageOptionCharacteristicLanguageTranslation: String](mplanguageoptioncharacteristiclanguagetranslation.md)
  Indicates that the language option contains a translation in the language of its specified locale.
- [let MPLanguageOptionCharacteristicTranscribesSpokenDialog: String](mplanguageoptioncharacteristictranscribesspokendialog.md)
  Indicates that the language option includes legible content in the language of its specified locale that transcribes spoken dialog.
- [let MPLanguageOptionCharacteristicVoiceOverTranslation: String](mplanguageoptioncharacteristicvoiceovertranslation.md)
  Indicates that the language option includes voice over content in the language of its specified locale describes translated dialog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mplanguageoptioncharacteristiccontainsonlyforcedsubtitles)*