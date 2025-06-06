# Core Graphics Constants

**Framework**: Core Graphics

## Topics

### Constants
- [class let colorSpace: CFString](cgdisplaystream/colorspace.md)
  This key specifies the color space of the output buffer. If this key is not included in the dictionary, the output buffer uses the same color space as the display. The value associated with this key must be a [`CGColorSpace`](cgcolorspace.md) for the desired color space.
- [class let conversionBlackPointCompensation: CFString](cgcolor/conversionblackpointcompensation.md)
  An option for whether to apply black point compensation when converting between color profiles.
- [var kCGDisplayBitsPerPixel: String](kcgdisplaybitsperpixel.md)
  Specifies a CFNumber integer value that represents the number of bits in a pixel.
- [var kCGDisplayBitsPerSample: String](kcgdisplaybitspersample.md)
  Specifies a CFNumber integer value that represents the number of bits in an individual sample (for example, a color value in an RGB pixel).
- [var kCGDisplayBlendNormal: Double](kcgdisplayblendnormal.md)
  The blend color is not applied at the start or end of a fade operation.
- [var kCGDisplayBlendSolidColor: Double](kcgdisplayblendsolidcolor.md)
  The user sees only the blend color at the start or end of a fade operation.
- [var kCGDisplayBytesPerRow: String](kcgdisplaybytesperrow.md)
  Specifies a CFNumber integer value that represents the number of bytes in a row on the display.
- [var kCGDisplayFadeReservationInvalidToken: Int32](kcgdisplayfadereservationinvalidtoken.md)
- [var kCGDisplayHeight: String](kcgdisplayheight.md)
  Specifies a CFNumber integer value that represents the height of the display in pixels.
- [var kCGDisplayIOFlags: String](kcgdisplayioflags.md)
  Specifies a CFNumber integer value that contains the I/O Kit display mode flags. For more information, see the header file `IOKit/IOGraphicsTypes.h`.
- [var kCGDisplayMode: String](kcgdisplaymode.md)
  Specifies a `CFNumber` integer value that represents the I/O Kit display mode number.
- [var kCGDisplayModeIsInterlaced: String](kcgdisplaymodeisinterlaced.md)
  Specifies a CFBoolean value indicating that the I/O Kit interlace mode flag is set.
- [var kCGDisplayModeIsSafeForHardware: String](kcgdisplaymodeissafeforhardware.md)
  Specifies a CFBoolean value indicating that the display mode doesn’t need a confirmation dialog to be set.
- [var kCGDisplayModeIsStretched: String](kcgdisplaymodeisstretched.md)
  Specifies a CFBoolean value indicating that the I/O Kit stretched mode flag is set.
- [var kCGDisplayModeIsTelevisionOutput: String](kcgdisplaymodeistelevisionoutput.md)
  Specifies a CFBoolean value indicating that the I/O Kit television output mode flag is set.
- [var kCGDisplayModeUsableForDesktopGUI: String](kcgdisplaymodeusablefordesktopgui.md)
  Specifies a CFBoolean value that indicates whether the display is suitable for use with the macOS graphical user interface. The criteria include factors such as sufficient width and height and adequate pixel depth.
- [var kCGDisplayRefreshRate: String](kcgdisplayrefreshrate.md)
  Specifies a `CFNumber` double-precision floating point value that represents the refresh rate of a CRT display.
- [var kCGDisplaySamplesPerPixel: String](kcgdisplaysamplesperpixel.md)
  Specifies a CFNumber integer value that represents the number of samples in a pixel.
- [let kCGDisplayShowDuplicateLowResolutionModes: CFString](kcgdisplayshowduplicatelowresolutionmodes.md)
- [class let destinationRect: CFString](cgdisplaystream/destinationrect.md)
  This key specifies that the display stream outputs the frame data into a subset of the output `IOSurface` object.
- [class let minimumFrameTime: CFString](cgdisplaystream/minimumframetime.md)
  This key specifies the desired minimum time between frame updates, allowing you to throttle the rate at which updates are received. If this key is not included in the dictionary, the default value is `0`, meaning that updates are not throttled. The value must be specified as a `CFNumber`.
- [class let queueDepth: CFString](cgdisplaystream/queuedepth.md)
  This key specifies the number of frames to keep in the queue. If this key is not included in the dictionary, the default value is `3` frames. Specifying more frames uses more memory, but may allow you to process frame data without stalling the display stream. The value associated with this key should be specified as a `CFNumber`, and should not exceed `8` frames.
- [class let showCursor: CFString](cgdisplaystream/showcursor.md)
  This key specifies whether the cursor should appear in the stream. If this key is not included in the dictionary, the cursor is visible. The value must be specified as a `CFBoolean`.
- [class let sourceRect: CFString](cgdisplaystream/sourcerect.md)
  This key specifies that the display stream only samples a subset of the display’s framebuffer.
- [class let yCbCrMatrix: CFString](cgdisplaystream/ycbcrmatrix.md)
  This key should only be included if you the display stream is creating output frames in either the 420v or 420f formats. It is used to specify the YCbCr matrix applied to the output surface.
- [class let yCbCrMatrix_ITU_R_601_4: CFString](cgdisplaystream/ycbcrmatrix_itu_r_601_4.md)
  Specifies the YCbCr to RGB conversion matrix for standard digital television (ITU R 601) images.
- [class let yCbCrMatrix_ITU_R_709_2: CFString](cgdisplaystream/ycbcrmatrix_itu_r_709_2.md)
  Specifies the YCbCr to RGB conversion matrix for HDTV digital television (ITU R 709) images.
- [class let yCbCrMatrix_SMPTE_240M_1995: CFString](cgdisplaystream/ycbcrmatrix_smpte_240m_1995.md)
  Specifies the YCbCR to RGB conversion matrix for 1920 x 1135 HDTV (SMPTE 240M 1995).
- [var kCGDisplayWidth: String](kcgdisplaywidth.md)
  Specifies a CFNumber integer value that represents the width of the display in pixels.
- [let kCGFontIndexInvalid: CGFontIndex](kcgfontindexinvalid.md)
  An invalid font index (a value which never represents a valid glyph).
- [let kCGFontIndexMax: CGFontIndex](kcgfontindexmax.md)
  The maximum allowed value of a [`CGFontIndex`](cgfontindex.md).
- [let kCGGlyphMax: CGFontIndex](kcgglyphmax.md)
  The maximum allowed value of a [`CGGlyph`](cgglyph.md).
- [var kCGIODisplayModeID: String](kcgiodisplaymodeid.md)
- [var kCGMouseDownEventMaskingDeadSwitchTimeout: Double](kcgmousedowneventmaskingdeadswitchtimeout.md)
- [var kCGNotifyEventTapAdded: String](kcgnotifyeventtapadded.md)
- [var kCGNotifyEventTapRemoved: String](kcgnotifyeventtapremoved.md)
- [var kCGNotifyGUIConsoleSessionChanged: String](kcgnotifyguiconsolesessionchanged.md)
- [var kCGNotifyGUISessionUserChanged: String](kcgnotifyguisessionuserchanged.md)
- [var kCGNumReservedWindowLevels: Int32](kcgnumreservedwindowlevels.md)
- [var kCGSessionConsoleSetKey: String](kcgsessionconsolesetkey.md)
  A `CFNumber` 32-bit unsigned integer value that represents a set of hardware composing a console.
- [var kCGSessionLoginDoneKey: String](kcgsessionlogindonekey.md)
  A `CFBoolean` value indicating whether the login operation has been done.
- [var kCGSessionOnConsoleKey: String](kcgsessiononconsolekey.md)
  A `CFBoolean` value indicating whether the session is on a console.
- [var kCGSessionUserIDKey: String](kcgsessionuseridkey.md)
  A `CFNumber` 32-bit unsigned integer value that encodes a user ID for the session’s current user.
- [var kCGSessionUserNameKey: String](kcgsessionusernamekey.md)
  A `CFString` value that encodes the session’s short user name as set by the login operation.
- [let kCGWindowAlpha: CFString](kcgwindowalpha.md)
- [let kCGWindowBackingLocationVideoMemory: CFString](kcgwindowbackinglocationvideomemory.md)
- [let kCGWindowBounds: CFString](kcgwindowbounds.md)
- [let kCGWindowIsOnscreen: CFString](kcgwindowisonscreen.md)
- [let kCGWindowLayer: CFString](kcgwindowlayer.md)
- [let kCGWindowMemoryUsage: CFString](kcgwindowmemoryusage.md)
- [let kCGWindowName: CFString](kcgwindowname.md)
- [let kCGWindowNumber: CFString](kcgwindownumber.md)
- [let kCGWindowOwnerName: CFString](kcgwindowownername.md)
- [let kCGWindowOwnerPID: CFString](kcgwindowownerpid.md)
- [let kCGWindowSharingState: CFString](kcgwindowsharingstate.md)
- [let kCGWindowStoreType: CFString](kcgwindowstoretype.md)
- [let CGPointZero: CGPoint](cgpointzero.md)
  A point constant with location `(0,0)`. The zero point is equivalent to `CGPointMake(0,0)`.
- [let CGRectZero: CGRect](cgrectzero.md)
  A rectangle constant with location `(0,0)`, and width and height of 0. The zero rectangle is equivalent to `CGRectMake(0,0,0,0)`.
- [let CGSizeZero: CGSize](cgsizezero.md)
  A size constant with width and height of `0`. The zero size is equivalent to `CGSizeMake(0,0)`.
- [let kCGWindowWorkspace: CFString](kcgwindowworkspace.md)
- [class let preserveAspectRatio: CFString](cgdisplaystream/preserveaspectratio.md)
  This key specifies whether the display stream preserves the aspect ratio of the source pixel data. If this key is not included in the dictionary, then the aspect ratio is preserved. If the aspect ratio is preserved, then the display stream adds black bars to the output data. If the aspect ratio is not preserved, then the pixel data is stretched to fit the output buffer’s dimensions. The value associated with the key must be a `CFBoolean`.
- [var CG_HDR_BT_2100: Int32](cg_hdr_bt_2100.md)
- [let kCGBitmapByteOrder16Host: CGBitmapInfo](kcgbitmapbyteorder16host.md)
  16-bit, host endian format.
- [let kCGBitmapByteOrder32Host: CGBitmapInfo](kcgbitmapbyteorder32host.md)
  32-bit, host endian format.
- [let kCGColorSpaceExtendedRange: CFString](kcgcolorspaceextendedrange.md)
- [var kCGDefaultHDRImageContentHeadroom: Float](kcgdefaulthdrimagecontentheadroom.md)
- [let kCGEXRToneMappingGammaDefog: CFString](kcgexrtonemappinggammadefog.md)
- [let kCGEXRToneMappingGammaExposure: CFString](kcgexrtonemappinggammaexposure.md)
- [let kCGEXRToneMappingGammaKneeHigh: CFString](kcgexrtonemappinggammakneehigh.md)
- [let kCGEXRToneMappingGammaKneeLow: CFString](kcgexrtonemappinggammakneelow.md)
- [var kCGNullDirectDisplay: CGDirectDisplayID](kcgnulldirectdisplay.md)
  A value that will never correspond to actual hardware.
- [var kCGNullWindowID: CGWindowID](kcgnullwindowid.md)
- [var kCGNumReservedBaseWindowLevels: Int32](kcgnumreservedbasewindowlevels.md)
- [let kCGPDFContextAccessPermissions: CFString](kcgpdfcontextaccesspermissions.md)
- [let kCGPDFContextCreateLinearizedPDF: CFString](kcgpdfcontextcreatelinearizedpdf.md)
- [let kCGPDFContextCreatePDFA: CFString](kcgpdfcontextcreatepdfa.md)
- [let kCGPDFOutlineChildren: CFString](kcgpdfoutlinechildren.md)
- [let kCGPDFOutlineDestination: CFString](kcgpdfoutlinedestination.md)
- [let kCGPDFOutlineDestinationRect: CFString](kcgpdfoutlinedestinationrect.md)
- [let kCGPDFOutlineTitle: CFString](kcgpdfoutlinetitle.md)
- [let kCGSkipBoostToHDR: CFString](kcgskipboosttohdr.md)
- [let kCGUse100nitsHLGOOTF: CFString](kcguse100nitshlgootf.md)
- [let kCGUseBT1886ForCoreVideoGamma: CFString](kcgusebt1886forcorevideogamma.md)
- [let kCGUseLegacyHDREcosystem: CFString](kcguselegacyhdrecosystem.md)
- [var kCGAssistiveTechHighWindowLevel: CGWindowLevel](kcgassistivetechhighwindowlevel.md)
- [var kCGBackstopMenuLevel: CGWindowLevel](kcgbackstopmenulevel.md)
- [var kCGDockWindowLevel: CGWindowLevel](kcgdockwindowlevel.md)
- [var kCGDraggingWindowLevel: CGWindowLevel](kcgdraggingwindowlevel.md)
- [var kCGFloatingWindowLevel: CGWindowLevel](kcgfloatingwindowlevel.md)
- [var kCGHelpWindowLevel: CGWindowLevel](kcghelpwindowlevel.md)
- [var kCGMainMenuWindowLevel: CGWindowLevel](kcgmainmenuwindowlevel.md)
- [var kCGModalPanelWindowLevel: CGWindowLevel](kcgmodalpanelwindowlevel.md)
- [var kCGNormalWindowLevel: CGWindowLevel](kcgnormalwindowlevel.md)
- [var kCGOverlayWindowLevel: CGWindowLevel](kcgoverlaywindowlevel.md)
- [var kCGPopUpMenuWindowLevel: CGWindowLevel](kcgpopupmenuwindowlevel.md)
- [var kCGScreenSaverWindowLevel: CGWindowLevel](kcgscreensaverwindowlevel.md)
- [var kCGStatusWindowLevel: CGWindowLevel](kcgstatuswindowlevel.md)
- [var kCGTornOffMenuWindowLevel: CGWindowLevel](kcgtornoffmenuwindowlevel.md)
- [var kCGUtilityWindowLevel: CGWindowLevel](kcgutilitywindowlevel.md)

## See Also

- [Core Graphics Structures](core-graphics-structures.md)
- [Core Graphics Enumerations](core-graphics-enumerations.md)
- [Core Graphics Functions](core-graphics-functions.md)
- [Core Graphics Data Types](core-graphics-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/core-graphics-constants)*