# NSImage.Name

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

Named images, defined by the system or you, for use in your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
typealias Name = String
```

```c
typedef NSString * NSImageName;
```

#### Discussion

The appearance of system-supplied images can change between releases. If you use an image for its intended purpose (and not because of how it looks), your code should look correct from release to release.

The size and aspect ratio of system images can also change between releases. In some situations, you should explicitly resize images as appropriate for your use. If you use these images in conjunction with an [`NSButtonCell`](../nsbuttoncell.md) object, however, you can use the [`imageScaling`](../nsbuttoncell/imagescaling.md) property of the cell to control scaling instead. Similarly, for an [`NSSegmentedCell`](../nssegmentedcell.md) object, you can use the [`setImageScaling(_:forSegment:)`](../nssegmentedcell/setimagescaling%28_,forsegment%29.md): method to control scaling.

Constants that end in the word “Template” represent template images. These images can be processed into variants appropriate for different situations.  For example, these images can invert in a selected table view row. See [`isTemplate`](./istemplate.md) for more information.

Some images also contain the word “FreestandingTemplate”.  These images are template images that are appropriate for use as a borderless button—that is, it doesn’t need any extra bezel artwork behind it.

## Topics

### System Images
- [class let actionTemplateName: String](./actiontemplatename.md)
  An action menu template image.
- [class let addTemplateName: String](./addtemplatename.md)
  An add item template image.
- [class let advancedName: String](./advancedname.md)
  Advanced preferences toolbar icon for the preferences window.
- [class let applicationIconName: String](./applicationiconname.md)
  The app’s icon.
- [class let bluetoothTemplateName: String](./bluetoothtemplatename.md)
  A Bluetooth template image.
- [class let bonjourName: String](./bonjourname.md)
  A Bonjour icon.
- [class let bookmarksTemplateName: String](./bookmarkstemplatename.md)
  Bookmarks image suitable for a template.
- [class let cautionName: String](./cautionname.md)
  A caution image.
- [class let colorPanelName: String](./colorpanelname.md)
  A color panel toolbar icon.
- [class let columnViewTemplateName: String](./columnviewtemplatename.md)
  A column view mode template image.
- [class let computerName: String](./computername.md)
  A computer icon.
- [class let enterFullScreenTemplateName: String](./enterfullscreentemplatename.md)
  An enter full-screen mode template image.
- [class let everyoneName: String](./everyonename.md)
  Permissions for all users.
- [class let exitFullScreenTemplateName: String](./exitfullscreentemplatename.md)
  An exit full-screen mode template image.
- [class let flowViewTemplateName: String](./flowviewtemplatename.md)
  A cover flow view mode template image.
- [class let folderName: String](./foldername.md)
  A folder image.
- [class let folderBurnableName: String](./folderburnablename.md)
  A burnable folder icon.
- [class let folderSmartName: String](./foldersmartname.md)
  A smart folder icon.
- [class let followLinkFreestandingTemplateName: String](./followlinkfreestandingtemplatename.md)
  A link template image.
- [class let fontPanelName: String](./fontpanelname.md)
  A font panel toolbar icon.
- [class let goBackTemplateName: String](./gobacktemplatename.md)
  A “go back” template image.
- [class let goForwardTemplateName: String](./goforwardtemplatename.md)
  A “go forward” template image.
- [class let goLeftTemplateName: String](./golefttemplatename.md)
  A “go back” template image.
- [class let goRightTemplateName: String](./gorighttemplatename.md)
  A “go forward” template image.
- [class let homeTemplateName: String](./hometemplatename.md)
  Home image suitable for a template.
- [class let iChatTheaterTemplateName: String](./ichattheatertemplatename.md)
  An iChat Theater template image.
- [class let iconViewTemplateName: String](./iconviewtemplatename.md)
  An icon view mode template image.
- [class let infoName: String](./infoname.md)
  An information toolbar icon.
- [class let invalidDataFreestandingTemplateName: String](./invaliddatafreestandingtemplatename.md)
  A template image used to denote invalid data.
- [class let leftFacingTriangleTemplateName: String](./leftfacingtriangletemplatename.md)
  A generic left-facing triangle template image.
- [class let listViewTemplateName: String](./listviewtemplatename.md)
  A list view mode template image.
- [class let lockLockedTemplateName: String](./locklockedtemplatename.md)
  A locked padlock template image.
- [class let lockUnlockedTemplateName: String](./lockunlockedtemplatename.md)
  An unlocked padlock template image.
- [class let menuMixedStateTemplateName: String](./menumixedstatetemplatename.md)
  A horizontal dash, for use in menus.
- [class let menuOnStateTemplateName: String](./menuonstatetemplatename.md)
  A check mark template image, for use in menus.
- [class let mobileMeName: String](./mobilemename.md)
  A MobileMe icon.
- [class let multipleDocumentsName: String](./multipledocumentsname.md)
  A drag image for multiple items.
- [class let networkName: String](./networkname.md)
  A network icon.
- [class let pathTemplateName: String](./pathtemplatename.md)
  A path button template image.
- [class let preferencesGeneralName: String](./preferencesgeneralname.md)
  General preferences toolbar icon for the preferences window.
- [class let quickLookTemplateName: String](./quicklooktemplatename.md)
  A Quick Look template image.
- [class let refreshFreestandingTemplateName: String](./refreshfreestandingtemplatename.md)
  A refresh template image.
- [class let refreshTemplateName: String](./refreshtemplatename.md)
  A refresh template image.
- [class let removeTemplateName: String](./removetemplatename.md)
  A remove item template image.
- [class let revealFreestandingTemplateName: String](./revealfreestandingtemplatename.md)
  A reveal contents template image.
- [class let rightFacingTriangleTemplateName: String](./rightfacingtriangletemplatename.md)
  A generic right-facing triangle template image.
- [class let shareTemplateName: String](./sharetemplatename.md)
  A share view template image.
- [class let slideshowTemplateName: String](./slideshowtemplatename.md)
  A slideshow template image.
- [class let smartBadgeTemplateName: String](./smartbadgetemplatename.md)
  A badge for a “smart” item.
- [class let statusAvailableName: String](./statusavailablename.md)
  Small green indicator, similar to iChat’s available image.
- [class let statusNoneName: String](./statusnonename.md)
  Small clear indicator.
- [class let statusPartiallyAvailableName: String](./statuspartiallyavailablename.md)
  Small yellow indicator, similar to iChat’s idle image.
- [class let statusUnavailableName: String](./statusunavailablename.md)
  Small red indicator, similar to iChat’s unavailable image.
- [class let stopProgressFreestandingTemplateName: String](./stopprogressfreestandingtemplatename.md)
  A stop progress template image.
- [class let stopProgressTemplateName: String](./stopprogresstemplatename.md)
  A stop progress button template image.
- [class let touchBarAddDetailTemplateName: String](./touchbaradddetailtemplatename.md)
  A template image for showing additional detail for an item.
- [class let touchBarAddTemplateName: String](./touchbaraddtemplatename.md)
  A template image for creating a new item.
- [class let touchBarAlarmTemplateName: String](./touchbaralarmtemplatename.md)
  A template image for setting or showing an alarm.
- [class let touchBarAudioInputMuteTemplateName: String](./touchbaraudioinputmutetemplatename.md)
  A template image for muting audio input or denoting that audio input is muted.
- [class let touchBarAudioInputTemplateName: String](./touchbaraudioinputtemplatename.md)
  A template image for denoting audio input.
- [class let touchBarAudioOutputMuteTemplateName: String](./touchbaraudiooutputmutetemplatename.md)
  A template image for muting audio output or for denoting that audio output is muted.
- [class let touchBarAudioOutputVolumeHighTemplateName: String](./touchbaraudiooutputvolumehightemplatename.md)
  A template image for setting the audio output volume to a high level, or for denoting that the audio is at the peak volume.
- [class let touchBarAudioOutputVolumeLowTemplateName: String](./touchbaraudiooutputvolumelowtemplatename.md)
  A template image for setting the audio output volume to a low level, or for denoting that it is set to a low level.
- [class let touchBarAudioOutputVolumeMediumTemplateName: String](./touchbaraudiooutputvolumemediumtemplatename.md)
  A template image for setting the audio output volume to a medium level, or for denoting that it is set to a medium level.
- [class let touchBarAudioOutputVolumeOffTemplateName: String](./touchbaraudiooutputvolumeofftemplatename.md)
  A template image for setting the audio output volume to silent, or for denoting that it is set to silent.
- [class let touchBarBookmarksTemplateName: String](./touchbarbookmarkstemplatename.md)
  A template image for showing app-specific bookmarks.
- [class let touchBarColorPickerFillName: String](./touchbarcolorpickerfillname.md)
  A template image for showing a color picker so the user can select a fill color.
- [class let touchBarColorPickerFontName: String](./touchbarcolorpickerfontname.md)
  A template image for showing a color picker so the user can select a text color.
- [class let touchBarColorPickerStrokeName: String](./touchbarcolorpickerstrokename.md)
  A template image for showing a color picker so the user can select a stroke color.
- [class let touchBarCommunicationAudioTemplateName: String](./touchbarcommunicationaudiotemplatename.md)
  A template image for initiating or denoting audio communication.
- [class let touchBarCommunicationVideoTemplateName: String](./touchbarcommunicationvideotemplatename.md)
  A template image for initiating or denoting video communication.
- [class let touchBarComposeTemplateName: String](./touchbarcomposetemplatename.md)
  A template image for opening a new document or view in edit mode.
- [class let touchBarDeleteTemplateName: String](./touchbardeletetemplatename.md)
  A template image for deleting the current or selected item.
- [class let touchBarDownloadTemplateName: String](./touchbardownloadtemplatename.md)
  A template image for downloading an item.
- [class let touchBarEnterFullScreenTemplateName: String](./touchbarenterfullscreentemplatename.md)
  A template image for entering full screen mode.
- [class let touchBarExitFullScreenTemplateName: String](./touchbarexitfullscreentemplatename.md)
  A template image for exiting full screen mode.
- [class let touchBarFastForwardTemplateName: String](./touchbarfastforwardtemplatename.md)
  A template image for moving forward through media playback or slides.
- [class let touchBarFolderCopyToTemplateName: String](./touchbarfoldercopytotemplatename.md)
  A template image for copying an item to a destination.
- [class let touchBarFolderMoveToTemplateName: String](./touchbarfoldermovetotemplatename.md)
  A template image for moving an item to a destination.
- [class let touchBarFolderTemplateName: String](./touchbarfoldertemplatename.md)
  A template image for opening or representing a folder.
- [class let touchBarGetInfoTemplateName: String](./touchbargetinfotemplatename.md)
  A template image for showing information about an item.
- [class let touchBarGoBackTemplateName: String](./touchbargobacktemplatename.md)
  A template image for returning to the previous screen or location.
- [class let touchBarGoDownTemplateName: String](./touchbargodowntemplatename.md)
  A template image for moving to the next item in a list.
- [class let touchBarGoForwardTemplateName: String](./touchbargoforwardtemplatename.md)
  A template image for moving to the next screen or location.
- [class let touchBarGoUpTemplateName: String](./touchbargouptemplatename.md)
  A template image for moving to the previous item in a list.
- [class let touchBarHistoryTemplateName: String](./touchbarhistorytemplatename.md)
  A template image for showing history information, such as recent downloads.
- [class let touchBarIconViewTemplateName: String](./touchbariconviewtemplatename.md)
  A template image for showing items in an icon view.
- [class let touchBarListViewTemplateName: String](./touchbarlistviewtemplatename.md)
  A template image for showing items in a list view.
- [class let touchBarMailTemplateName: String](./touchbarmailtemplatename.md)
  A template image for creating an email message.
- [class let touchBarNewFolderTemplateName: String](./touchbarnewfoldertemplatename.md)
  A template image for creating a new folder.
- [class let touchBarNewMessageTemplateName: String](./touchbarnewmessagetemplatename.md)
  A template image for creating a new message, or for denoting the use of messaging.
- [class let touchBarOpenInBrowserTemplateName: String](./touchbaropeninbrowsertemplatename.md)
  A template image for opening an item in the user’s browser.
- [class let touchBarPauseTemplateName: String](./touchbarpausetemplatename.md)
  A template image for pausing media playback or slides.
- [class let touchBarPlayPauseTemplateName: String](./touchbarplaypausetemplatename.md)
  A template image for toggling between playing and pausing media or slides.
- [class let touchBarPlayTemplateName: String](./touchbarplaytemplatename.md)
  A template image for starting or resuming playback of media or slides.
- [class let touchBarPlayheadTemplateName: String](./touchbarplayheadtemplatename.md)
  A template image for denoting the current playback position within a timeline track.
- [class let touchBarQuickLookTemplateName: String](./touchbarquicklooktemplatename.md)
  A template image for opening an item in Quick Look.
- [class let touchBarRecordStartTemplateName: String](./touchbarrecordstarttemplatename.md)
  A template image for starting recording.
- [class let touchBarRecordStopTemplateName: String](./touchbarrecordstoptemplatename.md)
  A template image for stopping recording or stopping playback of media or slides.
- [class let touchBarRefreshTemplateName: String](./touchbarrefreshtemplatename.md)
  A template image for refreshing displayed data.
- [class let touchBarRemoveTemplateName: String](./touchbarremovetemplatename.md)
  A template image for removing an item.
- [class let touchBarRewindTemplateName: String](./touchbarrewindtemplatename.md)
  A template image for moving backwards through media or slides.
- [class let touchBarRotateLeftTemplateName: String](./touchbarrotatelefttemplatename.md)
  A template image for rotating an item counterclockwise.
- [class let touchBarRotateRightTemplateName: String](./touchbarrotaterighttemplatename.md)
  A template image for rotating an item clockwise.
- [class let touchBarSearchTemplateName: String](./touchbarsearchtemplatename.md)
  A template image for showing a search field or for initiating a search.
- [class let touchBarShareTemplateName: String](./touchbarsharetemplatename.md)
  A template image for sharing content with others directly or via social media.
- [class let touchBarSidebarTemplateName: String](./touchbarsidebartemplatename.md)
  A template image for showing a sidebar in the current view.
- [class let touchBarSkipAhead15SecondsTemplateName: String](./touchbarskipahead15secondstemplatename.md)
  A template image for skipping ahead 15 seconds during media playback.
- [class let touchBarSkipAhead30SecondsTemplateName: String](./touchbarskipahead30secondstemplatename.md)
  A template image for skipping ahead 30 seconds during media playback.
- [class let touchBarSkipAheadTemplateName: String](./touchbarskipaheadtemplatename.md)
  A template image for skipping to the next chapter or location during media playback.
- [class let touchBarSkipBack15SecondsTemplateName: String](./touchbarskipback15secondstemplatename.md)
  A template image for skipping back 15 seconds during media playback.
- [class let touchBarSkipBack30SecondsTemplateName: String](./touchbarskipback30secondstemplatename.md)
  A template image for skipping back 30 seconds during media playback.
- [class let touchBarSkipBackTemplateName: String](./touchbarskipbacktemplatename.md)
  A template image for skipping to the previous chapter or location during media playback.
- [class let touchBarSkipToEndTemplateName: String](./touchbarskiptoendtemplatename.md)
  A template image for skipping to the end of media playback.
- [class let touchBarSkipToStartTemplateName: String](./touchbarskiptostarttemplatename.md)
  A template image for skipping to the start of media playback.
- [class let touchBarSlideshowTemplateName: String](./touchbarslideshowtemplatename.md)
  A template image for starting a slideshow.
- [class let touchBarTagIconTemplateName: String](./touchbartagicontemplatename.md)
  A template image for applying a tag to an item.
- [class let touchBarTextBoldTemplateName: String](./touchbartextboldtemplatename.md)
  A template image for making selected text bold.
- [class let touchBarTextBoxTemplateName: String](./touchbartextboxtemplatename.md)
  A template image for inserting a text box.
- [class let touchBarTextCenterAlignTemplateName: String](./touchbartextcenteraligntemplatename.md)
  A template image for centering text.
- [class let touchBarTextItalicTemplateName: String](./touchbartextitalictemplatename.md)
  A template image for italicizing the selected text.
- [class let touchBarTextJustifiedAlignTemplateName: String](./touchbartextjustifiedaligntemplatename.md)
  A template image for fully justifying text.
- [class let touchBarTextLeftAlignTemplateName: String](./touchbartextleftaligntemplatename.md)
  A template image for aligning text to the left.
- [class let touchBarTextListTemplateName: String](./touchbartextlisttemplatename.md)
  A template image for inserting a list or converting text to list form.
- [class let touchBarTextRightAlignTemplateName: String](./touchbartextrightaligntemplatename.md)
  A template image for aligning text to the right.
- [class let touchBarTextStrikethroughTemplateName: String](./touchbartextstrikethroughtemplatename.md)
  A template image for striking through text.
- [class let touchBarTextUnderlineTemplateName: String](./touchbartextunderlinetemplatename.md)
  A template image for underlining text.
- [class let touchBarUserAddTemplateName: String](./touchbaruseraddtemplatename.md)
  A template image for creating a new user account.
- [class let touchBarUserGroupTemplateName: String](./touchbarusergrouptemplatename.md)
  A template image for showing or representing a group of users.
- [class let touchBarUserTemplateName: String](./touchbarusertemplatename.md)
  A template image for showing or representing user information.
- [class let touchBarVolumeDownTemplateName: String](./touchbarvolumedowntemplatename.md)
  A template image for reducing the audio output volume.
- [class let touchBarVolumeUpTemplateName: String](./touchbarvolumeuptemplatename.md)
  A template image for increasing the audio output volume.
- [class let trashEmptyName: String](./trashemptyname.md)
  An image of the empty trash can.
- [class let trashFullName: String](./trashfullname.md)
  An image of the full trash can.
- [class let userName: String](./username.md)
  Permissions for a single user.
- [class let userAccountsName: String](./useraccountsname.md)
  User account toolbar icon for the preferences window.
- [class let userGroupName: String](./usergroupname.md)
  Permissions for a group of users.
- [class let userGuestName: String](./userguestname.md)
  Permissions for guests.

## See Also

### Creating Images by Name
- [Configuring and displaying symbol images in your UI](../../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [init?(named: NSImage.Name)](./init%28named%29.md)
  Returns the image object associated with the specified name.
- [convenience init?(systemSymbolName: String, accessibilityDescription: String?)](./init%28systemsymbolname,accessibilitydescription%29.md)
  Creates a symbol image with the system symbol name and accessibility description you specify.
- [convenience init?(systemSymbolName: String, variableValue: Double, accessibilityDescription: String?)](./init%28systemsymbolname,variablevalue,accessibilitydescription%29.md)
  Creates a symbol image with the system symbol name and variable value you specify.
- [convenience init?(symbolName: String, variableValue: Double)](./init%28symbolname,variablevalue%29.md)
  Creates a symbol image with the symbol name and variable value you specify.
- [convenience init?(symbolName: String, bundle: Bundle?, variableValue: Double)](./init%28symbolname,bundle,variablevalue%29.md)
  Creates a symbol image with the specified symbol name and variable value.
- [convenience init(resource: ImageResource)](./init%28resource%29.md)
  Initialize a `NSImage` with an image resource.
- [func setName(NSImage.Name?) -> Bool](./setname%28_%29.md)
  Registers the image object under the specified name.
- [func name() -> NSImage.Name?](./name%28%29.md)
  Returns the name associated with the image, if any.
- [convenience init(imageLiteralResourceName: String)](./init%28imageliteralresourcename%29.md)
  Creates an image initialized with the specified resource name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/name-swift.typealias)*