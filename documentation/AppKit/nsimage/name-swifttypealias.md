# NSImage.Name

**Framework**: AppKit  
**Kind**: typealias

Named images, defined by the system or you, for use in your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
typealias Name = String
```

#### Discussion

The appearance of system-supplied images can change between releases. If you use an image for its intended purpose (and not because of how it looks), your code should look correct from release to release.

The size and aspect ratio of system images can also change between releases. In some situations, you should explicitly resize images as appropriate for your use. If you use these images in conjunction with an [`NSButtonCell`](nsbuttoncell.md) object, however, you can use the [`imageScaling`](nsbuttoncell/imagescaling.md) property of the cell to control scaling instead. Similarly, for an [`NSSegmentedCell`](nssegmentedcell.md) object, you can use the [`setImageScaling(_:forSegment:)`](nssegmentedcell/setimagescaling(_:forsegment:).md): method to control scaling.

Constants that end in the word “Template” represent template images. These images can be processed into variants appropriate for different situations.  For example, these images can invert in a selected table view row. See [`isTemplate`](nsimage/istemplate.md) for more information.

Some images also contain the word “FreestandingTemplate”.  These images are template images that are appropriate for use as a borderless button—that is, it doesn’t need any extra bezel artwork behind it.

## Topics

### System Images
- [class let actionTemplateName: String](nsimage/actiontemplatename.md)
  An action menu template image.
- [class let addTemplateName: String](nsimage/addtemplatename.md)
  An add item template image.
- [class let advancedName: String](nsimage/advancedname.md)
  Advanced preferences toolbar icon for the preferences window.
- [class let applicationIconName: String](nsimage/applicationiconname.md)
  The app’s icon.
- [class let bluetoothTemplateName: String](nsimage/bluetoothtemplatename.md)
  A Bluetooth template image.
- [class let bonjourName: String](nsimage/bonjourname.md)
  A Bonjour icon.
- [class let bookmarksTemplateName: String](nsimage/bookmarkstemplatename.md)
  Bookmarks image suitable for a template.
- [class let cautionName: String](nsimage/cautionname.md)
  A caution image.
- [class let colorPanelName: String](nsimage/colorpanelname.md)
  A color panel toolbar icon.
- [class let columnViewTemplateName: String](nsimage/columnviewtemplatename.md)
  A column view mode template image.
- [class let computerName: String](nsimage/computername.md)
  A computer icon.
- [class let enterFullScreenTemplateName: String](nsimage/enterfullscreentemplatename.md)
  An enter full-screen mode template image.
- [class let everyoneName: String](nsimage/everyonename.md)
  Permissions for all users.
- [class let exitFullScreenTemplateName: String](nsimage/exitfullscreentemplatename.md)
  An exit full-screen mode template image.
- [class let flowViewTemplateName: String](nsimage/flowviewtemplatename.md)
  A cover flow view mode template image.
- [class let folderName: String](nsimage/foldername.md)
  A folder image.
- [class let folderBurnableName: String](nsimage/folderburnablename.md)
  A burnable folder icon.
- [class let folderSmartName: String](nsimage/foldersmartname.md)
  A smart folder icon.
- [class let followLinkFreestandingTemplateName: String](nsimage/followlinkfreestandingtemplatename.md)
  A link template image.
- [class let fontPanelName: String](nsimage/fontpanelname.md)
  A font panel toolbar icon.
- [class let goBackTemplateName: String](nsimage/gobacktemplatename.md)
  A “go back” template image.
- [class let goForwardTemplateName: String](nsimage/goforwardtemplatename.md)
  A “go forward” template image.
- [class let goLeftTemplateName: String](nsimage/golefttemplatename.md)
  A “go back” template image.
- [class let goRightTemplateName: String](nsimage/gorighttemplatename.md)
  A “go forward” template image.
- [class let homeTemplateName: String](nsimage/hometemplatename.md)
  Home image suitable for a template.
- [class let iChatTheaterTemplateName: String](nsimage/ichattheatertemplatename.md)
  An iChat Theater template image.
- [class let iconViewTemplateName: String](nsimage/iconviewtemplatename.md)
  An icon view mode template image.
- [class let infoName: String](nsimage/infoname.md)
  An information toolbar icon.
- [class let invalidDataFreestandingTemplateName: String](nsimage/invaliddatafreestandingtemplatename.md)
  A template image used to denote invalid data.
- [class let leftFacingTriangleTemplateName: String](nsimage/leftfacingtriangletemplatename.md)
  A generic left-facing triangle template image.
- [class let listViewTemplateName: String](nsimage/listviewtemplatename.md)
  A list view mode template image.
- [class let lockLockedTemplateName: String](nsimage/locklockedtemplatename.md)
  A locked padlock template image.
- [class let lockUnlockedTemplateName: String](nsimage/lockunlockedtemplatename.md)
  An unlocked padlock template image.
- [class let menuMixedStateTemplateName: String](nsimage/menumixedstatetemplatename.md)
  A horizontal dash, for use in menus.
- [class let menuOnStateTemplateName: String](nsimage/menuonstatetemplatename.md)
  A check mark template image, for use in menus.
- [class let mobileMeName: String](nsimage/mobilemename.md)
  A MobileMe icon.
- [class let multipleDocumentsName: String](nsimage/multipledocumentsname.md)
  A drag image for multiple items.
- [class let networkName: String](nsimage/networkname.md)
  A network icon.
- [class let pathTemplateName: String](nsimage/pathtemplatename.md)
  A path button template image.
- [class let preferencesGeneralName: String](nsimage/preferencesgeneralname.md)
  General preferences toolbar icon for the preferences window.
- [class let quickLookTemplateName: String](nsimage/quicklooktemplatename.md)
  A Quick Look template image.
- [class let refreshFreestandingTemplateName: String](nsimage/refreshfreestandingtemplatename.md)
  A refresh template image.
- [class let refreshTemplateName: String](nsimage/refreshtemplatename.md)
  A refresh template image.
- [class let removeTemplateName: String](nsimage/removetemplatename.md)
  A remove item template image.
- [class let revealFreestandingTemplateName: String](nsimage/revealfreestandingtemplatename.md)
  A reveal contents template image.
- [class let rightFacingTriangleTemplateName: String](nsimage/rightfacingtriangletemplatename.md)
  A generic right-facing triangle template image.
- [class let shareTemplateName: String](nsimage/sharetemplatename.md)
  A share view template image.
- [class let slideshowTemplateName: String](nsimage/slideshowtemplatename.md)
  A slideshow template image.
- [class let smartBadgeTemplateName: String](nsimage/smartbadgetemplatename.md)
  A badge for a “smart” item.
- [class let statusAvailableName: String](nsimage/statusavailablename.md)
  Small green indicator, similar to iChat’s available image.
- [class let statusNoneName: String](nsimage/statusnonename.md)
  Small clear indicator.
- [class let statusPartiallyAvailableName: String](nsimage/statuspartiallyavailablename.md)
  Small yellow indicator, similar to iChat’s idle image.
- [class let statusUnavailableName: String](nsimage/statusunavailablename.md)
  Small red indicator, similar to iChat’s unavailable image.
- [class let stopProgressFreestandingTemplateName: String](nsimage/stopprogressfreestandingtemplatename.md)
  A stop progress template image.
- [class let stopProgressTemplateName: String](nsimage/stopprogresstemplatename.md)
  A stop progress button template image.
- [class let touchBarAddDetailTemplateName: String](nsimage/touchbaradddetailtemplatename.md)
  A template image for showing additional detail for an item.
- [class let touchBarAddTemplateName: String](nsimage/touchbaraddtemplatename.md)
  A template image for creating a new item.
- [class let touchBarAlarmTemplateName: String](nsimage/touchbaralarmtemplatename.md)
  A template image for setting or showing an alarm.
- [class let touchBarAudioInputMuteTemplateName: String](nsimage/touchbaraudioinputmutetemplatename.md)
  A template image for muting audio input or denoting that audio input is muted.
- [class let touchBarAudioInputTemplateName: String](nsimage/touchbaraudioinputtemplatename.md)
  A template image for denoting audio input.
- [class let touchBarAudioOutputMuteTemplateName: String](nsimage/touchbaraudiooutputmutetemplatename.md)
  A template image for muting audio output or for denoting that audio output is muted.
- [class let touchBarAudioOutputVolumeHighTemplateName: String](nsimage/touchbaraudiooutputvolumehightemplatename.md)
  A template image for setting the audio output volume to a high level, or for denoting that the audio is at the peak volume.
- [class let touchBarAudioOutputVolumeLowTemplateName: String](nsimage/touchbaraudiooutputvolumelowtemplatename.md)
  A template image for setting the audio output volume to a low level, or for denoting that it is set to a low level.
- [class let touchBarAudioOutputVolumeMediumTemplateName: String](nsimage/touchbaraudiooutputvolumemediumtemplatename.md)
  A template image for setting the audio output volume to a medium level, or for denoting that it is set to a medium level.
- [class let touchBarAudioOutputVolumeOffTemplateName: String](nsimage/touchbaraudiooutputvolumeofftemplatename.md)
  A template image for setting the audio output volume to silent, or for denoting that it is set to silent.
- [class let touchBarBookmarksTemplateName: String](nsimage/touchbarbookmarkstemplatename.md)
  A template image for showing app-specific bookmarks.
- [class let touchBarColorPickerFillName: String](nsimage/touchbarcolorpickerfillname.md)
  A template image for showing a color picker so the user can select a fill color.
- [class let touchBarColorPickerFontName: String](nsimage/touchbarcolorpickerfontname.md)
  A template image for showing a color picker so the user can select a text color.
- [class let touchBarColorPickerStrokeName: String](nsimage/touchbarcolorpickerstrokename.md)
  A template image for showing a color picker so the user can select a stroke color.
- [class let touchBarCommunicationAudioTemplateName: String](nsimage/touchbarcommunicationaudiotemplatename.md)
  A template image for initiating or denoting audio communication.
- [class let touchBarCommunicationVideoTemplateName: String](nsimage/touchbarcommunicationvideotemplatename.md)
  A template image for initiating or denoting video communication.
- [class let touchBarComposeTemplateName: String](nsimage/touchbarcomposetemplatename.md)
  A template image for opening a new document or view in edit mode.
- [class let touchBarDeleteTemplateName: String](nsimage/touchbardeletetemplatename.md)
  A template image for deleting the current or selected item.
- [class let touchBarDownloadTemplateName: String](nsimage/touchbardownloadtemplatename.md)
  A template image for downloading an item.
- [class let touchBarEnterFullScreenTemplateName: String](nsimage/touchbarenterfullscreentemplatename.md)
  A template image for entering full screen mode.
- [class let touchBarExitFullScreenTemplateName: String](nsimage/touchbarexitfullscreentemplatename.md)
  A template image for exiting full screen mode.
- [class let touchBarFastForwardTemplateName: String](nsimage/touchbarfastforwardtemplatename.md)
  A template image for moving forward through media playback or slides.
- [class let touchBarFolderCopyToTemplateName: String](nsimage/touchbarfoldercopytotemplatename.md)
  A template image for copying an item to a destination.
- [class let touchBarFolderMoveToTemplateName: String](nsimage/touchbarfoldermovetotemplatename.md)
  A template image for moving an item to a destination.
- [class let touchBarFolderTemplateName: String](nsimage/touchbarfoldertemplatename.md)
  A template image for opening or representing a folder.
- [class let touchBarGetInfoTemplateName: String](nsimage/touchbargetinfotemplatename.md)
  A template image for showing information about an item.
- [class let touchBarGoBackTemplateName: String](nsimage/touchbargobacktemplatename.md)
  A template image for returning to the previous screen or location.
- [class let touchBarGoDownTemplateName: String](nsimage/touchbargodowntemplatename.md)
  A template image for moving to the next item in a list.
- [class let touchBarGoForwardTemplateName: String](nsimage/touchbargoforwardtemplatename.md)
  A template image for moving to the next screen or location.
- [class let touchBarGoUpTemplateName: String](nsimage/touchbargouptemplatename.md)
  A template image for moving to the previous item in a list.
- [class let touchBarHistoryTemplateName: String](nsimage/touchbarhistorytemplatename.md)
  A template image for showing history information, such as recent downloads.
- [class let touchBarIconViewTemplateName: String](nsimage/touchbariconviewtemplatename.md)
  A template image for showing items in an icon view.
- [class let touchBarListViewTemplateName: String](nsimage/touchbarlistviewtemplatename.md)
  A template image for showing items in a list view.
- [class let touchBarMailTemplateName: String](nsimage/touchbarmailtemplatename.md)
  A template image for creating an email message.
- [class let touchBarNewFolderTemplateName: String](nsimage/touchbarnewfoldertemplatename.md)
  A template image for creating a new folder.
- [class let touchBarNewMessageTemplateName: String](nsimage/touchbarnewmessagetemplatename.md)
  A template image for creating a new message, or for denoting the use of messaging.
- [class let touchBarOpenInBrowserTemplateName: String](nsimage/touchbaropeninbrowsertemplatename.md)
  A template image for opening an item in the user’s browser.
- [class let touchBarPauseTemplateName: String](nsimage/touchbarpausetemplatename.md)
  A template image for pausing media playback or slides.
- [class let touchBarPlayPauseTemplateName: String](nsimage/touchbarplaypausetemplatename.md)
  A template image for toggling between playing and pausing media or slides.
- [class let touchBarPlayTemplateName: String](nsimage/touchbarplaytemplatename.md)
  A template image for starting or resuming playback of media or slides.
- [class let touchBarPlayheadTemplateName: String](nsimage/touchbarplayheadtemplatename.md)
  A template image for denoting the current playback position within a timeline track.
- [class let touchBarQuickLookTemplateName: String](nsimage/touchbarquicklooktemplatename.md)
  A template image for opening an item in Quick Look.
- [class let touchBarRecordStartTemplateName: String](nsimage/touchbarrecordstarttemplatename.md)
  A template image for starting recording.
- [class let touchBarRecordStopTemplateName: String](nsimage/touchbarrecordstoptemplatename.md)
  A template image for stopping recording or stopping playback of media or slides.
- [class let touchBarRefreshTemplateName: String](nsimage/touchbarrefreshtemplatename.md)
  A template image for refreshing displayed data.
- [class let touchBarRemoveTemplateName: String](nsimage/touchbarremovetemplatename.md)
  A template image for removing an item.
- [class let touchBarRewindTemplateName: String](nsimage/touchbarrewindtemplatename.md)
  A template image for moving backwards through media or slides.
- [class let touchBarRotateLeftTemplateName: String](nsimage/touchbarrotatelefttemplatename.md)
  A template image for rotating an item counterclockwise.
- [class let touchBarRotateRightTemplateName: String](nsimage/touchbarrotaterighttemplatename.md)
  A template image for rotating an item clockwise.
- [class let touchBarSearchTemplateName: String](nsimage/touchbarsearchtemplatename.md)
  A template image for showing a search field or for initiating a search.
- [class let touchBarShareTemplateName: String](nsimage/touchbarsharetemplatename.md)
  A template image for sharing content with others directly or via social media.
- [class let touchBarSidebarTemplateName: String](nsimage/touchbarsidebartemplatename.md)
  A template image for showing a sidebar in the current view.
- [class let touchBarSkipAhead15SecondsTemplateName: String](nsimage/touchbarskipahead15secondstemplatename.md)
  A template image for skipping ahead 15 seconds during media playback.
- [class let touchBarSkipAhead30SecondsTemplateName: String](nsimage/touchbarskipahead30secondstemplatename.md)
  A template image for skipping ahead 30 seconds during media playback.
- [class let touchBarSkipAheadTemplateName: String](nsimage/touchbarskipaheadtemplatename.md)
  A template image for skipping to the next chapter or location during media playback.
- [class let touchBarSkipBack15SecondsTemplateName: String](nsimage/touchbarskipback15secondstemplatename.md)
  A template image for skipping back 15 seconds during media playback.
- [class let touchBarSkipBack30SecondsTemplateName: String](nsimage/touchbarskipback30secondstemplatename.md)
  A template image for skipping back 30 seconds during media playback.
- [class let touchBarSkipBackTemplateName: String](nsimage/touchbarskipbacktemplatename.md)
  A template image for skipping to the previous chapter or location during media playback.
- [class let touchBarSkipToEndTemplateName: String](nsimage/touchbarskiptoendtemplatename.md)
  A template image for skipping to the end of media playback.
- [class let touchBarSkipToStartTemplateName: String](nsimage/touchbarskiptostarttemplatename.md)
  A template image for skipping to the start of media playback.
- [class let touchBarSlideshowTemplateName: String](nsimage/touchbarslideshowtemplatename.md)
  A template image for starting a slideshow.
- [class let touchBarTagIconTemplateName: String](nsimage/touchbartagicontemplatename.md)
  A template image for applying a tag to an item.
- [class let touchBarTextBoldTemplateName: String](nsimage/touchbartextboldtemplatename.md)
  A template image for making selected text bold.
- [class let touchBarTextBoxTemplateName: String](nsimage/touchbartextboxtemplatename.md)
  A template image for inserting a text box.
- [class let touchBarTextCenterAlignTemplateName: String](nsimage/touchbartextcenteraligntemplatename.md)
  A template image for centering text.
- [class let touchBarTextItalicTemplateName: String](nsimage/touchbartextitalictemplatename.md)
  A template image for italicizing the selected text.
- [class let touchBarTextJustifiedAlignTemplateName: String](nsimage/touchbartextjustifiedaligntemplatename.md)
  A template image for fully justifying text.
- [class let touchBarTextLeftAlignTemplateName: String](nsimage/touchbartextleftaligntemplatename.md)
  A template image for aligning text to the left.
- [class let touchBarTextListTemplateName: String](nsimage/touchbartextlisttemplatename.md)
  A template image for inserting a list or converting text to list form.
- [class let touchBarTextRightAlignTemplateName: String](nsimage/touchbartextrightaligntemplatename.md)
  A template image for aligning text to the right.
- [class let touchBarTextStrikethroughTemplateName: String](nsimage/touchbartextstrikethroughtemplatename.md)
  A template image for striking through text.
- [class let touchBarTextUnderlineTemplateName: String](nsimage/touchbartextunderlinetemplatename.md)
  A template image for underlining text.
- [class let touchBarUserAddTemplateName: String](nsimage/touchbaruseraddtemplatename.md)
  A template image for creating a new user account.
- [class let touchBarUserGroupTemplateName: String](nsimage/touchbarusergrouptemplatename.md)
  A template image for showing or representing a group of users.
- [class let touchBarUserTemplateName: String](nsimage/touchbarusertemplatename.md)
  A template image for showing or representing user information.
- [class let touchBarVolumeDownTemplateName: String](nsimage/touchbarvolumedowntemplatename.md)
  A template image for reducing the audio output volume.
- [class let touchBarVolumeUpTemplateName: String](nsimage/touchbarvolumeuptemplatename.md)
  A template image for increasing the audio output volume.
- [class let trashEmptyName: String](nsimage/trashemptyname.md)
  An image of the empty trash can.
- [class let trashFullName: String](nsimage/trashfullname.md)
  An image of the full trash can.
- [class let userName: String](nsimage/username.md)
  Permissions for a single user.
- [class let userAccountsName: String](nsimage/useraccountsname.md)
  User account toolbar icon for the preferences window.
- [class let userGroupName: String](nsimage/usergroupname.md)
  Permissions for a group of users.
- [class let userGuestName: String](nsimage/userguestname.md)
  Permissions for guests.

## See Also

- [Configuring and displaying symbol images in your UI](../UIKit/configuring-and-displaying-symbol-images-in-your-ui.md)
  Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [init?(named: NSImage.Name)](nsimage/init(named:).md)
  Returns the image object associated with the specified name.
- [convenience init?(systemSymbolName: String, accessibilityDescription: String?)](nsimage/init(systemsymbolname:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and accessibility description you specify.
- [convenience init?(systemSymbolName: String, variableValue: Double, accessibilityDescription: String?)](nsimage/init(systemsymbolname:variablevalue:accessibilitydescription:).md)
  Creates a symbol image with the system symbol name and variable value you specify.
- [convenience init?(symbolName: String, variableValue: Double)](nsimage/init(symbolname:variablevalue:).md)
  Creates a symbol image with the symbol name and variable value you specify.
- [convenience init?(symbolName: String, bundle: Bundle?, variableValue: Double)](nsimage/init(symbolname:bundle:variablevalue:).md)
- [convenience init(resource: ImageResource)](nsimage/init(resource:).md)
- [func setName(NSImage.Name?) -> Bool](nsimage/setname(_:).md)
  Registers the image object under the specified name.
- [func name() -> NSImage.Name?](nsimage/name.md)
  Returns the name associated with the image, if any.
- [convenience init(imageLiteralResourceName: String)](nsimage/init(imageliteralresourcename:).md)
  Creates an image initialized with the specified resource name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/name-swift.typealias)*