# Core Graphics Functions

**Framework**: Core Graphics

## Topics

### Functions
- [func CGAcquireDisplayFadeReservation(CGDisplayReservationInterval, UnsafeMutablePointer<CGDisplayFadeReservationToken>?) -> CGError](cgacquiredisplayfadereservation(_:_:).md)
  Reserves the fade hardware for a specified time interval.
- [func CGAssociateMouseAndMouseCursorPosition(boolean_t) -> CGError](cgassociatemouseandmousecursorposition(_:).md)
  Connects or disconnects the mouse and cursor while an application is in the foreground.
- [func CGBeginDisplayConfiguration(UnsafeMutablePointer<CGDisplayConfigRef?>?) -> CGError](cgbegindisplayconfiguration(_:).md)
  Begins a new set of display configuration changes.
- [func CGCancelDisplayConfiguration(CGDisplayConfigRef?) -> CGError](cgcanceldisplayconfiguration(_:).md)
  Cancels a set of display configuration changes.
- [func CGCaptureAllDisplays() -> CGError](cgcapturealldisplays().md)
  Obtains exclusive use of all active displays, preventing other applications and system services from using the display or changing its configuration.
- [func CGCaptureAllDisplaysWithOptions(CGCaptureOptions) -> CGError](cgcapturealldisplayswithoptions(_:).md)
  Captures all attached displays, using the specified options.
- [func CGCompleteDisplayConfiguration(CGDisplayConfigRef?, CGConfigureOption) -> CGError](cgcompletedisplayconfiguration(_:_:).md)
  Completes a set of display configuration changes.
- [func CGConfigureDisplayFadeEffect(CGDisplayConfigRef?, CGDisplayFadeInterval, CGDisplayFadeInterval, Float, Float, Float) -> CGError](cgconfiguredisplayfadeeffect(_:_:_:_:_:_:).md)
  Modifies the settings of the built-in fade effect that occurs during a display configuration.
- [func CGConfigureDisplayMirrorOfDisplay(CGDisplayConfigRef?, CGDirectDisplayID, CGDirectDisplayID) -> CGError](cgconfiguredisplaymirrorofdisplay(_:_:_:).md)
  Changes the configuration of a mirroring set.
- [func CGConfigureDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CFDictionary?) -> CGError](cgconfiguredisplaymode(_:_:_:).md)
  Configures the display mode of a display.
- [func CGConfigureDisplayOrigin(CGDisplayConfigRef?, CGDirectDisplayID, Int32, Int32) -> CGError](cgconfiguredisplayorigin(_:_:_:_:).md)
  Configures the origin of a display relative to the global display coordinate space.
- [func CGConfigureDisplayStereoOperation(CGDisplayConfigRef?, CGDirectDisplayID, boolean_t, boolean_t) -> CGError](cgconfiguredisplaystereooperation(_:_:_:_:).md)
  Enables or disables stereo operation for a display, as part of a display configuration.
- [func CGConfigureDisplayWithDisplayMode(CGDisplayConfigRef?, CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](cgconfiguredisplaywithdisplaymode(_:_:_:_:).md)
  Configures the display mode of a display.
- [func CGCursorIsDrawnInFramebuffer() -> boolean_t](cgcursorisdrawninframebuffer().md)
  Returns a Boolean value indicating whether the mouse cursor is drawn in framebuffer memory.
- [func CGCursorIsVisible() -> boolean_t](cgcursorisvisible().md)
  Returns a Boolean value indicating whether the mouse cursor is visible.
- [func CGDirectDisplayCopyCurrentMetalDevice(CGDirectDisplayID) -> (any MTLDevice)?](cgdirectdisplaycopycurrentmetaldevice(_:).md)
  Returns the GPU device instance that’s currently driving a display.
- [func CGDisplayAvailableModes(CGDirectDisplayID) -> CFArray?](cgdisplayavailablemodes(_:).md)
  Returns information about the currently available display modes.
- [func CGDisplayBestModeForParameters(CGDirectDisplayID, Int, Int, Int, UnsafeMutablePointer<boolean_t>?) -> CFDictionary?](cgdisplaybestmodeforparameters(_:_:_:_:_:).md)
  Returns information about the display mode closest to a specified depth and screen size.
- [func CGDisplayBestModeForParametersAndRefreshRate(CGDirectDisplayID, Int, Int, Int, CGRefreshRate, UnsafeMutablePointer<boolean_t>?) -> CFDictionary?](cgdisplaybestmodeforparametersandrefreshrate(_:_:_:_:_:_:).md)
  Returns information about the display mode closest to a specified depth, screen size, and refresh rate.
- [func CGDisplayBounds(CGDirectDisplayID) -> CGRect](cgdisplaybounds(_:).md)
  Returns the bounds of a display in the global display coordinate space.
- [func CGDisplayCapture(CGDirectDisplayID) -> CGError](cgdisplaycapture(_:).md)
  Obtains exclusive use of a display, preventing other applications and system services from using the display or changing its configuration.
- [func CGDisplayCaptureWithOptions(CGDirectDisplayID, CGCaptureOptions) -> CGError](cgdisplaycapturewithoptions(_:_:).md)
  Obtains exclusive use of a display for an application using the options you specify.
- [func CGDisplayCopyAllDisplayModes(CGDirectDisplayID, CFDictionary?) -> CFArray?](cgdisplaycopyalldisplaymodes(_:_:).md)
  Returns information about the currently available display modes.
- [func CGDisplayCopyColorSpace(CGDirectDisplayID) -> CGColorSpace](cgdisplaycopycolorspace(_:).md)
  Returns the color space for a display.
- [func CGDisplayCopyDisplayMode(CGDirectDisplayID) -> CGDisplayMode?](cgdisplaycopydisplaymode(_:).md)
  Returns information about a display’s current configuration.
- [func CGDisplayCreateImage(CGDirectDisplayID) -> CGImage?](cgdisplaycreateimage(_:).md)
  Returns an image containing the contents of the specified display.
- [func CGDisplayCreateImage(CGDirectDisplayID, rect: CGRect) -> CGImage?](cgdisplaycreateimage(_:rect:).md)
  Returns an image containing the contents of a portion of the specified display.
- [func CGDisplayCurrentMode(CGDirectDisplayID) -> CFDictionary?](cgdisplaycurrentmode(_:).md)
  Returns information about the current display mode.
- [func CGDisplayFade(CGDisplayFadeReservationToken, CGDisplayFadeInterval, CGDisplayBlendFraction, CGDisplayBlendFraction, Float, Float, Float, boolean_t) -> CGError](cgdisplayfade(_:_:_:_:_:_:_:_:).md)
  Performs a single fade operation.
- [func CGDisplayFadeOperationInProgress() -> boolean_t](cgdisplayfadeoperationinprogress().md)
  Returns a Boolean value indicating whether a fade operation is currently in progress.
- [func CGDisplayGammaTableCapacity(CGDirectDisplayID) -> UInt32](cgdisplaygammatablecapacity(_:).md)
  Returns the capacity, or number of entries, in the gamma table for a display.
- [func CGDisplayGetDrawingContext(CGDirectDisplayID) -> CGContext?](cgdisplaygetdrawingcontext(_:).md)
  Returns a graphics context suitable for drawing to a captured display.
- [func CGDisplayHideCursor(CGDirectDisplayID) -> CGError](cgdisplayhidecursor(_:).md)
  Hides the mouse cursor, and increments the hide cursor count.
- [func CGDisplayIDToOpenGLDisplayMask(CGDirectDisplayID) -> CGOpenGLDisplayMask](cgdisplayidtoopengldisplaymask(_:).md)
  Maps a display ID to an OpenGL display mask.
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
- [func CGDisplayIsCaptured(CGDirectDisplayID) -> boolean_t](cgdisplayiscaptured(_:).md)
  Returns a Boolean value indicating whether a display is captured.
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
- [var pixelEncoding: CFString?](cgdisplaymode/pixelencoding.md)
  Returns the pixel encoding of the specified display mode.
- [var height: Int](cgdisplaymode/height.md)
  Returns the height of the specified display mode.
- [var ioDisplayModeID: Int32](cgdisplaymode/iodisplaymodeid.md)
  Returns the I/O Kit display mode ID of the specified display mode.
- [var ioFlags: UInt32](cgdisplaymode/ioflags.md)
  Returns the I/O Kit flags of the specified display mode.
- [var pixelWidth: Int](cgdisplaymode/pixelwidth.md)
- [var refreshRate: Double](cgdisplaymode/refreshrate.md)
  Returns the refresh rate of the specified display mode.
- [class var typeID: CFTypeID](cgdisplaymode/typeid.md)
  Returns the type identifier of Quartz display modes.
- [var width: Int](cgdisplaymode/width.md)
  Returns the width of the specified display mode.
- [func isUsableForDesktopGUI() -> Bool](cgdisplaymode/isusablefordesktopgui.md)
  Returns a Boolean value indicating whether the specified display mode is usable for a desktop graphical user interface.
- [func CGDisplayModelNumber(CGDirectDisplayID) -> UInt32](cgdisplaymodelnumber(_:).md)
  Returns the model number of a display monitor.
- [func CGDisplayMoveCursorToPoint(CGDirectDisplayID, CGPoint) -> CGError](cgdisplaymovecursortopoint(_:_:).md)
  Moves the mouse cursor to a specified point relative to the upper-left corner of the display.
- [func CGDisplayPixelsHigh(CGDirectDisplayID) -> Int](cgdisplaypixelshigh(_:).md)
  Returns the display height in pixel units.
- [func CGDisplayPixelsWide(CGDirectDisplayID) -> Int](cgdisplaypixelswide(_:).md)
  Returns the display width in pixel units.
- [func CGDisplayPrimaryDisplay(CGDirectDisplayID) -> CGDirectDisplayID](cgdisplayprimarydisplay(_:).md)
  Returns the primary display in a hardware mirroring set.
- [func CGDisplayRegisterReconfigurationCallback(CGDisplayReconfigurationCallBack?, UnsafeMutableRawPointer?) -> CGError](cgdisplayregisterreconfigurationcallback(_:_:).md)
  Registers a callback function to be invoked whenever a local display is reconfigured.
- [func CGDisplayRelease(CGDirectDisplayID) -> CGError](cgdisplayrelease(_:).md)
  Releases a captured display.
- [func CGDisplayRemoveReconfigurationCallback(CGDisplayReconfigurationCallBack?, UnsafeMutableRawPointer?) -> CGError](cgdisplayremovereconfigurationcallback(_:_:).md)
  Removes the registration of a callback function that’s invoked whenever a local display is reconfigured.
- [func CGDisplayRestoreColorSyncSettings()](cgdisplayrestorecolorsyncsettings().md)
  Restores the gamma tables to the values in the user’s ColorSync display profile.
- [func CGDisplayRotation(CGDirectDisplayID) -> Double](cgdisplayrotation(_:).md)
  Returns the rotation angle of a display in degrees.
- [func CGDisplayScreenSize(CGDirectDisplayID) -> CGSize](cgdisplayscreensize(_:).md)
  Returns the width and height of a display in millimeters.
- [func CGDisplaySerialNumber(CGDirectDisplayID) -> UInt32](cgdisplayserialnumber(_:).md)
  Returns the serial number of a display monitor.
- [func CGDisplaySetDisplayMode(CGDirectDisplayID, CGDisplayMode?, CFDictionary?) -> CGError](cgdisplaysetdisplaymode(_:_:_:).md)
  Switches a display to a different mode.
- [func CGDisplaySetStereoOperation(CGDirectDisplayID, boolean_t, boolean_t, CGConfigureOption) -> CGError](cgdisplaysetstereooperation(_:_:_:_:).md)
  Immediately enables or disables stereo operation for a display.
- [func CGDisplayShowCursor(CGDirectDisplayID) -> CGError](cgdisplayshowcursor(_:).md)
  Decrements the hide cursor count, and shows the mouse cursor if the count is `0`.
- [init?(display: CGDirectDisplayID, outputWidth: Int, outputHeight: Int, pixelFormat: Int32, properties: CFDictionary?, handler: CGDisplayStreamFrameAvailableHandler?)](cgdisplaystream/init(display:outputwidth:outputheight:pixelformat:properties:handler:).md)
  Creates a new display stream to be used with a `CFRunloop`.
- [init?(dispatchQueueDisplay: CGDirectDisplayID, outputWidth: Int, outputHeight: Int, pixelFormat: Int32, properties: CFDictionary?, queue: dispatch_queue_t, handler: CGDisplayStreamFrameAvailableHandler?)](cgdisplaystream/init(dispatchqueuedisplay:outputwidth:outputheight:pixelformat:properties:queue:handler:).md)
  Creates a new display stream whose updates are delivered to a dispatch queue.
- [var runLoopSource: CFRunLoopSource?](cgdisplaystream/runloopsource.md)
  Gets the run loop source for a display stream.
- [func start() -> CGError](cgdisplaystream/start.md)
  Tells a stream to start sending updates.
- [func stop() -> CGError](cgdisplaystream/stop.md)
  Tells a stream to stop sending updates.
- [init?(mergedUpdateFirstUpdate: CGDisplayStreamUpdate?, secondUpdate: CGDisplayStreamUpdate?)](cgdisplaystreamupdate/init(mergedupdatefirstupdate:secondupdate:).md)
  Combines two updates into a new update that includes the metadata for both source updates.
- [var dropCount: Int](cgdisplaystreamupdate/dropcount.md)
  Returns the number of frames that have been dropped since the last call to your update handler.
- [func getMovedRectsDelta(dx: UnsafeMutablePointer<CGFloat>, dy: UnsafeMutablePointer<CGFloat>)](cgdisplaystreamupdate/getmovedrectsdelta(dx:dy:).md)
  Return the movement delta values for a single update.
- [func getRects(CGDisplayStreamUpdateRectType, rectCount: UnsafeMutablePointer<Int>) -> UnsafePointer<CGRect>?](cgdisplaystreamupdate/getrects(_:rectcount:).md)
  Returns an array of rectangles that describe where the frame has changed since the previous frame.
- [class var typeID: CFTypeID](cgdisplaystreamupdate/typeid.md)
  Returns the type identifier of a Quartz display stream update.
- [func CGDisplaySwitchToMode(CGDirectDisplayID, CFDictionary?) -> CGError](cgdisplayswitchtomode(_:_:).md)
  Switches a display to a different mode.
- [func CGDisplayUnitNumber(CGDirectDisplayID) -> UInt32](cgdisplayunitnumber(_:).md)
  Returns the logical unit number of a display.
- [func CGDisplayUsesOpenGLAcceleration(CGDirectDisplayID) -> boolean_t](cgdisplayusesopenglacceleration(_:).md)
  Returns a Boolean value indicating whether Quartz is using OpenGL-based window acceleration (Quartz Extreme) to render in a display.
- [func CGDisplayVendorNumber(CGDirectDisplayID) -> UInt32](cgdisplayvendornumber(_:).md)
  Returns the vendor number of the specified display’s monitor.
- [func CGEnableEventStateCombining(boolean_t) -> CGError](cgenableeventstatecombining(_:).md)
  Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event.
- [init?(source: CGEventSource?)](cgevent/init(source:).md)
  Returns a new Quartz event.
- [func copy() -> CGEvent?](cgevent/copy.md)
  Returns a copy of an existing Quartz event.
- [init?(withDataAllocator: CFAllocator?, data: CFData?)](cgevent/init(withdataallocator:data:).md)
  Returns a Quartz event created from a flattened data representation of the event.
- [init?(keyboardEventSource: CGEventSource?, virtualKey: CGKeyCode, keyDown: Bool)](cgevent/init(keyboardeventsource:virtualkey:keydown:).md)
  Returns a new Quartz keyboard event.
- [init?(mouseEventSource: CGEventSource?, mouseType: CGEventType, mouseCursorPosition: CGPoint, mouseButton: CGMouseButton)](cgevent/init(mouseeventsource:mousetype:mousecursorposition:mousebutton:).md)
  Returns a new Quartz mouse event.
- [init?(event: CGEvent?)](cgeventsource/init(event:).md)
  Returns a Quartz event source created from an existing Quartz event.
- [func getDoubleValueField(CGEventField) -> Double](cgevent/getdoublevaluefield(_:).md)
  Returns the floating-point value of a field in a Quartz event.
- [var flags: CGEventFlags](cgevent/flags.md)
  Returns the event flags of a Quartz event.
- [func getIntegerValueField(CGEventField) -> Int64](cgevent/getintegervaluefield(_:).md)
  Returns the integer value of a field in a Quartz event.
- [var location: CGPoint](cgevent/location.md)
  Returns the location of a Quartz mouse event.
- [var timestamp: CGEventTimestamp](cgevent/timestamp.md)
  Returns the timestamp of a Quartz event.
- [var type: CGEventType](cgevent/type.md)
  Returns the event type of a Quartz event (left mouse down, for example).
- [class var typeID: CFTypeID](cgevent/typeid.md)
  Returns the type identifier for the opaque type `CGEventRef`.
- [var unflippedLocation: CGPoint](cgevent/unflippedlocation.md)
  Returns the location of a Quartz mouse event.
- [func keyboardGetUnicodeString(maxStringLength: Int, actualStringLength: UnsafeMutablePointer<Int>?, unicodeString: UnsafeMutablePointer<UniChar>?)](cgevent/keyboardgetunicodestring(maxstringlength:actualstringlength:unicodestring:).md)
  Returns the Unicode string associated with a Quartz keyboard event.
- [func keyboardSetUnicodeString(stringLength: Int, unicodeString: UnsafePointer<UniChar>?)](cgevent/keyboardsetunicodestring(stringlength:unicodestring:).md)
  Sets the Unicode string associated with a Quartz keyboard event.
- [func post(tap: CGEventTapLocation)](cgevent/post(tap:).md)
  Posts a Quartz event into the event stream at a specified location.
- [func postToPSN(processSerialNumber: UnsafeMutableRawPointer?)](cgevent/posttopsn(processserialnumber:).md)
  Posts a Quartz event into the event stream for a specific application.
- [func postToPid(pid_t)](cgevent/posttopid(_:).md)
- [func setDoubleValueField(CGEventField, value: Double)](cgevent/setdoublevaluefield(_:value:).md)
  Sets the floating-point value of a field in a Quartz event.
- [func setIntegerValueField(CGEventField, value: Int64)](cgevent/setintegervaluefield(_:value:).md)
  Sets the integer value of a field in a Quartz event.
- [func setSource(CGEventSource?)](cgevent/setsource(_:).md)
  Sets the event source of a Quartz event.
- [class func buttonState(CGEventSourceStateID, button: CGMouseButton) -> Bool](cgeventsource/buttonstate(_:button:).md)
  Returns a Boolean value indicating the current button state of a Quartz event source.
- [class func counterForEventType(CGEventSourceStateID, eventType: CGEventType) -> UInt32](cgeventsource/counterforeventtype(_:eventtype:).md)
  Returns a count of events of a given type seen since the window server started.
- [init?(stateID: CGEventSourceStateID)](cgeventsource/init(stateid:).md)
  Returns a Quartz event source created with a specified source state.
- [class func flagsState(CGEventSourceStateID) -> CGEventFlags](cgeventsource/flagsstate(_:).md)
  Returns the current flags of a Quartz event source.
- [var keyboardType: CGEventSourceKeyboardType](cgeventsource/keyboardtype.md)
  Returns the keyboard type to be used with a Quartz event source.
- [func getLocalEventsFilterDuringSuppressionState(CGEventSuppressionState) -> CGEventFilterMask](cgeventsource/getlocaleventsfilterduringsuppressionstate(_:).md)
  Returns the mask that indicates which classes of local hardware events are enabled during event suppression.
- [var pixelsPerLine: Double](cgeventsource/pixelsperline.md)
  Gets the scale of pixels per line in a scrolling event source.
- [var sourceStateID: CGEventSourceStateID](cgeventsource/sourcestateid.md)
  Returns the source state associated with a Quartz event source.
- [class var typeID: CFTypeID](cgeventsource/typeid.md)
  Returns the type identifier for the opaque type `CGEventSourceRef`.
- [var userData: Int64](cgeventsource/userdata.md)
  Returns the 64-bit user-specified data for a Quartz event source.
- [class func keyState(CGEventSourceStateID, key: CGKeyCode) -> Bool](cgeventsource/keystate(_:key:).md)
  Returns a Boolean value indicating the current keyboard state of a Quartz event source.
- [class func secondsSinceLastEventType(CGEventSourceStateID, eventType: CGEventType) -> CFTimeInterval](cgeventsource/secondssincelasteventtype(_:eventtype:).md)
  Returns the elapsed time since the last event for a Quartz event source.
- [func setLocalEventsFilterDuringSuppressionState(CGEventFilterMask, state: CGEventSuppressionState)](cgeventsource/setlocaleventsfilterduringsuppressionstate(_:state:).md)
  Sets the mask that indicates which classes of local hardware events are enabled during event suppression.
- [class func tapCreate(tap: CGEventTapLocation, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](cgevent/tapcreate(tap:place:options:eventsofinterest:callback:userinfo:).md)
  Creates an event tap.
- [class func tapCreateForPSN(processSerialNumber: UnsafeMutableRawPointer, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](cgevent/tapcreateforpsn(processserialnumber:place:options:eventsofinterest:callback:userinfo:).md)
  Creates an event tap for a specified process.
- [class func tapCreateForPid(pid: pid_t, place: CGEventTapPlacement, options: CGEventTapOptions, eventsOfInterest: CGEventMask, callback: CGEventTapCallBack, userInfo: UnsafeMutableRawPointer?) -> CFMachPort?](cgevent/tapcreateforpid(pid:place:options:eventsofinterest:callback:userinfo:).md)
- [class func tapEnable(tap: CFMachPort, enable: Bool)](cgevent/tapenable(tap:enable:).md)
  Enables or disables an event tap.
- [class func tapIsEnabled(tap: CFMachPort) -> Bool](cgevent/tapisenabled(tap:).md)
  Returns a Boolean value indicating whether an event tap is enabled.
- [func tapPostEvent(CGEventTapProxy?)](cgevent/tappostevent(_:).md)
  Posts a Quartz event from an event tap into the event stream.
- [func CGGetActiveDisplayList(UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetactivedisplaylist(_:_:_:).md)
  Provides a list of displays that are active for drawing.
- [func CGGetDisplayTransferByFormula(CGDirectDisplayID, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?) -> CGError](cggetdisplaytransferbyformula(_:_:_:_:_:_:_:_:_:_:).md)
  Gets the coefficients of the gamma transfer formula for a display.
- [func CGGetDisplayTransferByTable(CGDirectDisplayID, UInt32, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<CGGammaValue>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetdisplaytransferbytable(_:_:_:_:_:_:).md)
  Gets the values in the RGB gamma tables for a display.
- [func CGGetDisplaysWithOpenGLDisplayMask(CGOpenGLDisplayMask, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetdisplayswithopengldisplaymask(_:_:_:_:).md)
  Provides a list of displays that corresponds to the bits set in an OpenGL display mask.
- [func CGGetDisplaysWithPoint(CGPoint, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetdisplayswithpoint(_:_:_:_:).md)
  Provides a list of online displays with bounds that include the specified point.
- [func CGGetDisplaysWithRect(CGRect, UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetdisplayswithrect(_:_:_:_:).md)
  Gets a list of online displays with bounds that intersect the specified rectangle.
- [func CGGetEventTapList(UInt32, UnsafeMutablePointer<CGEventTapInformation>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggeteventtaplist(_:_:_:).md)
  Gets a list of currently installed event taps.
- [func CGGetLastMouseDelta() -> (x: Int32, y: Int32)](cggetlastmousedelta().md)
  Reports the change in mouse position since the last mouse movement event received by the application.
- [func CGGetOnlineDisplayList(UInt32, UnsafeMutablePointer<CGDirectDisplayID>?, UnsafeMutablePointer<UInt32>?) -> CGError](cggetonlinedisplaylist(_:_:_:).md)
  Provides a list of displays that are online (active, mirrored, or sleeping).
- [var utType: CFString?](cgimage/uttype.md)
  The Universal Type Identifier for the image.
- [func CGInhibitLocalEvents(boolean_t) -> CGError](cginhibitlocalevents(_:).md)
  Turns off local hardware events in the current session.
- [func CGMainDisplayID() -> CGDirectDisplayID](cgmaindisplayid().md)
  Returns the display ID of the main display.
- [func CGOpenGLDisplayMaskToDisplayID(CGOpenGLDisplayMask) -> CGDirectDisplayID](cgopengldisplaymasktodisplayid(_:).md)
  Maps an OpenGL display mask to a display ID.
- [func CGPointEqualToPoint(CGPoint, CGPoint) -> Bool](cgpointequaltopoint(_:_:).md)
  Returns whether two points are equal.
- [func CGPostKeyboardEvent(CGCharCode, CGKeyCode, boolean_t) -> CGError](cgpostkeyboardevent(_:_:_:).md)
  Synthesizes a low-level keyboard event on the local machine.
- [func CGRegisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?) -> CGError](cgregisterscreenrefreshcallback(_:_:).md)
  Registers a callback function to be invoked when local displays are refreshed or modified.
- [func CGReleaseAllDisplays() -> CGError](cgreleasealldisplays().md)
  Releases all captured displays.
- [func CGReleaseDisplayFadeReservation(CGDisplayFadeReservationToken) -> CGError](cgreleasedisplayfadereservation(_:).md)
  Releases a display fade reservation, and unfades the display if needed.
- [func CGReleaseScreenRefreshRects(UnsafeMutablePointer<CGRect>?)](cgreleasescreenrefreshrects(_:).md)
  Deallocates a list of rectangles that represent changed areas on local displays.
- [func CGRestorePermanentDisplayConfiguration()](cgrestorepermanentdisplayconfiguration().md)
  Restores the permanent display configuration settings for the current user.
- [func CGScreenRegisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?) -> CGError](cgscreenregistermovecallback(_:_:).md)
  Registers a callback function to be invoked when an area of the display is moved.
- [func CGScreenUnregisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?)](cgscreenunregistermovecallback(_:_:).md)
  Removes a previously registered callback function invoked when an area of the display is moved.
- [func CGSessionCopyCurrentDictionary() -> CFDictionary?](cgsessioncopycurrentdictionary().md)
  Returns information about the caller’s window server session.
- [func CGSetDisplayTransferByByteTable(CGDirectDisplayID, UInt32, UnsafePointer<UInt8>, UnsafePointer<UInt8>, UnsafePointer<UInt8>) -> CGError](cgsetdisplaytransferbybytetable(_:_:_:_:_:).md)
  Sets the byte values in the 8-bit RGB gamma tables for a display.
- [func CGSetDisplayTransferByFormula(CGDirectDisplayID, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue, CGGammaValue) -> CGError](cgsetdisplaytransferbyformula(_:_:_:_:_:_:_:_:_:_:).md)
  Sets the gamma function for a display by specifying the coefficients of the gamma transfer formula.
- [func CGSetDisplayTransferByTable(CGDirectDisplayID, UInt32, UnsafePointer<CGGammaValue>?, UnsafePointer<CGGammaValue>?, UnsafePointer<CGGammaValue>?) -> CGError](cgsetdisplaytransferbytable(_:_:_:_:_:).md)
  Sets the color gamma function for a display by specifying the values in the RGB gamma tables.
- [func CGSetLocalEventsFilterDuringSuppressionState(CGEventFilterMask, CGEventSuppressionState) -> CGError](cgsetlocaleventsfilterduringsuppressionstate(_:_:).md)
  Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted.
- [func CGSetLocalEventsSuppressionInterval(CFTimeInterval) -> CGError](cgsetlocaleventssuppressioninterval(_:).md)
  Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event.
- [func CGShieldingWindowID(CGDirectDisplayID) -> CGWindowID](cgshieldingwindowid(_:).md)
  Returns the window ID of the shield window for a captured display.
- [func CGShieldingWindowLevel() -> CGWindowLevel](cgshieldingwindowlevel().md)
  Returns the window level of the shield window for a captured display.
- [func CGSizeEqualToSize(CGSize, CGSize) -> Bool](cgsizeequaltosize(_:_:).md)
  Returns whether two sizes are equal.
- [func CGUnregisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?)](cgunregisterscreenrefreshcallback(_:_:).md)
  Removes a previously registered callback function invoked when local displays are refreshed or modified.
- [func CGWaitForScreenRefreshRects(UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<UInt32>?) -> CGError](cgwaitforscreenrefreshrects(_:_:).md)
  Waits for screen refresh operations.
- [func CGWaitForScreenUpdateRects(CGScreenUpdateOperation, UnsafeMutablePointer<CGScreenUpdateOperation>?, UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<CGScreenUpdateMoveDelta>?) -> CGError](cgwaitforscreenupdaterects(_:_:_:_:_:).md)
  Waits for screen update operations.
- [func CGWarpMouseCursorPosition(CGPoint) -> CGError](cgwarpmousecursorposition(_:).md)
  Moves the mouse cursor without generating events.
- [func CGWindowLevelForKey(CGWindowLevelKey) -> CGWindowLevel](cgwindowlevelforkey(_:).md)
  Returns the window level that corresponds to one of the standard window types.
- [func CGWindowListCopyWindowInfo(CGWindowListOption, CGWindowID) -> CFArray?](cgwindowlistcopywindowinfo(_:_:).md)
  Generates and returns information about the selected windows in the current user session.
- [func CGWindowListCreateDescriptionFromArray(CFArray?) -> CFArray?](cgwindowlistcreatedescriptionfromarray(_:).md)
  Generates and returns information about windows with the specified window IDs.
- [func CGWindowListCreateImage(CGRect, CGWindowListOption, CGWindowID, CGWindowImageOption) -> CGImage?](cgwindowlistcreateimage(_:_:_:_:).md)
  Returns a composite image based on a dynamically generated list of windows.
- [init?(windowListFromArrayScreenBounds: CGRect, windowArray: CFArray, imageOption: CGWindowImageOption)](cgimage/init(windowlistfromarrayscreenbounds:windowarray:imageoption:).md)
  Returns a composite image of the specified windows.
- [func CGWindowServerCFMachPort() -> CFMachPort?](cgwindowservercfmachport().md)
  Returns a Core Foundation Mach port (CFMachPort) that corresponds to the macOS window server.
- [func CGWindowServerCreateServerPort() -> CFMachPort?](cgwindowservercreateserverport().md)
- [func acos(CGFloat) -> CGFloat](acos(_:).md)
- [func acosh(CGFloat) -> CGFloat](acosh(_:).md)
- [func asin(CGFloat) -> CGFloat](asin(_:).md)
- [func asinh(CGFloat) -> CGFloat](asinh(_:).md)
- [func atan(CGFloat) -> CGFloat](atan(_:).md)
- [func atan2(CGFloat, CGFloat) -> CGFloat](atan2(_:_:).md)
- [func atanh(CGFloat) -> CGFloat](atanh(_:).md)
- [func cbrt(CGFloat) -> CGFloat](cbrt(_:).md)
- [func copysign(CGFloat, CGFloat) -> CGFloat](copysign(_:_:).md)
- [func cos(CGFloat) -> CGFloat](cos(_:).md)
- [func cosh(CGFloat) -> CGFloat](cosh(_:).md)
- [func erf(CGFloat) -> CGFloat](erf(_:).md)
- [func erfc(CGFloat) -> CGFloat](erfc(_:).md)
- [func exp(CGFloat) -> CGFloat](exp(_:).md)
- [func exp2(CGFloat) -> CGFloat](exp2(_:).md)
- [func expm1(CGFloat) -> CGFloat](expm1(_:).md)
- [func fdim(CGFloat, CGFloat) -> CGFloat](fdim(_:_:).md)
- [func fmax(CGFloat, CGFloat) -> CGFloat](fmax(_:_:).md)
- [func fmin(CGFloat, CGFloat) -> CGFloat](fmin(_:_:).md)
- [func hypot(CGFloat, CGFloat) -> CGFloat](hypot(_:_:).md)
- [func ilogb(CGFloat) -> Int](ilogb(_:).md)
- [func CGColorSpaceCreateLinearized(CGColorSpace) -> CGColorSpace?](cgcolorspacecreatelinearized(_:).md)
- [init?(src: CGColorSpace, dst: CGColorSpace)](cgcolorconversioninfo/init(src:dst:).md)
  Creates a conversion between two specified color spaces.
- [func j0(CGFloat) -> CGFloat](j0(_:).md)
- [func j1(CGFloat) -> CGFloat](j1(_:).md)
- [func jn(Int, CGFloat) -> CGFloat](jn(_:_:).md)
- [func ldexp(CGFloat, Int) -> CGFloat](ldexp(_:_:).md)
- [func lgamma(CGFloat) -> (CGFloat, Int)](lgamma(_:).md)
- [func log(CGFloat) -> CGFloat](log(_:).md)
- [func log10(CGFloat) -> CGFloat](log10(_:).md)
- [func log1p(CGFloat) -> CGFloat](log1p(_:).md)
- [func log2(CGFloat) -> CGFloat](log2(_:).md)
- [func logb(CGFloat) -> CGFloat](logb(_:).md)
- [func nan(String) -> CGFloat](nan(_:).md)
- [func nearbyint(CGFloat) -> CGFloat](nearbyint(_:).md)
- [func nextafter(CGFloat, CGFloat) -> CGFloat](nextafter(_:_:).md)
- [func pow(CGFloat, CGFloat) -> CGFloat](pow(_:_:).md)
- [func remquo(CGFloat, CGFloat) -> (CGFloat, Int)](remquo(_:_:).md)
- [func rint(CGFloat) -> CGFloat](rint(_:).md)
- [func sin(CGFloat) -> CGFloat](sin(_:).md)
- [func sinh(CGFloat) -> CGFloat](sinh(_:).md)
- [func tan(CGFloat) -> CGFloat](tan(_:).md)
- [func tanh(CGFloat) -> CGFloat](tanh(_:).md)
- [func tgamma(CGFloat) -> CGFloat](tgamma(_:).md)
- [var localEventsSuppressionInterval: CFTimeInterval](cgeventsource/localeventssuppressioninterval.md)
  Returns the interval that local hardware events may be suppressed following the posting of a Quartz event.
- [var pixelHeight: Int](cgdisplaymode/pixelheight.md)
- [class var typeID: CFTypeID](cgdisplaystream/typeid.md)
  Returns the type identifier of a Quartz display stream.
- [class var typeID: CFTypeID](cgcolorconversioninfo/typeid.md)
  Returns the Core Foundation type identifier for a color conversion info data type.
- [func y0(CGFloat) -> CGFloat](y0(_:).md)
- [func y1(CGFloat) -> CGFloat](y1(_:).md)
- [func yn(Int, CGFloat) -> CGFloat](yn(_:_:).md)
- [func CGAffineTransformMake(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGAffineTransform](cgaffinetransformmake(_:_:_:_:_:_:).md)
  Returns an affine transformation matrix constructed from values you provide.
- [func CGColorSpaceCopyBaseColorSpace(CGColorSpace) -> CGColorSpace](cgcolorspacecopybasecolorspace(_:).md)
- [func CGColorSpaceCreateCopyWithStandardRange(CGColorSpace) -> CGColorSpace](cgcolorspacecreatecopywithstandardrange(_:).md)
- [func CGColorSpaceCreateExtended(CGColorSpace) -> CGColorSpace?](cgcolorspacecreateextended(_:).md)
- [func CGColorSpaceCreateExtendedLinearized(CGColorSpace) -> CGColorSpace?](cgcolorspacecreateextendedlinearized(_:).md)
- [func CGColorSpaceCreateWithColorSyncProfile(ColorSyncProfile?, CFDictionary?) -> CGColorSpace?](cgcolorspacecreatewithcolorsyncprofile(_:_:).md)
- [func CGColorSpaceIsHLGBased(CGColorSpace) -> Bool](cgcolorspaceishlgbased(_:).md)
- [func CGColorSpaceIsPQBased(CGColorSpace) -> Bool](cgcolorspaceispqbased(_:).md)
- [func CGColorSpaceUsesITUR_2100TF(CGColorSpace) -> Bool](cgcolorspaceusesitur_2100tf(_:).md)
- [func CGContextDrawConicGradient(CGContext, CGGradient?, CGPoint, CGFloat)](cgcontextdrawconicgradient(_:_:_:_:).md)
- [func CGContextGetEDRTargetHeadroom(CGContext) -> Float](cgcontextgetedrtargetheadroom(_:).md)
- [func CGConvertColorDataWithFormat(Int, Int, UnsafeMutableRawPointer!, CGColorDataFormat, UnsafeMutableRawPointer!, CGColorDataFormat, CFDictionary!) -> Bool](cgconvertcolordatawithformat(_:_:_:_:_:_:_:).md)
- [func CGEnableEventStateCombining(boolean_t) -> CGError](cgenableeventstatecombining(_:).md)
  Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event.
- [func CGErrorSetCallback(CGErrorCallback!)](cgerrorsetcallback(_:).md)
- [func CGImageCreateCopyWithContentHeadroom(Float, CGImage) -> CGImage?](cgimagecreatecopywithcontentheadroom(_:_:).md)
- [func CGInhibitLocalEvents(boolean_t) -> CGError](cginhibitlocalevents(_:).md)
  Turns off local hardware events in the current session.
- [func CGPDFArrayApplyBlock(CGPDFArrayRef, CGPDFArrayApplierBlock, UnsafeMutableRawPointer?)](cgpdfarrayapplyblock(_:_:_:).md)
- [func CGPDFContextBeginTag(CGContext, CGPDFTagType, CFDictionary)](cgpdfcontextbegintag(_:_:_:).md)
- [func CGPDFContextEndTag(CGContext)](cgpdfcontextendtag(_:).md)
- [func CGPDFContextSetIDTree(CGContext, CGPDFDictionaryRef)](cgpdfcontextsetidtree(_:_:).md)
- [func CGPDFContextSetOutline(CGContext, CFDictionary?)](cgpdfcontextsetoutline(_:_:).md)
- [func CGPDFContextSetPageTagStructureTree(CGContext, CFDictionary)](cgpdfcontextsetpagetagstructuretree(_:_:).md)
- [func CGPDFContextSetParentTree(CGContext, CGPDFDictionaryRef)](cgpdfcontextsetparenttree(_:_:).md)
- [func CGPDFDictionaryApplyBlock(CGPDFDictionaryRef, CGPDFDictionaryApplierBlock, UnsafeMutableRawPointer?)](cgpdfdictionaryapplyblock(_:_:_:).md)
- [func CGPDFScannerStop(CGPDFScannerRef)](cgpdfscannerstop(_:).md)
- [func CGPointMake(CGFloat, CGFloat) -> CGPoint](cgpointmake(_:_:).md)
  Returns a point with the specified coordinates.
- [func CGPointMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGPoint>) -> Bool](cgpointmakewithdictionaryrepresentation(_:_:).md)
  Fills in a point using the contents of the specified dictionary.
- [func CGPostKeyboardEvent(CGCharCode, CGKeyCode, boolean_t) -> CGError](cgpostkeyboardevent(_:_:_:).md)
  Synthesizes a low-level keyboard event on the local machine.
- [func CGPreflightListenEventAccess() -> Bool](cgpreflightlisteneventaccess().md)
- [func CGPreflightPostEventAccess() -> Bool](cgpreflightposteventaccess().md)
- [func CGPreflightScreenCaptureAccess() -> Bool](cgpreflightscreencaptureaccess().md)
- [func CGRectMake(CGFloat, CGFloat, CGFloat, CGFloat) -> CGRect](cgrectmake(_:_:_:_:).md)
  Returns a rectangle with the specified coordinate and size values.
- [func CGRectMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGRect>) -> Bool](cgrectmakewithdictionaryrepresentation(_:_:).md)
  Fills in a rectangle using the contents of the specified dictionary.
- [func CGRegisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?) -> CGError](cgregisterscreenrefreshcallback(_:_:).md)
  Registers a callback function to be invoked when local displays are refreshed or modified.
- [func CGReleaseScreenRefreshRects(UnsafeMutablePointer<CGRect>?)](cgreleasescreenrefreshrects(_:).md)
  Deallocates a list of rectangles that represent changed areas on local displays.
- [func CGRequestListenEventAccess() -> Bool](cgrequestlisteneventaccess().md)
- [func CGRequestPostEventAccess() -> Bool](cgrequestposteventaccess().md)
- [func CGRequestScreenCaptureAccess() -> Bool](cgrequestscreencaptureaccess().md)
- [func CGScreenRegisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?) -> CGError](cgscreenregistermovecallback(_:_:).md)
  Registers a callback function to be invoked when an area of the display is moved.
- [func CGScreenUnregisterMoveCallback(CGScreenUpdateMoveCallback, UnsafeMutableRawPointer?)](cgscreenunregistermovecallback(_:_:).md)
  Removes a previously registered callback function invoked when an area of the display is moved.
- [func CGSetLocalEventsFilterDuringSuppressionState(CGEventFilterMask, CGEventSuppressionState) -> CGError](cgsetlocaleventsfilterduringsuppressionstate(_:_:).md)
  Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted.
- [func CGSetLocalEventsSuppressionInterval(CFTimeInterval) -> CGError](cgsetlocaleventssuppressioninterval(_:).md)
  Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event.
- [func CGSizeMake(CGFloat, CGFloat) -> CGSize](cgsizemake(_:_:).md)
  Returns a size with the specified dimension values.
- [func CGSizeMakeWithDictionaryRepresentation(CFDictionary, UnsafeMutablePointer<CGSize>) -> Bool](cgsizemakewithdictionaryrepresentation(_:_:).md)
  Fills in a size using the contents of the specified dictionary.
- [func CGUnregisterScreenRefreshCallback(CGScreenRefreshCallback, UnsafeMutableRawPointer?)](cgunregisterscreenrefreshcallback(_:_:).md)
  Removes a previously registered callback function invoked when local displays are refreshed or modified.
- [func CGVectorMake(CGFloat, CGFloat) -> CGVector](cgvectormake(_:_:).md)
  Returns a vector with the specified dimension values.
- [func CGWaitForScreenRefreshRects(UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<UInt32>?) -> CGError](cgwaitforscreenrefreshrects(_:_:).md)
  Waits for screen refresh operations.
- [func CGWaitForScreenUpdateRects(CGScreenUpdateOperation, UnsafeMutablePointer<CGScreenUpdateOperation>?, UnsafeMutablePointer<UnsafeMutablePointer<CGRect>?>?, UnsafeMutablePointer<Int>?, UnsafeMutablePointer<CGScreenUpdateMoveDelta>?) -> CGError](cgwaitforscreenupdaterects(_:_:_:_:_:).md)
  Waits for screen update operations.
- [var accessPermissions: CGPDFAccessPermissions](cgpdfdocument/accesspermissions.md)
- [func applyWithBlock((UnsafePointer<CGPathElement>) -> Void)](cgpath/applywithblock(_:).md)
- [var byteOrderInfo: CGImageByteOrderInfo](cgimage/byteorderinfo.md)
- [var containsImageSpecificToneMappingMetadata: Bool](cgimage/containsimagespecifictonemappingmetadata.md)
- [var contentHeadroom: Float](cgimage/contentheadroom.md)
- [func convert(width: Int, height: Int, to: UnsafeMutableRawPointer, format: CGColorBufferFormat, from: UnsafeRawPointer, format: CGColorBufferFormat, options: CFDictionary?) -> Bool](cgcolorconversioninfo/convert(width:height:to:format:from:format:options:).md)
- [func copyPropertyList() -> CFPropertyList?](cgcolorspace/copypropertylist.md)
  Returns a copy of the color space’s properties.
- [var info: UnsafeMutableRawPointer?](cgdataprovider/info.md)
- [init(genericGrayGamma2_2Gray: CGFloat, alpha: CGFloat)](cgcolor/init(genericgraygamma2_2gray:alpha:).md)
  Creates a color in the Generic gray color space with a gamma ramp of 2.2.
- [init?(headroom: Float, width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](cgimage/init(headroom:width:height:bitspercomponent:bitsperpixel:bytesperrow:space:bitmapinfo:provider:decode:shouldinterpolate:intent:).md)
- [init?(iccData: CFTypeRef)](cgcolorspace/init(iccdata:).md)
  Creates an ICC-based color space using the ICC profile contained in the specified data.
- [init?(optionsSrc: CGColorSpace, dst: CGColorSpace, options: CFDictionary?)](cgcolorconversioninfo/init(optionssrc:dst:options:).md)
- [init?(propertyListPlist: CFPropertyList)](cgcolorspace/init(propertylistplist:).md)
  Creates a color space from a property list.
- [init?(scrollWheelEvent2Source: CGEventSource?, units: CGScrollEventUnit, wheelCount: UInt32, wheel1: Int32, wheel2: Int32, wheel3: Int32)](cgevent/init(scrollwheelevent2source:units:wheelcount:wheel1:wheel2:wheel3:).md)
- [init?(src: CGColorSpace, srcHeadroom: Float, dst: CGColorSpace, dstHeadroom: Float, toneMapping: CGToneMapping, options: CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](cgcolorconversioninfo/init(src:srcheadroom:dst:dstheadroom:tonemapping:options:).md)
- [func isHDR() -> Bool](cgcolorspace/ishdr.md)
- [var name: UnsafePointer<CChar>](cgpdftagtype/name.md)
- [var outline: CFDictionary?](cgpdfdocument/outline.md)
- [var pixelFormatInfo: CGImagePixelFormatInfo](cgimage/pixelformatinfo.md)
- [func resetClip()](cgcontext/resetclip.md)
- [func setEDRTargetHeadroom(Float) -> Bool](cgcontext/setedrtargetheadroom(_:).md)
- [var shouldToneMap: Bool](cgimage/shouldtonemap.md)
- [func CGColorSpaceUsesExtendedRange(CGColorSpace) -> Bool](cgcolorspaceusesextendedrange(_:).md)

## See Also

- [Core Graphics Structures](core-graphics-structures.md)
- [Core Graphics Enumerations](core-graphics-enumerations.md)
- [Core Graphics Constants](core-graphics-constants.md)
- [Core Graphics Data Types](core-graphics-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/core-graphics-functions)*