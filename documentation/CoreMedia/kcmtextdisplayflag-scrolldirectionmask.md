# kCMTextDisplayFlag_scrollDirectionMask

**Framework**: Core Media  
**Kind**: var

A flag that describes the scrolling direction is set by a two-bit field, obtained from displayFlags using kCMTextDisplayFlag_scrollDirectionMask.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kCMTextDisplayFlag_scrollDirectionMask: CMTextDisplayFlags { get }
```

## See Also

- [var kCMTextDisplayFlag_scrollIn: CMTextDisplayFlags](kcmtextdisplayflag_scrollin.md)
  A flag that describes the text scrolls into the display region.
- [var kCMTextDisplayFlag_scrollOut: CMTextDisplayFlags](kcmtextdisplayflag_scrollout.md)
  A flag that describes the text scrolls out of the display region.
- [var kCMTextDisplayFlag_scrollDirection_bottomToTop: CMTextDisplayFlags](kcmtextdisplayflag_scrolldirection_bottomtotop.md)
  A flag that describes the text is vertically scrolled up (“credits style”), entering from the bottom and leaving towards the top.
- [var kCMTextDisplayFlag_scrollDirection_rightToLeft: CMTextDisplayFlags](kcmtextdisplayflag_scrolldirection_righttoleft.md)
  A flag that describes the text is horizontally scrolled (“marquee style”), entering from the right and leaving towards the left.
- [var kCMTextDisplayFlag_scrollDirection_topToBottom: CMTextDisplayFlags](kcmtextdisplayflag_scrolldirection_toptobottom.md)
  A flag that describes the text is vertically scrolled down, entering from the top and leaving towards the bottom.
- [var kCMTextDisplayFlag_scrollDirection_leftToRight: CMTextDisplayFlags](kcmtextdisplayflag_scrolldirection_lefttoright.md)
  A flag that describes the text is horizontally scrolled, entering from the left and leaving towards the right.
- [var kCMTextDisplayFlag_continuousKaraoke: CMTextDisplayFlags](kcmtextdisplayflag_continuouskaraoke.md)
  A flag that describes enabling the continuous karaoke mode where the range of karaoke highlighting extends to include additional ranges rather than the highlighting moves onto the next range.
- [var kCMTextDisplayFlag_writeTextVertically: CMTextDisplayFlags](kcmtextdisplayflag_writetextvertically.md)
  A flag that describes the text renders vertically.
- [var kCMTextDisplayFlag_fillTextRegion: CMTextDisplayFlags](kcmtextdisplayflag_filltextregion.md)
  A flag that describes the subtitle display bounds are to be filled with the color specified by `kCMTextFormatDescriptionExtension_BackgroundColor`.
- [var kCMTextDisplayFlag_forcedSubtitlesPresent: CMTextDisplayFlags](kcmtextdisplayflag_forcedsubtitlespresent.md)
  A flag that describes forcing subtitles are present, for example, a subtitle which only displays during foreign language sections of the video. Check individual samples to determine what type of subtitle is contained.
- [var kCMTextDisplayFlag_allSubtitlesForced: CMTextDisplayFlags](kcmtextdisplayflag_allsubtitlesforced.md)
  A flag that describes treating all subtitle samples as if they contain forced subtitles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/kcmtextdisplayflag_scrolldirectionmask)*