# Core Graphics Functions

**Framework**: Core Graphics  
**Role**: API Collection

## Topics

### Functions
- [func CGAcquireDisplayFadeReservation(CGDisplayReservationInterval, UnsafeMutablePointer<CGDisplayFadeReservationToken>?) -> CGError](./cgacquiredisplayfadereservation%28_,_%29.md)
  Reserves the fade hardware for a specified time interval.
- [func CGAssociateMouseAndMouseCursorPosition(boolean_t) -> CGError](./cgassociatemouseandmousecursorposition%28_%29.md)
  Connects or disconnects the mouse and cursor while an application is in the foreground.
- [func CGBeginDisplayConfiguration(UnsafeMutablePointer<CGDisplayConfigRef?>?) -> CGError](./cgbegindisplayconfiguration%28_%29.md)
  Begins a new set of display configuration changes.
- [func CGCancelDisplayConfiguration(CGDisplayConfigRef?) -> CGError](./cgcanceldisplayconfiguration%28_%29.md)
  Cancels a set of display configuration changes.
- [func CGCaptureAllDisplays() -> CGError](./cgcapturealldisplays%28%29.md)
  Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [func CGCaptureAllDisplaysWithOptions(CGCaptureOptions) -> CGError](./cgcapturealldisplayswithoptions%28_%29.md)
  Captures all attached displays, using the specified options.
- [func CGCompleteDisplayConfiguration(CGDisplayConfigRef?, CGConfigureOption) -> CGError](./cgcompletedisplayconfiguration%28_,_%29.md)
  Completes a set of display configuration changes.
- [func CGConfigureDisplayFadeEffect(CGDisplayConfigRef?, CGDisplayFadeInterval, CGDisplayFadeInterval, Float, Float, Float) -> CGError](./cgconfiguredisplayfadeeffect%28_,_,_,_,_,_%29.md)
  Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [func CGConfigureDisplayMirrorOfDisplay(CGDisplayConfigRef?, CGDirectDisplayID, CGDirectDisplayID) -> CGError](./cgconfiguredisplaymirrorofdisplay%28_,_,_%29.md)
  Changes the configuration of a mirroring set.
- [func CGConfigureDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CFDictionary?) -> CGError](./cgconfiguredisplaymode%28_,_,_%29.md)
  Configures the display mode of a display.
- [func CGConfigureDisplayOrigin(CGDisplayConfigRef?, CGDirectDisplayID, Int32, Int32) -> CGError](./cgconfiguredisplayorigin%28_,_,_,_%29.md)
  Configures the origin of a display relative to the global display coordinate space.
- [func CGConfigureDisplayStereoOperation(CGDisplayConfigRef?, CGDirectDisplayID, boolean_t, boolean_t) -> CGError](./cgconfiguredisplaystereooperation%28_,_,_,_%29.md)
  Enables or disables stereo operation for a display, as part of a display configuration.
- [func CGConfigureDisplayWithDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](./cgconfiguredisplaywithdisplaymode%28_,_,_,_%29.md)
  Configures the display mode of a display.
- [func CGCursorIsDrawnInFramebuffer() -> boolean_t](./cgcursorisdrawninframebuffer%28%29.md)
  Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory.
- [func CGCursorIsVisible() -> boolean_t](./cgcursorisvisible%28%29.md)
  Returns a Boolean value indicating whether the mouse cursor is visible.
- [func CGDirectDisplayCopyCurrentMetalDevice(CGDirectDisplayID) -> (any MTLDevice)?](./cgdirectdisplaycopycurrentmetaldevice%28_%29.md)
  Returns the GPU device instance that’s currently driving a display.
- [func CGDisplayAvailableModes(CGDirectDisplayID) -> CFArray?](./cgdisplayavailablemodes%28_%29.md)
  Returns information about the currently available display modes.
- [func CGDisplayBestModeForParameters(CGDirectDisplayID, Int, Int, Int, UnsafeMutablePointer<boolean_t>?) -> CFDictionary?](./cgdisplaybestmodeforparameters%28_,_,_,_,_%29.md)
  Returns information about the display mode closest to a specified depth and screen size.
- [func CGDisplayBestModeForParametersAndRefreshRate(CGDirectDisplayID, Int, Int, Int, CGRefreshRate, UnsafeMutablePointer<boolean_t>?) -> CFDictionary?](./cgdisplaybestmodeforparametersandrefreshrate%28_,_,_,_,_,_%29.md)
  Returns information about the display mode closest to a specified depth, screen size, and refresh rate.
- [func CGDisplayBounds(CGDirectDisplayID) -> CGRect](./cgdisplaybounds%28_%29.md)
  Returns the bounds of a display in the global display coordinate space.
- [func CGDisplayCapture(CGDirectDisplayID) -> CGError](./cgdisplaycapture%28_%29.md)
  Obtains exclusive use of a display, preventing other applications and system services from using the display or changing its configuration.
- [func CGDisplayCaptureWithOptions(CGDirectDisplayID, CGCaptureOptions) -> CGError](./cgdisplaycapturewithoptions%28_,_%29.md)
  Obtains exclusive use of a display for an application using the options you specify.
- [func CGDisplayCopyAllDisplayModes(CGDirectDisplayID, CFDictionary?) -> CFArray?](./cgdisplaycopyalldisplaymodes%28_,_%29.md)
  Returns information about the currently available display modes.
- [func CGDisplayCopyColorSpace(CGDirectDisplayID) -> CGColorSpace](./cgdisplaycopycolorspace%28_%29.md)
  Returns the color space for a display.
- [func CGDisplayCopyDisplayMode(CGDirectDisplayID) -> CGDisplayMode?](./cgdisplaycopydisplaymode%28_%29.md)
  Returns information about a display’s current configuration.
- [func CGDisplayCurrentMode(CGDirectDisplayID) -> CFDictionary?](./cgdisplaycurrentmode%28_%29.md)
  Returns information about the current display mode.
- [func CGDisplayFade(CGDisplayFadeReservationToken, CGDisplayFadeInterval, CGDisplayBlendFraction, CGDisplayBlendFraction, Float, Float, Float, boolean_t) -> CGError](./cgdisplayfade%28_,_,_,_,_,_,_,_%29.md)
  Performs a single fade operation.
- [func CGDisplayFadeOperationInProgress() -> boolean_t](./cgdisplayfadeoperationinprogress%28%29.md)
  Returns a Boolean value indicating whether a fade operation is currently in progress.
- [func CGDisplayGammaTableCapacity(CGDirectDisplayID) -> UInt32](./cgdisplaygammatablecapacity%28_%29.md)
  Returns the capacity, or number of entries, in the gamma table for a display.
- [func CGDisplayGetDrawingContext(CGDirectDisplayID) -> CGContext?](./cgdisplaygetdrawingcontext%28_%29.md)
  Returns a graphics context suitable for drawing to a captured display.
- [func CGDisplayHideCursor(CGDirectDisplayID) -> CGError](./cgdisplayhidecursor%28_%29.md)
  Hides the mouse cursor, and increments the hide cursor count.
- [func CGDisplayIDToOpenGLDisplayMask(CGDirectDisplayID) -> CGOpenGLDisplayMask](./cgdisplayidtoopengldisplaymask%28_%29.md)
  Maps a display ID to an OpenGL display mask.
- [func CGDisplayIOServicePort(CGDirectDisplayID) -> io_service_t](./cgdisplayioserviceport%28_%29.md)
  Returns the I/O Kit service port of the specified display.
- [func CGDisplayIsActive(CGDirectDisplayID) -> boolean_t](./cgdisplayisactive%28_%29.md)
  Returns a Boolean value indicating whether a display is active.
- [func CGDisplayIsAlwaysInMirrorSet(CGDirectDisplayID) -> boolean_t](./cgdisplayisalwaysinmirrorset%28_%29.md)
  Returns a Boolean value indicating whether a display is always in a mirroring set.
- [func CGDisplayIsAsleep(CGDirectDisplayID) -> boolean_t](./cgdisplayisasleep%28_%29.md)
  Returns a Boolean value indicating whether a display is sleeping (and is therefore not drawable).
- [func CGDisplayIsBuiltin(CGDirectDisplayID) -> boolean_t](./cgdisplayisbuiltin%28_%29.md)
  Returns a Boolean value indicating whether a display is built-in, such as the internal display in portable systems.
- [func CGDisplayIsCaptured(CGDirectDisplayID) -> boolean_t](./cgdisplayiscaptured%28_%29.md)
  Returns a Boolean value indicating whether a display is captured.
- [func CGDisplayIsInHWMirrorSet(CGDirectDisplayID) -> boolean_t](./cgdisplayisinhwmirrorset%28_%29.md)
  Returns a Boolean value indicating whether a display is in a hardware mirroring set.
- [func CGDisplayIsInMirrorSet(CGDirectDisplayID) -> boolean_t](./cgdisplayisinmirrorset%28_%29.md)
  Returns a Boolean value indicating whether a display is in a mirroring set.
- [func CGDisplayIsMain(CGDirectDisplayID) -> boolean_t](./cgdisplayismain%28_%29.md)
  Returns a Boolean value indicating whether a display is the main display.
- [func CGDisplayIsOnline(CGDirectDisplayID) -> boolean_t](./cgdisplayisonline%28_%29.md)
  Returns a Boolean value indicating whether a display is connected or online.
- [func CGDisplayIsStereo(CGDirectDisplayID) -> boolean_t](./cgdisplayisstereo%28_%29.md)
  Returns a Boolean value indicating whether a display is running in a stereo graphics mode.
- [func CGDisplayMirrorsDisplay(CGDirectDisplayID) -> CGDirectDisplayID](./cgdisplaymirrorsdisplay%28_%29.md)
  For a secondary display in a mirroring set, returns the primary display.
- [var pixelEncoding: CFString?](./cgdisplaymode/pixelencoding.md)
  Returns the pixel encoding of the specified display mode.
- [var height: Int](./cgdisplaymode/height.md)
  Returns the height of the specified display mode.
- [var ioDisplayModeID: Int32](./cgdisplaymode/iodisplaymodeid.md)
  Returns the I/O Kit display mode ID of the specified display mode.
- [var ioFlags: UInt32](./cgdisplaymode/ioflags.md)
  Returns the I/O Kit flags of the specified display mode.
- [var pixelWidth: Int](./cgdisplaymode/pixelwidth.md)
- [var refreshRate: Double](./cgdisplaymode/refreshrate.md)
  Returns the refresh rate of the specified display mode.
- [class var typeID: CFTypeID](./cgdisplaymode/typeid.md)
  Returns the type identifier of Quartz display modes.
- [var width: Int](./cgdisplaymode/width.md)
  Returns the width of the specified display mode.
- [func isUsableForDesktopGUI() -> Bool](./cgdisplaymode/isusablefordesktopgui%28%29.md)
  Returns a Boolean value indicating whether the specified display mode is usable for a desktop graphical user interface.
- [func CGDisplayModelNumber(CGDirectDisplayID) -> UInt32](./cgdisplaymodelnumber%28_%29.md)
  Returns the model number of a display monitor.
- [func CGDisplayMoveCursorToPoint(CGDirectDisplayID, CGPoint) -> CGError](./cgdisplaymovecursortopoint%28_,_%29.md)
  Moves the mouse cursor to a specified point relative to the upper-left corner of the display.
- [func CGDisplayPixelsHigh(CGDirectDisplayID) -> Int](./cgdisplaypixelshigh%28_%29.md)
  Returns the display height in pixel units.
- [func CGDisplayPixelsWide(CGDirectDisplayID) -> Int](./cgdisplaypixelswide%28_%29.md)
  Returns the display width in pixel units.
- [func CGDisplayPrimaryDisplay(CGDirectDisplayID) -> CGDirectDisplayID](./cgdisplayprimarydisplay%28_%29.md)
  Returns the primary display in a hardware mirroring set.
- [func CGDisplayRegisterReconfigurationCallback(CGDisplayReconfigurationCallBack?, UnsafeMutableRawPointer?) -> CGError](./cgdisplayregisterreconfigurationcallback%28_,_%29.md)
  Registers a callback function to be invoked whenever a local display is reconfigured.
- [func CGDisplayRelease(CGDirectDisplayID) -> CGError](./cgdisplayrelease%28_%29.md)
  Releases a captured display.
- [func CGDisplayRemoveReconfigurationCallback(CGDisplayReconfigurationCallBack?, UnsafeMutableRawPointer?) -> CGError](./cgdisplayremovereconfigurationcallback%28_,_%29.md)
  Removes the registration of a callback function that’s invoked whenever a local display is reconfigured.
- [func CGDisplayRestoreColorSyncSettings()](./cgdisplayrestorecolorsyncsettings%28%29.md)
  Restores the gamma tables to the values in the user’s ColorSync display profile.
- [func CGDisplayRotation(CGDirectDisplayID) -> Double](./cgdisplayrotation%28_%29.md)
  Returns the rotation angle of a display in degrees.
- [func CGDisplayScreenSize(CGDirectDisplayID) -> CGSize](./cgdisplayscreensize%28_%29.md)
  Returns the width and height of a display in millimeters.
- [func CGDisplaySerialNumber(CGDirectDisplayID) -> UInt32](./cgdisplayserialnumber%28_%29.md)
  Returns the serial number of a display monitor.
- [func CGDisplaySetDisplayMode(CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](./cgdisplaysetdisplaymode%28_,_,_%29.md)
  Switches a display to a different mode.
- [func CGDisplaySetStereoOperation(CGDirectDisplayID, boolean_t, boolean_t, CGConfigureOption) -> CGError](./cgdisplaysetstereooperation%28_,_,_,_%29.md)
  Immediately enables or disables stereo operation for a display.
- [func CGDisplayShowCursor(CGDirectDisplayID) -> CGError](./cgdisplayshowcursor%28_%29.md)
  Decrements the hide cursor count, and shows the mouse cursor if the count is `0`.
- [func CGDisplaySwitchToMode(CGDirectDisplayID, CFDictionary?) -> CGError](./cgdisplayswitchtomode%28_,_%29.md)
  Switches a display to a different mode.
- [func CGDisplayUnitNumber(CGDirectDisplayID) -> UInt32](./cgdisplayunitnumber%28_%29.md)
  Returns the logical unit number of a display.
- [func CGDisplayUsesOpenGLAcceleration(CGDirectDisplayID) -> boolean_t](./cgdisplayusesopenglacceleration%28_%29.md)
  Returns a Boolean value indicating whether Quartz is using OpenGL-based window acceleration (Quartz Extreme) to render in a display.
- [func CGDisplayVendorNumber(CGDirectDisplayID) -> UInt32](./cgdisplayvendornumber%28_%29.md)
  Returns the vendor number of the specified display’s monitor.
- [func CGEnableEventStateCombining(boolean_t) -> CGError](./cgenableeventstatecombining%28_%29.md)
  Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event.
- [init?(source: CGEventSource?)](./cgevent/init%28source%29.md)
  Returns a new Quartz event.
- [func copy() -> CGEvent?](./cgevent/copy%28%29.md)
  Returns a copy of an existing Quartz event.
- [init?(withDataAllocator: CFAllocator?, data: CFData?)](./cgevent/init%28withdataallocator,data%29.md)
  Returns a Quartz event created from a flattened data representation of the event.
- [init?(keyboardEventSource: CGEventSource?, virtualKey: CGKeyCode, keyDown: Bool)](./cgevent/init%28keyboardeventsource,virtualkey,keydown%29.md)
  Returns a new Quartz keyboard event.
- [init?(mouseEventSource: CGEventSource?, mouseType: CGEventType, mouseCursorPosition: CGPoint, mouseButton: CGMouseButton)](./cgevent/init%28mouseeventsource,mousetype,mousecursorposition,mousebutton%29.md)
  Returns a new Quartz mouse event.
- [init?(event: CGEvent?)](./cgeventsource/init%28event%29.md)
  Returns a Quartz event source created from an existing Quartz event.
- [func getDoubleValueField(CGEventField) -> Double](./cgevent/getdoublevaluefield%28_%29.md)
  Returns the floating-point value of a field in a Quartz event.
- [var flags: CGEventFlags](./cgevent/flags.md)
  Returns the event flags of a Quartz event.
- [func getIntegerValueField(CGEventField) -> Int64](./cgevent/getintegervaluefield%28_%29.md)
  Returns the integer value of a field in a Quartz event.
- [var location: CGPoint](./cgevent/location.md)
  Returns the location of a Quartz mouse event.
- [var timestamp: CGEventTimestamp](./cgevent/timestamp.md)
  Returns the timestamp of a Quartz event.
- [var type: CGEventType](./cgevent/type.md)
  Returns the event type of a Quartz event (left mouse down, for example).
- [class var typeID: CFTypeID](./cgevent/typeid.md)
  Returns the type identifier for the opaque type `CGEventRef`.
- [var unflippedLocation: CGPoint](./cgevent/unflippedlocation.md)
  Returns the location of a Quartz mouse event.
- [func keyboardGetUnicodeString(maxStringLength: Int, actualStringLength: UnsafeMutablePointer<Int>?, unicodeString: UnsafeMutablePointer<UniChar>?)](./cgevent/keyboardgetunicodestring%28maxstringlength,actualstringlength,unicodestring%29.md)
  Returns the Unicode string associated with a Quartz keyboard event.
- [func keyboardSetUnicodeString(stringLength: Int, unicodeString: UnsafePointer<UniChar>?)](./cgevent/keyboardsetunicodestring%28stringlength,unicodestring%29.md)
  Sets the Unicode string associated with a Quartz keyboard event.
- [func post(tap: CGEventTapLocation)](./cgevent/post%28tap%29.md)
  Posts a Quartz event into the event stream at a specified location.
- [func postToPSN(processSerialNumber: UnsafeMutableRawPointer?)](./cgevent/posttopsn%28processserialnumber%29.md)
  Posts a Quartz event into the event stream for a specific application.
- [func postToPid(pid_t)](./cgevent/posttopid%28_%29.md)
- [func setDoubleValueField(CGEventField, value: Double)](./cgevent/setdoublevaluefield%28_,value%29.md)
  Sets the floating-point value of a field in a Quartz event.
- [func setIntegerValueField(CGEventField, value: Int64)](./cgevent/setintegervaluefield%28_,value%29.md)
  Sets the integer value of a field in a Quartz event.
- [func setSource(CGEventSource?)](./cgevent/setsource%28_%29.md)
  Sets the event source of a Quartz event.
- [class func buttonState(CGEventSourceStateID, button: CGMouseButton) -> Bool](./cgeventsource/buttonstate%28_,button%29.md)
  Returns a Boolean value indicating the current button state of a Quartz event source.
- [class func counterForEventType(CGEventSourceStateID, eventType: CGEventType) -> UInt32](./cgeventsource/counterforeventtype%28_,eventtype%29.md)
  Returns a count of events of a given type seen since the window server started.
- [init?(stateID: CGEventSourceStateID)](./cgeventsource/init%28stateid%29.md)
  Returns a Quartz event source created with a specified source state.
- [class func flagsState(CGEventSourceStateID) -> CGEventFlags](./cgeventsource/flagsstate%28_%29.md)
  Returns the current flags of a Quartz event source.
- [var keyboardType: CGEventSourceKeyboardType](./cgeventsource/keyboardtype.md)
  Returns the keyboard type to be used with a Quartz event source.
- [func getLocalEventsFilterDuringSuppressionState(CGEventSuppressionState) -> CGEventFilterMask](./cgeventsource/getlocaleventsfilterduringsuppressionstate%28_%29.md)
  Returns the mask that indicates which classes of local hardware events are enabled during event suppression.
- [var pixelsPerLine: Double](./cgeventsource/pixelsperline.md)
  Gets the scale of pixels per line in a scrolling event source.
- [var sourceStateID: CGEventSourceStateID](./cgeventsource/sourcestateid.md)
  Returns the source state associated with a Quartz event source.
- [class var typeID: CFTypeID](./cgeventsource/typeid.md)
  Returns the type identifier for the opaque type `CGEventSourceRef`.
- [var userData: Int64](./cgeventsource/userdata.md)
  Returns the 64-bit user-specified data for a Quartz event source.
- [class func keyState(CGEventSourceStateID, key: CGKeyCode) -> Bool](./cgeventsource/keystate%28_,key%29.md)
  Returns a Boolean value indicating the current keyboard state of a Quartz event source.
- [class func secondsSinceLastEventType(CGEventSourceStateID, eventType: CGEventType) -> CFTimeInterval](./cgeventsource/secondssincelasteventtype%28_,eventtype%29.md)
  Returns the elapsed time since the last event for a Quartz event source.
- [func setLocalEventsFilterDuringSuppressionState(CGEventFilterMask, state: CGEventSuppressionState)](./cgeventsource/setlocaleventsfilterduringsuppressionstate%28_,state%29.md)
  Sets the mask that indicates which classes of local hardware events are enabled during event suppression.
- [class func tapCreate(tap: CGEventTapLocation, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](./cgevent/tapcreate%28tap,place,options,eventsofinterest,callback,userinfo%29.md)
  Creates an event tap.
- [class func tapCreateForPSN(processSerialNumber: UnsafeMutableRawPointer, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](./cgevent/tapcreateforpsn%28processserialnumber,place,options,eventsofinterest,callback,userinfo%29.md)
  Creates an event tap for a specified process.
- [class func tapCreateForPid(pid: pid_t, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](./cgevent/tapcreateforpid%28pid,place,options,eventsofinterest,callback,userinfo%29.md)
- [class func tapEnable(tap: CFMachPort, enable: Bool)](./cgevent/tapenable%28tap,enable%29.md)
  Enables or disables an event tap.
- [class func tapIsEnabled(tap: CFMachPort) -> Bool](./cgevent/tapisenabled%28tap%29.md)
  Returns a Boolean value indicating whether an event tap is enabled.
- [func tapPostEvent(CGEventTapProxy?)](./cgevent/tappostevent%28_%29.md)
  Posts a Quartz event from an event tap into the event stream.
- [func CGGetActiveDisplayList(UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cggetactivedisplaylist%28_,_,_%29.md)
  Provides a list of displays that are active for drawing.
- [func CGGetDisplayTransferByFormula(CGDirectDisplayID, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?) -> CGError](./cggetdisplaytransferbyformula%28_,_,_,_,_,_,_,_,_,_%29.md)
  Gets the coefficients of the gamma transfer formula for a display.
- [func CGGetDisplayTransferByTable(CGDirectDisplayID, UInt32, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cggetdisplaytransferbytable%28_,_,_,_,_,_%29.md)
  Gets the values in the RGB gamma tables for a display.
- [func CGGetDisplaysWithOpenGLDisplayMask(CGOpenGLDisplayMask, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cggetdisplayswithopengldisplaymask%28_,_,_,_%29.md)
  Provides a list of displays that corresponds to the bits set in an OpenGL display mask.
- [func CGGetDisplaysWithPoint(CGPoint, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cggetdisplayswithpoint%28_,_,_,_%29.md)
  Provides a list of online displays with bounds that include the specified point.
- [func CGGetDisplaysWithRect(CGRect, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cggetdisplayswithrect%28_,_,_,_%29.md)
  Gets a list of online displays with bounds that intersect the specified rectangle.
- [func CGGetEventTapList(UInt32, UnsafeMutablePointer<CGEventTapInformation>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cggeteventtaplist%28_,_,_%29.md)
  Gets a list of currently installed event taps.
- [func CGGetLastMouseDelta() -> (x: Int32, y: Int32)](./cggetlastmousedelta%28%29.md)
  Reports the change in mouse position since the last mouse movement event received by the application.
- [func CGGetOnlineDisplayList(UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cggetonlinedisplaylist%28_,_,_%29.md)
  Provides a list of displays that are online (active, mirrored, or sleeping).
- [var utType: CFString?](./cgimage/uttype.md)
  The Universal Type Identifier for the image.
- [func CGInhibitLocalEvents(boolean_t) -> CGError](./cginhibitlocalevents%28_%29.md)
  Turns off local hardware events in the current session.
- [func CGMainDisplayID() -> CGDirectDisplayID](./cgmaindisplayid%28%29.md)
  Returns the display ID of the main display.
- [func CGOpenGLDisplayMaskToDisplayID(CGOpenGLDisplayMask) -> CGDirectDisplayID](./cgopengldisplaymasktodisplayid%28_%29.md)
  Maps an OpenGL display mask to a display ID.
- [func CGPointEqualToPoint(CGPoint, CGPoint) -> Bool](./cgpointequaltopoint%28_,_%29.md)
  Returns whether two points are equal.
- [func CGPostKeyboardEvent(CGCharCode, CGKeyCode, boolean_t) -> CGError](./cgpostkeyboardevent%28_,_,_%29.md)
  Synthesizes a low-level keyboard event on the local machine.
- [func CGRegisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?) -> CGError](./cgregisterscreenrefreshcallback%28_,_%29.md)
  Registers a callback function to be invoked when local displays are refreshed or modified.
- [func CGReleaseAllDisplays() -> CGError](./cgreleasealldisplays%28%29.md)
  Releases all captured displays.
- [func CGReleaseDisplayFadeReservation(CGDisplayFadeReservationToken) -> CGError](./cgreleasedisplayfadereservation%28_%29.md)
  Releases a display fade reservation, and unfades the display if needed.
- [func CGReleaseScreenRefreshRects(UnsafeMutablePointer<CGRect>?)](./cgreleasescreenrefreshrects%28_%29.md)
  Deallocates a list of rectangles that represent changed areas on local displays.
- [func CGRestorePermanentDisplayConfiguration()](./cgrestorepermanentdisplayconfiguration%28%29.md)
  Restores the permanent display configuration settings for the current user.
- [func CGScreenRegisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?) -> CGError](./cgscreenregistermovecallback%28_,_%29.md)
  Registers a callback function to be invoked when an area of the display is moved.
- [func CGScreenUnregisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?)](./cgscreenunregistermovecallback%28_,_%29.md)
  Removes a previously registered callback function invoked when an area of the display is moved.
- [func CGSessionCopyCurrentDictionary() -> CFDictionary?](./cgsessioncopycurrentdictionary%28%29.md)
  Returns information about the caller’s window server session.
- [func CGSetDisplayTransferByByteTable(CGDirectDisplayID, UInt32, UnsafePointer<UInt8>, UnsafePointer<UInt8>, UnsafePointer<UInt8>) -> CGError](./cgsetdisplaytransferbybytetable%28_,_,_,_,_%29.md)
  Sets the byte values in the 8-bit RGB gamma tables for a display.
- [func CGSetDisplayTransferByFormula(CGDirectDisplayID, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue) -> CGError](./cgsetdisplaytransferbyformula%28_,_,_,_,_,_,_,_,_,_%29.md)
  Sets the gamma function for a display by specifying the coefficients of the gamma transfer formula.
- [func CGSetDisplayTransferByTable(CGDirectDisplayID, UInt32, UnsafePointer<CGGammaValue>?, UnsafePointer<CGGammaValue>?, UnsafePointer<CGGammaValue>?) -> CGError](./cgsetdisplaytransferbytable%28_,_,_,_,_%29.md)
  Sets the color gamma function for a display by specifying the values in the RGB gamma tables.
- [func CGSetLocalEventsFilterDuringSuppressionState(CGEventFilterMask, CGEventSuppressionState) -> CGError](./cgsetlocaleventsfilterduringsuppressionstate%28_,_%29.md)
  Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted.
- [func CGSetLocalEventsSuppressionInterval(CFTimeInterval) -> CGError](./cgsetlocaleventssuppressioninterval%28_%29.md)
  Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event.
- [func CGShieldingWindowID(CGDirectDisplayID) -> CGWindowID](./cgshieldingwindowid%28_%29.md)
  Returns the window ID of the shield window for a captured display.
- [func CGShieldingWindowLevel() -> CGWindowLevel](./cgshieldingwindowlevel%28%29.md)
  Returns the window level of the shield window for a captured display.
- [func CGSizeEqualToSize(CGSize, CGSize) -> Bool](./cgsizeequaltosize%28_,_%29.md)
  Returns whether two sizes are equal.
- [func CGUnregisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?)](./cgunregisterscreenrefreshcallback%28_,_%29.md)
  Removes a previously registered callback function invoked when local displays are refreshed or modified.
- [func CGWaitForScreenRefreshRects(UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cgwaitforscreenrefreshrects%28_,_%29.md)
  Waits for screen refresh operations.
- [func CGWaitForScreenUpdateRects(CGScreenUpdateOperation, UnsafeMutablePointer<CGScreenUpdateOperation>?, UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<CGScreenUpdateMoveDelta>?) -> CGError](./cgwaitforscreenupdaterects%28_,_,_,_,_%29.md)
  Waits for screen update operations.
- [func CGWarpMouseCursorPosition(CGPoint) -> CGError](./cgwarpmousecursorposition%28_%29.md)
  Moves the mouse cursor without generating events.
- [func CGWindowLevelForKey(CGWindowLevelKey) -> CGWindowLevel](./cgwindowlevelforkey%28_%29.md)
  Returns the window level that corresponds to one of the standard window types.
- [func CGWindowListCopyWindowInfo(CGWindowListOption, CGWindowID) -> CFArray?](./cgwindowlistcopywindowinfo%28_,_%29.md)
  Generates and returns information about the selected windows in the current user session.
- [func CGWindowListCreateDescriptionFromArray(CFArray?) -> CFArray?](./cgwindowlistcreatedescriptionfromarray%28_%29.md)
  Generates and returns information about windows with the specified window IDs.
- [func CGWindowServerCFMachPort() -> CFMachPort?](./cgwindowservercfmachport%28%29.md)
  Returns a Core Foundation Mach port (CFMachPort) that corresponds to the macOS window server.
- [func CGWindowServerCreateServerPort() -> CFMachPort?](./cgwindowservercreateserverport%28%29.md)
- [func acos(CGFloat) -> CGFloat](./acos%28_%29.md)
- [func acosh(CGFloat) -> CGFloat](./acosh%28_%29.md)
- [func asin(CGFloat) -> CGFloat](./asin%28_%29.md)
- [func asinh(CGFloat) -> CGFloat](./asinh%28_%29.md)
- [func atan(CGFloat) -> CGFloat](./atan%28_%29.md)
- [func atan2(CGFloat, CGFloat) -> CGFloat](./atan2%28_,_%29.md)
- [func atanh(CGFloat) -> CGFloat](./atanh%28_%29.md)
- [func cbrt(CGFloat) -> CGFloat](./cbrt%28_%29.md)
- [func copysign(CGFloat, CGFloat) -> CGFloat](./copysign%28_,_%29.md)
- [func cos(CGFloat) -> CGFloat](./cos%28_%29.md)
- [func cosh(CGFloat) -> CGFloat](./cosh%28_%29.md)
- [func erf(CGFloat) -> CGFloat](./erf%28_%29.md)
- [func erfc(CGFloat) -> CGFloat](./erfc%28_%29.md)
- [func exp(CGFloat) -> CGFloat](./exp%28_%29.md)
- [func exp2(CGFloat) -> CGFloat](./exp2%28_%29.md)
- [func expm1(CGFloat) -> CGFloat](./expm1%28_%29.md)
- [func fdim(CGFloat, CGFloat) -> CGFloat](./fdim%28_,_%29.md)
- [func fmax(CGFloat, CGFloat) -> CGFloat](./fmax%28_,_%29.md)
- [func fmin(CGFloat, CGFloat) -> CGFloat](./fmin%28_,_%29.md)
- [func hypot(CGFloat, CGFloat) -> CGFloat](./hypot%28_,_%29.md)
- [func ilogb(CGFloat) -> Int](./ilogb%28_%29.md)
- [func CGColorSpaceCreateLinearized(CGColorSpace) -> CGColorSpace?](./cgcolorspacecreatelinearized%28_%29.md)
- [init?(src: CGColorSpace, dst: CGColorSpace)](./cgcolorconversioninfo/init%28src,dst%29.md)
  Creates a conversion between two specified color spaces.
- [func j0(CGFloat) -> CGFloat](./j0%28_%29.md)
- [func j1(CGFloat) -> CGFloat](./j1%28_%29.md)
- [func jn(Int, CGFloat) -> CGFloat](./jn%28_,_%29.md)
- [func ldexp(CGFloat, Int) -> CGFloat](./ldexp%28_,_%29.md)
- [func lgamma(CGFloat) -> (CGFloat, Int)](./lgamma%28_%29.md)
- [func log(CGFloat) -> CGFloat](./log%28_%29.md)
- [func log10(CGFloat) -> CGFloat](./log10%28_%29.md)
- [func log1p(CGFloat) -> CGFloat](./log1p%28_%29.md)
- [func log2(CGFloat) -> CGFloat](./log2%28_%29.md)
- [func logb(CGFloat) -> CGFloat](./logb%28_%29.md)
- [func nan(String) -> CGFloat](./nan%28_%29.md)
- [func nearbyint(CGFloat) -> CGFloat](./nearbyint%28_%29.md)
- [func nextafter(CGFloat, CGFloat) -> CGFloat](./nextafter%28_,_%29.md)
- [func pow(CGFloat, CGFloat) -> CGFloat](./pow%28_,_%29.md)
- [func remquo(CGFloat, CGFloat) -> (CGFloat, Int)](./remquo%28_,_%29.md)
- [func rint(CGFloat) -> CGFloat](./rint%28_%29.md)
- [func sin(CGFloat) -> CGFloat](./sin%28_%29.md)
- [func sinh(CGFloat) -> CGFloat](./sinh%28_%29.md)
- [func tan(CGFloat) -> CGFloat](./tan%28_%29.md)
- [func tanh(CGFloat) -> CGFloat](./tanh%28_%29.md)
- [func tgamma(CGFloat) -> CGFloat](./tgamma%28_%29.md)
- [var localEventsSuppressionInterval: CFTimeInterval](./cgeventsource/localeventssuppressioninterval.md)
  Returns the interval that local hardware events may be suppressed following the posting of a Quartz event.
- [var pixelHeight: Int](./cgdisplaymode/pixelheight.md)
- [class var typeID: CFTypeID](./cgcolorconversioninfo/typeid.md)
  Returns the Core Foundation type identifier for a color conversion info data type.
- [func y0(CGFloat) -> CGFloat](./y0%28_%29.md)
- [func y1(CGFloat) -> CGFloat](./y1%28_%29.md)
- [func yn(Int, CGFloat) -> CGFloat](./yn%28_,_%29.md)
- [func CGAffineTransformMake(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformmake%28_,_,_,_,_,_%29.md)
  Returns an affine transformation matrix constructed from values you provide.
- [func CGColorSpaceCopyBaseColorSpace(CGColorSpace) -> CGColorSpace](./cgcolorspacecopybasecolorspace%28_%29.md)
- [func CGColorSpaceCreateCopyWithStandardRange(CGColorSpace) -> CGColorSpace](./cgcolorspacecreatecopywithstandardrange%28_%29.md)
- [func CGColorSpaceCreateExtended(CGColorSpace) -> CGColorSpace?](./cgcolorspacecreateextended%28_%29.md)
- [func CGColorSpaceCreateExtendedLinearized(CGColorSpace) -> CGColorSpace?](./cgcolorspacecreateextendedlinearized%28_%29.md)
- [func CGColorSpaceCreateWithColorSyncProfile(ColorSyncProfile?, CFDictionary?) -> CGColorSpace?](./cgcolorspacecreatewithcolorsyncprofile%28_,_%29.md)
- [func CGColorSpaceIsHLGBased(CGColorSpace) -> Bool](./cgcolorspaceishlgbased%28_%29.md)
- [func CGColorSpaceIsPQBased(CGColorSpace) -> Bool](./cgcolorspaceispqbased%28_%29.md)
- [func CGColorSpaceUsesITUR_2100TF(CGColorSpace) -> Bool](./cgcolorspaceusesitur_2100tf%28_%29.md)
- [func CGContextDrawConicGradient(CGContext, CGGradient?, CGPoint, CGFloat)](./cgcontextdrawconicgradient%28_,_,_,_%29.md)
- [func CGContextGetEDRTargetHeadroom(CGContext) -> Float](./cgcontextgetedrtargetheadroom%28_%29.md)
- [func CGConvertColorDataWithFormat(Int, Int, UnsafeMutableRawPointer!, CGColorDataFormat, UnsafeMutableRawPointer!, CGColorDataFormat, CFDictionary!) -> Bool](./cgconvertcolordatawithformat%28_,_,_,_,_,_,_%29.md)
- [func CGEnableEventStateCombining(boolean_t) -> CGError](./cgenableeventstatecombining%28_%29.md)
  Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event.
- [func CGErrorSetCallback(CGErrorCallback!)](./cgerrorsetcallback%28_%29.md)
- [func CGImageCreateCopyWithContentHeadroom(Float, CGImage) -> CGImage?](./cgimagecreatecopywithcontentheadroom%28_,_%29.md)
- [func CGInhibitLocalEvents(boolean_t) -> CGError](./cginhibitlocalevents%28_%29.md)
  Turns off local hardware events in the current session.
- [func CGPDFArrayApplyBlock(CGPDFArrayRef, (Int, CGPDFObjectRef, UnsafeMutableRawPointer?) -> Bool, UnsafeMutableRawPointer?)](./cgpdfarrayapplyblock%28_,_,_%29.md)
- [func CGPDFContextBeginTag(CGContext, CGPDFTagType, CFDictionary)](./cgpdfcontextbegintag%28_,_,_%29.md)
- [func CGPDFContextEndTag(CGContext)](./cgpdfcontextendtag%28_%29.md)
- [func CGPDFContextSetIDTree(CGContext, CGPDFDictionaryRef)](./cgpdfcontextsetidtree%28_,_%29.md)
- [func CGPDFContextSetOutline(CGContext, CFDictionary?)](./cgpdfcontextsetoutline%28_,_%29.md)
- [func CGPDFContextSetPageTagStructureTree(CGContext, CFDictionary)](./cgpdfcontextsetpagetagstructuretree%28_,_%29.md)
- [func CGPDFContextSetParentTree(CGContext, CGPDFDictionaryRef)](./cgpdfcontextsetparenttree%28_,_%29.md)
- [func CGPDFDictionaryApplyBlock(CGPDFDictionaryRef, (UnsafePointer<CChar>, CGPDFObjectRef, UnsafeMutableRawPointer?) -> Bool, UnsafeMutableRawPointer?)](./cgpdfdictionaryapplyblock%28_,_,_%29.md)
- [func CGPDFScannerStop(CGPDFScannerRef)](./cgpdfscannerstop%28_%29.md)
- [func CGPointMake(CGFloat, CGFloat) -> CGPoint](./cgpointmake%28_,_%29.md)
  Returns a point with the specified coordinates.
- [func CGPointMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGPoint>) -> Bool](./cgpointmakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a point using the contents of the specified dictionary.
- [func CGPostKeyboardEvent(CGCharCode, CGKeyCode, boolean_t) -> CGError](./cgpostkeyboardevent%28_,_,_%29.md)
  Synthesizes a low-level keyboard event on the local machine.
- [func CGPreflightListenEventAccess() -> Bool](./cgpreflightlisteneventaccess%28%29.md)
- [func CGPreflightPostEventAccess() -> Bool](./cgpreflightposteventaccess%28%29.md)
- [func CGPreflightScreenCaptureAccess() -> Bool](./cgpreflightscreencaptureaccess%28%29.md)
- [func CGRectMake(CGFloat, CGFloat, CGFloat, CGFloat) -> CGRect](./cgrectmake%28_,_,_,_%29.md)
  Returns a rectangle with the specified coordinate and size values.
- [func CGRectMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGRect>) -> Bool](./cgrectmakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a rectangle using the contents of the specified dictionary.
- [func CGRegisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?) -> CGError](./cgregisterscreenrefreshcallback%28_,_%29.md)
  Registers a callback function to be invoked when local displays are refreshed or modified.
- [func CGReleaseScreenRefreshRects(UnsafeMutablePointer<CGRect>?)](./cgreleasescreenrefreshrects%28_%29.md)
  Deallocates a list of rectangles that represent changed areas on local displays.
- [func CGRequestListenEventAccess() -> Bool](./cgrequestlisteneventaccess%28%29.md)
- [func CGRequestPostEventAccess() -> Bool](./cgrequestposteventaccess%28%29.md)
- [func CGRequestScreenCaptureAccess() -> Bool](./cgrequestscreencaptureaccess%28%29.md)
- [func CGScreenRegisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?) -> CGError](./cgscreenregistermovecallback%28_,_%29.md)
  Registers a callback function to be invoked when an area of the display is moved.
- [func CGScreenUnregisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?)](./cgscreenunregistermovecallback%28_,_%29.md)
  Removes a previously registered callback function invoked when an area of the display is moved.
- [func CGSetLocalEventsFilterDuringSuppressionState(CGEventFilterMask, CGEventSuppressionState) -> CGError](./cgsetlocaleventsfilterduringsuppressionstate%28_,_%29.md)
  Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted.
- [func CGSetLocalEventsSuppressionInterval(CFTimeInterval) -> CGError](./cgsetlocaleventssuppressioninterval%28_%29.md)
  Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event.
- [func CGSizeMake(CGFloat, CGFloat) -> CGSize](./cgsizemake%28_,_%29.md)
  Returns a size with the specified dimension values.
- [func CGSizeMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGSize>) -> Bool](./cgsizemakewithdictionaryrepresentation%28_,_%29.md)
  Fills in a size using the contents of the specified dictionary.
- [func CGUnregisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?)](./cgunregisterscreenrefreshcallback%28_,_%29.md)
  Removes a previously registered callback function invoked when local displays are refreshed or modified.
- [func CGVectorMake(CGFloat, CGFloat) -> CGVector](./cgvectormake%28_,_%29.md)
  Returns a vector with the specified dimension values.
- [func CGWaitForScreenRefreshRects(UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<UInt32>?) -> CGError](./cgwaitforscreenrefreshrects%28_,_%29.md)
  Waits for screen refresh operations.
- [func CGWaitForScreenUpdateRects(CGScreenUpdateOperation, UnsafeMutablePointer<CGScreenUpdateOperation>?, UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<CGScreenUpdateMoveDelta>?) -> CGError](./cgwaitforscreenupdaterects%28_,_,_,_,_%29.md)
  Waits for screen update operations.
- [var accessPermissions: CGPDFAccessPermissions](./cgpdfdocument/accesspermissions.md)
- [func applyWithBlock((UnsafePointer<CGPathElement>) -> Void)](./cgpath/applywithblock%28_%29.md)
- [var byteOrderInfo: CGImageByteOrderInfo](./cgimage/byteorderinfo.md)
- [var containsImageSpecificToneMappingMetadata: Bool](./cgimage/containsimagespecifictonemappingmetadata.md)
- [var contentHeadroom: Float](./cgimage/contentheadroom.md)
- [func convert(width: Int, height: Int, to: UnsafeMutableRawPointer, format: CGColorBufferFormat, from: UnsafeRawPointer, format: CGColorBufferFormat, options: CFDictionary?) -> Bool](./cgcolorconversioninfo/convert%28width,height,to,format,from,format,options%29.md)
- [func copyPropertyList() -> CFPropertyList?](./cgcolorspace/copypropertylist%28%29.md)
  Returns a copy of the color space’s properties.
- [var info: UnsafeMutableRawPointer?](./cgdataprovider/info.md)
- [init(genericGrayGamma2_2Gray: CGFloat, alpha: CGFloat)](./cgcolor/init%28genericgraygamma2_2gray,alpha%29.md)
  Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [init?(headroom: Float, width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](./cgimage/init%28headroom,width,height,bitspercomponent,bitsperpixel,bytesperrow,space,bitmapinfo,provider,decode,shouldinterpolate,intent%29.md)
- [init?(iccData: CFTypeRef)](./cgcolorspace/init%28iccdata%29.md)
  Creates an ICC-based color space using the ICC profile contained in the specified data.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](./cgcolorconversioninfo/init%28optionssrc,dst,options%29.md)
- [init?(propertyListPlist: CFPropertyList)](./cgcolorspace/init%28propertylistplist%29.md)
  Creates a color space from a property list.
- [init?(scrollWheelEvent2Source: CGEventSource?, units: CGScrollEventUnit, wheelCount: UInt32, wheel1: Int32, wheel2: Int32, wheel3: Int32)](./cgevent/init%28scrollwheelevent2source,units,wheelcount,wheel1,wheel2,wheel3%29.md)
- [func isHDR() -> Bool](./cgcolorspace/ishdr%28%29.md)
- [var name: UnsafePointer<CChar>](./cgpdftagtype/name.md)
- [var outline: CFDictionary?](./cgpdfdocument/outline.md)
- [var pixelFormatInfo: CGImagePixelFormatInfo](./cgimage/pixelformatinfo.md)
- [func resetClip()](./cgcontext/resetclip%28%29.md)
- [func setEDRTargetHeadroom(Float) -> Bool](./cgcontext/setedrtargetheadroom%28_%29.md)
- [var shouldToneMap: Bool](./cgimage/shouldtonemap.md)
- [func CGColorSpaceUsesExtendedRange(CGColorSpace) -> Bool](./cgcolorspaceusesextendedrange%28_%29.md)
- [CGColorConversionInfoCreateFromList](./cgcolorconversioninfocreatefromlist.md)
  Creates a conversion between an arbitrary number of specified color spaces.
- [CGContextDrawPDFDocument](./cgcontextdrawpdfdocument.md)
- [CGDisplayModeRelease](./cgdisplaymoderelease.md)
  Releases a Core Graphics display mode.
- [CGDisplayModeRetain](./cgdisplaymoderetain.md)
  Retains a Core Graphics display mode.
- [CGEventCreateData](./cgeventcreatedata.md)
  Returns a flattened data representation of a Quartz event.
- [CGEventCreateScrollWheelEvent](./cgeventcreatescrollwheelevent.md)
  Returns a new Quartz scrolling event.
- [CGEventSetFlags](./cgeventsetflags.md)
  Sets the event flags of a Quartz event.
- [CGEventSetLocation](./cgeventsetlocation.md)
  Sets the location of a Quartz mouse event.
- [CGEventSetTimestamp](./cgeventsettimestamp.md)
  Sets the timestamp of a Quartz event.
- [CGEventSetType](./cgeventsettype.md)
  Sets the event type of a Quartz event (left mouse down, for example).
- [CGEventSourceSetKeyboardType](./cgeventsourcesetkeyboardtype.md)
  Sets the keyboard type to be used with a Quartz event source.
- [CGEventSourceSetLocalEventsSuppressionInterval](./cgeventsourcesetlocaleventssuppressioninterval.md)
  Sets the interval that local hardware events may be suppressed following the posting of a Quartz event.
- [CGEventSourceSetPixelsPerLine](./cgeventsourcesetpixelsperline.md)
  Sets the scale of pixels per line in a scrolling event source.
- [CGEventSourceSetUserData](./cgeventsourcesetuserdata.md)
  Sets the 64-bit user-specified data for a Quartz event source.
- [CGGetLastMouseDelta](./cggetlastmousedelta.md)
  Reports the change in mouse position since the last mouse movement event received by the application.
- [CGPostMouseEvent](./cgpostmouseevent.md)
  Synthesizes a low-level mouse-button event on the local machine.
- [CGPostScrollWheelEvent](./cgpostscrollwheelevent.md)
  Synthesizes a low-level scrolling event on the local machine.
- [CGWindowListCreate](./cgwindowlistcreate.md)
  Returns the list of window IDs associated with the specified windows in the current user session.
- [CGColorConversionInfoCreateFromListWithArguments](./cgcolorconversioninfocreatefromlistwitharguments.md)
- [CGColorSpaceGetName](./cgcolorspacegetname.md)
- [CGContextDrawImageApplyingToneMapping](./cgcontextdrawimageapplyingtonemapping.md)
- [CGPathCreateCopyByFlattening](./cgpathcreatecopybyflattening.md)
- [CGPathCreateCopyByIntersectingPath](./cgpathcreatecopybyintersectingpath.md)
- [CGPathCreateCopyByNormalizing](./cgpathcreatecopybynormalizing.md)
- [CGPathCreateCopyBySubtractingPath](./cgpathcreatecopybysubtractingpath.md)
- [CGPathCreateCopyBySymmetricDifferenceOfPath](./cgpathcreatecopybysymmetricdifferenceofpath.md)
- [CGPathCreateCopyByUnioningPath](./cgpathcreatecopybyunioningpath.md)
- [CGPathCreateCopyOfLineByIntersectingPath](./cgpathcreatecopyoflinebyintersectingpath.md)
- [CGPathCreateCopyOfLineBySubtractingPath](./cgpathcreatecopyoflinebysubtractingpath.md)
- [CGPathCreateSeparateComponents](./cgpathcreateseparatecomponents.md)
- [CGPathIntersectsPath](./cgpathintersectspath.md)
- [CGAffineTransformDecompose](./cgaffinetransformdecompose.md)
- [CGAffineTransformMakeWithComponents](./cgaffinetransformmakewithcomponents.md)

## See Also

### Reference
- [Core Graphics Structures](./core-graphics-structures.md)
- [Core Graphics Enumerations](./core-graphics-enumerations.md)
- [Core Graphics Constants](./core-graphics-constants.md)
- [Core Graphics Data Types](./core-graphics-data-types.md)
- [CGAffineTransform](./cgaffinetransform.md)
  An affine transformation matrix for use in drawing 2D graphics.
- [CGGeometry](./cggeometry.md)
  Various structures and associated functions for 2D geometric primitives.
- [Core Graphics Macros](./core-graphics-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/core-graphics-functions)*