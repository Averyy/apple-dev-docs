# Quartz Display Services

**Framework**: Core Graphics

Provides direct access to features in the macOS window server for configuring and controlling display hardware.

#### Overview

You can use Quartz Display Services to:

- Examine and change display mode properties such as width, height, and pixel depth
- Configure a set of displays in a single operation
- Capture one or more displays for exclusive use
- Stream the contents of a display
- Perform fade effects
- Activate display mirroring
- Configure gamma color correction tables
- Receive notification of screen update operations

## Topics

### Finding Displays
- [func CGMainDisplayID() -> CGDirectDisplayID](cgmaindisplayid().md)
  Returns the display ID of the main display.
- [func CGGetOnlineDisplayList(UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetonlinedisplaylist(_:_:_:).md)
  Provides a list of displays that are online (active, mirrored, or sleeping).
- [func CGGetActiveDisplayList(UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetactivedisplaylist(_:_:_:).md)
  Provides a list of displays that are active for drawing.
- [func CGGetDisplaysWithOpenGLDisplayMask(CGOpenGLDisplayMask, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetdisplayswithopengldisplaymask(_:_:_:_:).md)
  Provides a list of displays that corresponds to the bits set in an OpenGL display mask.
- [func CGGetDisplaysWithPoint(CGPoint, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetdisplayswithpoint(_:_:_:_:).md)
  Provides a list of online displays with bounds that include the specified point.
- [func CGGetDisplaysWithRect(CGRect, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetdisplayswithrect(_:_:_:_:).md)
  Gets a list of online displays with bounds that intersect the specified rectangle.
- [func CGOpenGLDisplayMaskToDisplayID(CGOpenGLDisplayMask) -> CGDirectDisplayID](cgopengldisplaymasktodisplayid(_:).md)
  Maps an OpenGL display mask to a display ID.
- [func CGDisplayIDToOpenGLDisplayMask(CGDirectDisplayID) -> CGOpenGLDisplayMask](cgdisplayidtoopengldisplaymask(_:).md)
  Maps a display ID to an OpenGL display mask.
### Capturing and Releasing Displays
- [func CGDisplayCapture(CGDirectDisplayID) -> CGError](cgdisplaycapture(_:).md)
  Obtains exclusive use of a display, preventing other applications and system services from using the display or changing its configuration.
- [func CGDisplayCaptureWithOptions(CGDirectDisplayID, CGCaptureOptions) -> CGError](cgdisplaycapturewithoptions(_:_:).md)
  Obtains exclusive use of a display for an application using the options you specify.
- [func CGDisplayRelease(CGDirectDisplayID) -> CGError](cgdisplayrelease(_:).md)
  Releases a captured display.
- [func CGDisplayIsCaptured(CGDirectDisplayID) -> boolean_t](cgdisplayiscaptured(_:).md)
  Returns a Boolean value indicating whether a display is captured.
- [func CGCaptureAllDisplays() -> CGError](cgcapturealldisplays().md)
  Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [func CGCaptureAllDisplaysWithOptions(CGCaptureOptions) -> CGError](cgcapturealldisplayswithoptions(_:).md)
  Captures all attached displays, using the specified options.
- [func CGReleaseAllDisplays() -> CGError](cgreleasealldisplays().md)
  Releases all captured displays.
- [func CGShieldingWindowID(CGDirectDisplayID) -> CGWindowID](cgshieldingwindowid(_:).md)
  Returns the window ID of the shield window for a captured display.
- [func CGShieldingWindowLevel() -> CGWindowLevel](cgshieldingwindowlevel().md)
  Returns the window level of the shield window for a captured display.
- [func CGDisplayGetDrawingContext(CGDirectDisplayID) -> CGContext?](cgdisplaygetdrawingcontext(_:).md)
  Returns a graphics context suitable for drawing to a captured display.
### Creating Images from the Display
- [func CGDisplayCreateImage(CGDirectDisplayID) -> CGImage?](cgdisplaycreateimage(_:).md)
  Returns an image containing the contents of the specified display.
- [func CGDisplayCreateImage(CGDirectDisplayID, rect: CGRect) -> CGImage?](cgdisplaycreateimage(_:rect:).md)
  Returns an image containing the contents of a portion of the specified display.
### Configuring Displays
- [func CGBeginDisplayConfiguration(UnsafeMutablePointer<CGDisplayConfigRef?>?) -> CGError](cgbegindisplayconfiguration(_:).md)
  Begins a new set of display configuration changes.
- [func CGCancelDisplayConfiguration(CGDisplayConfigRef?) -> CGError](cgcanceldisplayconfiguration(_:).md)
  Cancels a set of display configuration changes.
- [func CGCompleteDisplayConfiguration(CGDisplayConfigRef?, CGConfigureOption) -> CGError](cgcompletedisplayconfiguration(_:_:).md)
  Completes a set of display configuration changes.
- [func CGConfigureDisplayMirrorOfDisplay(CGDisplayConfigRef?, CGDirectDisplayID, CGDirectDisplayID) -> CGError](cgconfiguredisplaymirrorofdisplay(_:_:_:).md)
  Changes the configuration of a mirroring set.
- [func CGConfigureDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CFDictionary?) -> CGError](cgconfiguredisplaymode(_:_:_:).md)
  Configures the display mode of a display.
- [func CGConfigureDisplayOrigin(CGDisplayConfigRef?, CGDirectDisplayID, Int32, Int32) -> CGError](cgconfiguredisplayorigin(_:_:_:_:).md)
  Configures the origin of a display relative to the global display coordinate space.
- [func CGRestorePermanentDisplayConfiguration()](cgrestorepermanentdisplayconfiguration().md)
  Restores the permanent display configuration settings for the current user.
- [func CGConfigureDisplayStereoOperation(CGDisplayConfigRef?, CGDirectDisplayID, boolean_t, boolean_t) -> CGError](cgconfiguredisplaystereooperation(_:_:_:_:).md)
  Enables or disables stereo operation for a display, as part of a display configuration.
- [func CGDisplaySetStereoOperation(CGDirectDisplayID, boolean_t, boolean_t, CGConfigureOption) -> CGError](cgdisplaysetstereooperation(_:_:_:_:).md)
  Immediately enables or disables stereo operation for a display.
- [func CGConfigureDisplayWithDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](cgconfiguredisplaywithdisplaymode(_:_:_:_:).md)
  Configures the display mode of a display.
### Getting the Display Configuration
- [func CGDisplayCopyColorSpace(CGDirectDisplayID) -> CGColorSpace](cgdisplaycopycolorspace(_:).md)
  Returns the color space for a display.
- [func CGDisplayIOServicePort(CGDirectDisplayID) -> io_service_t](cgdisplayioserviceport(_:).md)
  Returns the I/O Kit service port of the specified display.
- [func CGDisplayIsActive(CGDirectDisplayID) -> boolean_t](cgdisplayisactive(_:).md)
  Returns a Boolean value indicating whether a display is active.
- [func CGDisplayIsAlwaysInMirrorSet(CGDirectDisplayID) -> boolean_t](cgdisplayisalwaysinmirrorset(_:).md)
  Returns a Boolean value indicating whether a display is always in a mirroring set.
- [func CGDisplayIsAsleep(CGDirectDisplayID) -> boolean_t](cgdisplayisasleep(_:).md)
  Returns a Boolean value indicating whether a display is sleeping (and is therefore not drawable).
- [func CGDisplayIsBuiltin(CGDirectDisplayID) -> boolean_t](cgdisplayisbuiltin(_:).md)
  Returns a Boolean value indicating whether a display is built-in, such as the internal display in portable systems.
- [func CGDisplayIsInHWMirrorSet(CGDirectDisplayID) -> boolean_t](cgdisplayisinhwmirrorset(_:).md)
  Returns a Boolean value indicating whether a display is in a hardware mirroring set.
- [func CGDisplayIsInMirrorSet(CGDirectDisplayID) -> boolean_t](cgdisplayisinmirrorset(_:).md)
  Returns a Boolean value indicating whether a display is in a mirroring set.
- [func CGDisplayIsMain(CGDirectDisplayID) -> boolean_t](cgdisplayismain(_:).md)
  Returns a Boolean value indicating whether a display is the main display.
- [func CGDisplayIsOnline(CGDirectDisplayID) -> boolean_t](cgdisplayisonline(_:).md)
  Returns a Boolean value indicating whether a display is connected or online.
- [func CGDisplayIsStereo(CGDirectDisplayID) -> boolean_t](cgdisplayisstereo(_:).md)
  Returns a Boolean value indicating whether a display is running in a stereo graphics mode.
- [func CGDisplayMirrorsDisplay(CGDirectDisplayID) -> CGDirectDisplayID](cgdisplaymirrorsdisplay(_:).md)
  For a secondary display in a mirroring set, returns the primary display.
- [func CGDisplayModelNumber(CGDirectDisplayID) -> UInt32](cgdisplaymodelnumber(_:).md)
  Returns the model number of a display monitor.
- [func CGDisplayPrimaryDisplay(CGDirectDisplayID) -> CGDirectDisplayID](cgdisplayprimarydisplay(_:).md)
  Returns the primary display in a hardware mirroring set.
- [func CGDisplayRotation(CGDirectDisplayID) -> Double](cgdisplayrotation(_:).md)
  Returns the rotation angle of a display in degrees.
- [func CGDisplayScreenSize(CGDirectDisplayID) -> CGSize](cgdisplayscreensize(_:).md)
  Returns the width and height of a display in millimeters.
- [func CGDisplaySerialNumber(CGDirectDisplayID) -> UInt32](cgdisplayserialnumber(_:).md)
  Returns the serial number of a display monitor.
- [func CGDisplayUnitNumber(CGDirectDisplayID) -> UInt32](cgdisplayunitnumber(_:).md)
  Returns the logical unit number of a display.
- [func CGDisplayUsesOpenGLAcceleration(CGDirectDisplayID) -> boolean_t](cgdisplayusesopenglacceleration(_:).md)
  Returns a Boolean value indicating whether Quartz is using OpenGL-based window acceleration (Quartz Extreme) to render in a display.
- [func CGDisplayVendorNumber(CGDirectDisplayID) -> UInt32](cgdisplayvendornumber(_:).md)
  Returns the vendor number of the specified display’s monitor.
### Registering for Notification of Display Configuration Changes
- [func CGDisplayRegisterReconfigurationCallback(CGDisplayReconfigurationCallBack?, UnsafeMutableRawPointer?) -> CGError](cgdisplayregisterreconfigurationcallback(_:_:).md)
  Registers a callback function to be invoked whenever a local display is reconfigured.
- [func CGDisplayRemoveReconfigurationCallback(CGDisplayReconfigurationCallBack?, UnsafeMutableRawPointer?) -> CGError](cgdisplayremovereconfigurationcallback(_:_:).md)
  Removes the registration of a callback function that’s invoked whenever a local display is reconfigured.
### Retrieving Display Parameters
- [func CGDisplayBounds(CGDirectDisplayID) -> CGRect](cgdisplaybounds(_:).md)
  Returns the bounds of a display in the global display coordinate space.
- [func CGDisplayPixelsHigh(CGDirectDisplayID) -> Int](cgdisplaypixelshigh(_:).md)
  Returns the display height in pixel units.
- [func CGDisplayPixelsWide(CGDirectDisplayID) -> Int](cgdisplaypixelswide(_:).md)
  Returns the display width in pixel units.
### Creating and Managing Display Modes
- [func CGDisplayAvailableModes(CGDirectDisplayID) -> CFArray?](cgdisplayavailablemodes(_:).md)
  Returns information about the currently available display modes.
- [func CGDisplayBestModeForParameters(CGDirectDisplayID, Int, Int, Int, UnsafeMutablePointer<boolean_t>?) -> CFDictionary?](cgdisplaybestmodeforparameters(_:_:_:_:_:).md)
  Returns information about the display mode closest to a specified depth and screen size.
- [func CGDisplayBestModeForParametersAndRefreshRate(CGDirectDisplayID, Int, Int, Int, CGRefreshRate, UnsafeMutablePointer<boolean_t>?) -> CFDictionary?](cgdisplaybestmodeforparametersandrefreshrate(_:_:_:_:_:_:).md)
  Returns information about the display mode closest to a specified depth, screen size, and refresh rate.
- [func CGDisplayCurrentMode(CGDirectDisplayID) -> CFDictionary?](cgdisplaycurrentmode(_:).md)
  Returns information about the current display mode.
- [func CGDisplaySwitchToMode(CGDirectDisplayID, CFDictionary?) -> CGError](cgdisplayswitchtomode(_:_:).md)
  Switches a display to a different mode.
- [func CGDisplayCopyDisplayMode(CGDirectDisplayID) -> CGDisplayMode?](cgdisplaycopydisplaymode(_:).md)
  Returns information about a display’s current configuration.
- [func CGDisplayCopyAllDisplayModes(CGDirectDisplayID, CFDictionary?) -> CFArray?](cgdisplaycopyalldisplaymodes(_:_:).md)
  Returns information about the currently available display modes.
- [func CGDisplaySetDisplayMode(CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](cgdisplaysetdisplaymode(_:_:_:).md)
  Switches a display to a different mode.
### Getting Information About a Display Mode
- [var width: Int](cgdisplaymode/width.md)
  Returns the width of the specified display mode.
- [var height: Int](cgdisplaymode/height.md)
  Returns the height of the specified display mode.
- [var pixelEncoding: CFString?](cgdisplaymode/pixelencoding.md)
  Returns the pixel encoding of the specified display mode.
- [var refreshRate: Double](cgdisplaymode/refreshrate.md)
  Returns the refresh rate of the specified display mode.
- [var ioFlags: UInt32](cgdisplaymode/ioflags.md)
  Returns the I/O Kit flags of the specified display mode.
- [var ioDisplayModeID: Int32](cgdisplaymode/iodisplaymodeid.md)
  Returns the I/O Kit display mode ID of the specified display mode.
- [func isUsableForDesktopGUI() -> Bool](cgdisplaymode/isusablefordesktopgui.md)
  Returns a Boolean value indicating whether the specified display mode is usable for a desktop graphical user interface.
- [class var typeID: CFTypeID](cgdisplaymode/typeid.md)
  Returns the type identifier of Quartz display modes.
### Adjusting the Display Gamma
- [func CGSetDisplayTransferByFormula(CGDirectDisplayID, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue) -> CGError](cgsetdisplaytransferbyformula(_:_:_:_:_:_:_:_:_:_:).md)
  Sets the gamma function for a display by specifying the coefficients of the gamma transfer formula.
- [func CGGetDisplayTransferByFormula(CGDirectDisplayID, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?) -> CGError](cggetdisplaytransferbyformula(_:_:_:_:_:_:_:_:_:_:).md)
  Gets the coefficients of the gamma transfer formula for a display.
- [func CGSetDisplayTransferByTable(CGDirectDisplayID, UInt32, UnsafePointer<CGGammaValue>?, UnsafePointer<CGGammaValue>?, UnsafePointer<CGGammaValue>?) -> CGError](cgsetdisplaytransferbytable(_:_:_:_:_:).md)
  Sets the color gamma function for a display by specifying the values in the RGB gamma tables.
- [func CGGetDisplayTransferByTable(CGDirectDisplayID, UInt32, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetdisplaytransferbytable(_:_:_:_:_:_:).md)
  Gets the values in the RGB gamma tables for a display.
- [func CGSetDisplayTransferByByteTable(CGDirectDisplayID, UInt32, UnsafePointer<UInt8>, UnsafePointer<UInt8>, UnsafePointer<UInt8>) -> CGError](cgsetdisplaytransferbybytetable(_:_:_:_:_:).md)
  Sets the byte values in the 8-bit RGB gamma tables for a display.
- [func CGDisplayRestoreColorSyncSettings()](cgdisplayrestorecolorsyncsettings().md)
  Restores the gamma tables to the values in the user’s ColorSync display profile.
- [func CGDisplayGammaTableCapacity(CGDirectDisplayID) -> UInt32](cgdisplaygammatablecapacity(_:).md)
  Returns the capacity, or number of entries, in the gamma table for a display.
### Display Fade Effects
- [func CGConfigureDisplayFadeEffect(CGDisplayConfigRef?, CGDisplayFadeInterval, CGDisplayFadeInterval, Float, Float, Float) -> CGError](cgconfiguredisplayfadeeffect(_:_:_:_:_:_:).md)
  Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [func CGAcquireDisplayFadeReservation(CGDisplayReservationInterval, UnsafeMutablePointer<CGDisplayFadeReservationToken>?) -> CGError](cgacquiredisplayfadereservation(_:_:).md)
  Reserves the fade hardware for a specified time interval.
- [func CGDisplayFade(CGDisplayFadeReservationToken, CGDisplayFadeInterval, CGDisplayBlendFraction, CGDisplayBlendFraction, Float, Float, Float, boolean_t) -> CGError](cgdisplayfade(_:_:_:_:_:_:_:_:).md)
  Performs a single fade operation.
- [func CGDisplayFadeOperationInProgress() -> boolean_t](cgdisplayfadeoperationinprogress().md)
  Returns a Boolean value indicating whether a fade operation is currently in progress.
- [func CGReleaseDisplayFadeReservation(CGDisplayFadeReservationToken) -> CGError](cgreleasedisplayfadereservation(_:).md)
  Releases a display fade reservation, and unfades the display if needed.
### Controlling the Mouse Cursor
- [func CGDisplayHideCursor(CGDirectDisplayID) -> CGError](cgdisplayhidecursor(_:).md)
  Hides the mouse cursor, and increments the hide cursor count.
- [func CGDisplayShowCursor(CGDirectDisplayID) -> CGError](cgdisplayshowcursor(_:).md)
  Decrements the hide cursor count, and shows the mouse cursor if the count is `0`.
- [func CGDisplayMoveCursorToPoint(CGDirectDisplayID, CGPoint) -> CGError](cgdisplaymovecursortopoint(_:_:).md)
  Moves the mouse cursor to a specified point relative to the upper-left corner of the display.
- [func CGCursorIsVisible() -> boolean_t](cgcursorisvisible().md)
  Returns a Boolean value indicating whether the mouse cursor is visible.
- [func CGCursorIsDrawnInFramebuffer() -> boolean_t](cgcursorisdrawninframebuffer().md)
  Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory.
- [func CGAssociateMouseAndMouseCursorPosition(boolean_t) -> CGError](cgassociatemouseandmousecursorposition(_:).md)
  Connects or disconnects the mouse and cursor while an application is in the foreground.
- [func CGWarpMouseCursorPosition(CGPoint) -> CGError](cgwarpmousecursorposition(_:).md)
  Moves the mouse cursor without generating events.
- [func CGGetLastMouseDelta() -> (x: Int32, y: Int32)](cggetlastmousedelta().md)
  Reports the change in mouse position since the last mouse movement event received by the application.
### Getting Window Server Information
- [func CGSessionCopyCurrentDictionary() -> CFDictionary?](cgsessioncopycurrentdictionary().md)
  Returns information about the caller’s window server session.
- [func CGWindowServerCFMachPort() -> CFMachPort?](cgwindowservercfmachport().md)
  Returns a Core Foundation Mach port (CFMachPort) that corresponds to the macOS window server.
- [func CGWindowLevelForKey(CGWindowLevelKey) -> CGWindowLevel](cgwindowlevelforkey(_:).md)
  Returns the window level that corresponds to one of the standard window types.
### Getting Information About Refresh and Move Operations
- [func CGRegisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?) -> CGError](cgregisterscreenrefreshcallback(_:_:).md)
  Registers a callback function to be invoked when local displays are refreshed or modified.
- [func CGUnregisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?)](cgunregisterscreenrefreshcallback(_:_:).md)
  Removes a previously registered callback function invoked when local displays are refreshed or modified.
- [func CGWaitForScreenRefreshRects(UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<UInt32>?) -> CGError](cgwaitforscreenrefreshrects(_:_:).md)
  Waits for screen refresh operations.
- [func CGScreenRegisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?) -> CGError](cgscreenregistermovecallback(_:_:).md)
  Registers a callback function to be invoked when an area of the display is moved.
- [func CGScreenUnregisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?)](cgscreenunregistermovecallback(_:_:).md)
  Removes a previously registered callback function invoked when an area of the display is moved.
- [func CGWaitForScreenUpdateRects(CGScreenUpdateOperation, UnsafeMutablePointer<CGScreenUpdateOperation>?, UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<CGScreenUpdateMoveDelta>?) -> CGError](cgwaitforscreenupdaterects(_:_:_:_:_:).md)
  Waits for screen update operations.
- [func CGReleaseScreenRefreshRects(UnsafeMutablePointer<CGRect>?)](cgreleasescreenrefreshrects(_:).md)
  Deallocates a list of rectangles that represent changed areas on local displays.
### Streaming the Contents of a Display
- [init?(display: CGDirectDisplayID, outputWidth: Int, outputHeight: Int, pixelFormat: Int32, properties: CFDictionary?, handler: CGDisplayStreamFrameAvailableHandler?)](cgdisplaystream/init(display:outputwidth:outputheight:pixelformat:properties:handler:).md)
  Creates a new display stream to be used with a `CFRunloop`.
- [init?(dispatchQueueDisplay: CGDirectDisplayID, outputWidth: Int, outputHeight: Int, pixelFormat: Int32, properties: CFDictionary?, queue: dispatch_queue_t, handler: CGDisplayStreamFrameAvailableHandler?)](cgdisplaystream/init(dispatchqueuedisplay:outputwidth:outputheight:pixelformat:properties:queue:handler:).md)
  Creates a new display stream whose updates are delivered to a dispatch queue.
- [func start() -> CGError](cgdisplaystream/start.md)
  Tells a stream to start sending updates.
- [func stop() -> CGError](cgdisplaystream/stop.md)
  Tells a stream to stop sending updates.
- [var runLoopSource: CFRunLoopSource?](cgdisplaystream/runloopsource.md)
  Gets the run loop source for a display stream.
- [func getRects(CGDisplayStreamUpdateRectType, rectCount: UnsafeMutablePointer<Int>) -> UnsafePointer<CGRect>?](cgdisplaystreamupdate/getrects(_:rectcount:).md)
  Returns an array of rectangles that describe where the frame has changed since the previous frame.
- [init?(mergedUpdateFirstUpdate: CGDisplayStreamUpdate?, secondUpdate: CGDisplayStreamUpdate?)](cgdisplaystreamupdate/init(mergedupdatefirstupdate:secondupdate:).md)
  Combines two updates into a new update that includes the metadata for both source updates.
- [func getMovedRectsDelta(dx: UnsafeMutablePointer<CGFloat>, dy: UnsafeMutablePointer<CGFloat>)](cgdisplaystreamupdate/getmovedrectsdelta(dx:dy:).md)
  Return the movement delta values for a single update.
- [var dropCount: Int](cgdisplaystreamupdate/dropcount.md)
  Returns the number of frames that have been dropped since the last call to your update handler.
- [class var typeID: CFTypeID](cgdisplaystream/typeid.md)
  Returns the type identifier of a Quartz display stream.
- [class var typeID: CFTypeID](cgdisplaystreamupdate/typeid.md)
  Returns the type identifier of a Quartz display stream update.
### Callbacks
- [typealias CGDisplayReconfigurationCallBack](cgdisplayreconfigurationcallback.md)
  A client-supplied callback function that’s invoked whenever the configuration of a local display is changed.
- [typealias CGScreenRefreshCallback](cgscreenrefreshcallback.md)
  A client-supplied callback function that’s invoked when an area of the display is modified or refreshed.
- [typealias CGScreenUpdateMoveCallback](cgscreenupdatemovecallback.md)
  A client-supplied callback function invoked when an area of the display is moved.
### Data Types
- [typealias CGDirectDisplayID](cgdirectdisplayid.md)
  A unique identifier for an attached display.
- [typealias CGDisplayBlendFraction](cgdisplayblendfraction.md)
  The percentage of blend color used in a fade operation.
- [typealias CGDisplayConfigRef](cgdisplayconfigref.md)
  A reference to a display configuration transaction.
- [typealias CGDisplayCount](cgdisplaycount.md)
  The number of displays in various lists.
- [typealias CGDisplayErr](cgdisplayerr.md)
  A uniform type for result codes returned by functions in Quartz Display Services.
- [typealias CGDisplayFadeInterval](cgdisplayfadeinterval.md)
  The duration in seconds of a fade operation or a fade hardware reservation.
- [typealias CGDisplayFadeReservationToken](cgdisplayfadereservationtoken.md)
  A token issued by Quartz when reserving one or more displays for a fade operation during a specified interval.
- [class CGDisplayMode](cgdisplaymode.md)
  A reference to a display mode object.
- [typealias CGDisplayReservationInterval](cgdisplayreservationinterval.md)
  The time interval for a fade reservation.
- [typealias CGGammaValue](cggammavalue.md)
  A value used to map a color generated in software to a color supported by the display hardware.
- [typealias CGOpenGLDisplayMask](cgopengldisplaymask.md)
  A bitmask used in OpenGL to specify a set of attached displays.
- [typealias CGRectCount](cgrectcount.md)
  The size of an array of Quartz rectangles.
- [typealias CGRefreshRate](cgrefreshrate.md)
  A display’s refresh rate in frames per second.
- [struct CGScreenUpdateMoveDelta](cgscreenupdatemovedelta.md)
  The distance, in pixel units, that an onscreen region moves.
- [typealias CGWindowLevel](cgwindowlevel.md)
  A level assigned to a window by an application framework.
- [class CGDisplayStream](cgdisplaystream.md)
  A reference to a display stream object.
- [class CGDisplayStreamUpdate](cgdisplaystreamupdate.md)
  A reference to frame update’s metadata.
- [typealias CGDisplayStreamFrameAvailableHandler](cgdisplaystreamframeavailablehandler.md)
  A block called when a data stream has a new frame event to process.
### Constants
- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [struct CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md)
  The configuration parameters that are passed to a display reconfiguration callback function.
- [struct CGConfigureOption](cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
- [Display Fade Blend Fractions](display-fade-blend-fractions.md)
  The lower and upper bounds for blend color fractions during a display fade operation.
- [Display Fade Constants](display-fade-constants.md)
  Values relating to fade operations.
- [Display ID Defaults](display-id-defaults.md)
  Default values for a display ID.
- [Display Mode Standard Properties](display-mode-standard-properties.md)
  Keys for the standard properties in a display mode dictionary.
- [Display Mode Optional Properties](display-mode-optional-properties.md)
  Keys for optional properties in a display mode dictionary.
- [Reserved Window Levels](reserved-window-levels.md)
  Window level constants.
- [struct CGScreenUpdateOperation](cgscreenupdateoperation.md)
  Types of screen-update operations.
- [enum CGWindowLevelKey](cgwindowlevelkey.md)
  Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.
- [Window Server Session Properties](window-server-session-properties.md)
  The keys for the standard properties in a window server session dictionary.
- [enum CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md)
  Use these constants to determine which rectangles your app is interested in.
- [enum CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md)
  Describes a frame update event.
- [Display Stream Optional Property Keys](display-stream-optional-property-keys.md)
  These keys are used to populate the `properties` dictionary used when creating a new display stream.
- [Display Stream YCbCr to RGB conversion Matrix Options](display-stream-ycbcr-to-rgb-conversion-matrix-options.md)
  These strings are used to specify a matrix for the [`yCbCrMatrix`](cgdisplaystream/ycbcrmatrix.md) option.

## See Also

- [Quartz Display Services Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzDisplayServicesConceptual/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004316)
- [Quartz Event Services](quartz-event-services.md)
  Provides features for managing —filters for observing and altering the stream of low-level user input events in macOS.
- [Quartz Window Services](quartz-window-services.md)
  Provides information about the windows managed by the macOS window server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/quartz-display-services)*