# CGEventField

**Framework**: Core Graphics  
**Kind**: enum

Constants used as keys to access specialized fields in low-level events.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum CGEventField
```

#### Overview

These constants are used as keys to access certain specialized event fields when using low-level accessor functions such as [`getIntegerValueField(_:)`](cgevent/getintegervaluefield(_:).md), [`setIntegerValueField(_:value:)`](cgevent/setintegervaluefield(_:value:).md), [`getDoubleValueField(_:)`](cgevent/getdoublevaluefield(_:).md), and [`setDoubleValueField(_:value:)`](cgevent/setdoublevaluefield(_:value:).md).

## Topics

### Constants
- [CGEventField.mouseEventNumber](cgeventfield/mouseeventnumber.md)
  Key to access an integer field that contains the mouse button event number. Matching mouse-down and mouse-up events will have the same event number.
- [CGEventField.mouseEventClickState](cgeventfield/mouseeventclickstate.md)
  Key to access an integer field that contains the mouse button click state. A click state of 1 represents a single click. A click state of 2 represents a double-click. A click state of 3 represents a triple-click.
- [CGEventField.mouseEventPressure](cgeventfield/mouseeventpressure.md)
  Key to access a double field that contains the mouse button pressure. The pressure value may range from 0 to 1, with 0 representing the mouse being up. This value is commonly set by tablet pens mimicking a mouse.
- [CGEventField.mouseEventButtonNumber](cgeventfield/mouseeventbuttonnumber.md)
  Key to access an integer field that contains the mouse button number. For information about the possible values, see [`CGMouseButton`](cgmousebutton.md).
- [CGEventField.mouseEventDeltaX](cgeventfield/mouseeventdeltax.md)
  Key to access an integer field that contains the horizontal mouse delta since the last mouse movement event.
- [CGEventField.mouseEventDeltaY](cgeventfield/mouseeventdeltay.md)
  Key to access an integer field that contains the vertical mouse delta since the last mouse movement event.
- [CGEventField.mouseEventInstantMouser](cgeventfield/mouseeventinstantmouser.md)
  Key to access an integer field. The value is non-zero if the event should be ignored by the Inkwell subsystem.
- [CGEventField.mouseEventSubtype](cgeventfield/mouseeventsubtype.md)
  Key to access an integer field that encodes the mouse event subtype as a `kCFNumberIntType`.
- [CGEventField.keyboardEventAutorepeat](cgeventfield/keyboardeventautorepeat.md)
  Key to access an integer field, non-zero when this is an autorepeat of a key-down, and zero otherwise.
- [CGEventField.keyboardEventKeycode](cgeventfield/keyboardeventkeycode.md)
  Key to access an integer field that contains the virtual keycode of the key-down or key-up event.
- [CGEventField.keyboardEventKeyboardType](cgeventfield/keyboardeventkeyboardtype.md)
  Key to access an integer field that contains the keyboard type identifier.
- [CGEventField.scrollWheelEventDeltaAxis1](cgeventfield/scrollwheeleventdeltaaxis1.md)
  Key to access an integer field that contains scrolling data. This field typically contains the change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller.
- [CGEventField.scrollWheelEventDeltaAxis2](cgeventfield/scrollwheeleventdeltaaxis2.md)
  Key to access an integer field that contains scrolling data. This field typically contains the change in horizontal position since the last scrolling event from a Mighty Mouse scroller.
- [CGEventField.scrollWheelEventDeltaAxis3](cgeventfield/scrollwheeleventdeltaaxis3.md)
  This field is not used.
- [CGEventField.scrollWheelEventFixedPtDeltaAxis1](cgeventfield/scrollwheeleventfixedptdeltaaxis1.md)
  Key to access a field that contains scrolling data. The scrolling data represents a line-based or pixel-based change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller. The scrolling data uses a fixed-point 16.16 signed integer format. For example, if the field contains a value of 1.0, the integer 0x00010000 is returned by `CGEventGetIntegerValueField`. If this key is passed to `CGEventGetDoubleValueField`, the fixed-point value is converted to a double value.
- [CGEventField.scrollWheelEventFixedPtDeltaAxis2](cgeventfield/scrollwheeleventfixedptdeltaaxis2.md)
  Key to access a field that contains scrolling data. The scrolling data represents a line-based or pixel-based change in horizontal position since the last scrolling event from a Mighty Mouse scroller. The scrolling data uses a fixed-point 16.16 signed integer format. For example, if the field contains a value of 1.0, the integer 0x00010000 is returned by `CGEventGetIntegerValueField`. If this key is passed to `CGEventGetDoubleValueField`, the fixed-point value is converted to a double value.
- [CGEventField.scrollWheelEventFixedPtDeltaAxis3](cgeventfield/scrollwheeleventfixedptdeltaaxis3.md)
  This field is not used.
- [CGEventField.scrollWheelEventPointDeltaAxis1](cgeventfield/scrollwheeleventpointdeltaaxis1.md)
  Key to access an integer field that contains pixel-based scrolling data. The scrolling data represents the change in vertical position since the last scrolling event from a Mighty Mouse scroller or a single-wheel mouse scroller.
- [CGEventField.scrollWheelEventPointDeltaAxis2](cgeventfield/scrollwheeleventpointdeltaaxis2.md)
  Key to access an integer field that contains pixel-based scrolling data. The scrolling data represents the change in horizontal position since the last scrolling event from a Mighty Mouse scroller.
- [CGEventField.scrollWheelEventPointDeltaAxis3](cgeventfield/scrollwheeleventpointdeltaaxis3.md)
  This field is not used.
- [CGEventField.scrollWheelEventInstantMouser](cgeventfield/scrollwheeleventinstantmouser.md)
  Key to access an integer field that indicates whether the event should be ignored by the Inkwell subsystem. If the value is non-zero, the event should be ignored.
- [CGEventField.tabletEventPointX](cgeventfield/tableteventpointx.md)
  Key to access an integer field that contains the absolute X coordinate in tablet space at full tablet resolution.
- [CGEventField.tabletEventPointY](cgeventfield/tableteventpointy.md)
  Key to access an integer field that contains the absolute Y coordinate in tablet space at full tablet resolution.
- [CGEventField.tabletEventPointZ](cgeventfield/tableteventpointz.md)
  Key to access an integer field that contains the absolute Z coordinate in tablet space at full tablet resolution.
- [CGEventField.tabletEventPointButtons](cgeventfield/tableteventpointbuttons.md)
  Key to access an integer field that contains the tablet button state. Bit 0 is the first button, and a set bit represents a closed or pressed button. Up to 16 buttons are supported.
- [CGEventField.tabletEventPointPressure](cgeventfield/tableteventpointpressure.md)
  Key to access a double field that contains the tablet pen pressure. A value of 0.0 represents no pressure, and 1.0 represents maximum pressure.
- [CGEventField.tabletEventTiltX](cgeventfield/tableteventtiltx.md)
  Key to access a double field that contains the horizontal tablet pen tilt. A value of 0.0 represents no tilt, and 1.0 represents maximum tilt.
- [CGEventField.tabletEventTiltY](cgeventfield/tableteventtilty.md)
  Key to access a double field that contains the vertical tablet pen tilt. A value of 0.0 represents no tilt, and 1.0 represents maximum tilt.
- [CGEventField.tabletEventRotation](cgeventfield/tableteventrotation.md)
  Key to access a double field that contains the tablet pen rotation.
- [CGEventField.tabletEventTangentialPressure](cgeventfield/tableteventtangentialpressure.md)
  Key to access a double field that contains the tangential pressure on the device. A value of 0.0 represents no pressure, and 1.0 represents maximum pressure.
- [CGEventField.tabletEventDeviceID](cgeventfield/tableteventdeviceid.md)
  Key to access an integer field that contains the system-assigned unique device ID.
- [CGEventField.tabletEventVendor1](cgeventfield/tableteventvendor1.md)
  Key to access an integer field that contains a vendor-specified value.
- [CGEventField.tabletEventVendor2](cgeventfield/tableteventvendor2.md)
  Key to access an integer field that contains a vendor-specified value.
- [CGEventField.tabletEventVendor3](cgeventfield/tableteventvendor3.md)
  Key to access an integer field that contains a vendor-specified value.
- [CGEventField.tabletProximityEventVendorID](cgeventfield/tabletproximityeventvendorid.md)
  Key to access an integer field that contains the vendor-defined ID, typically the USB vendor ID.
- [CGEventField.tabletProximityEventTabletID](cgeventfield/tabletproximityeventtabletid.md)
  Key to access an integer field that contains the vendor-defined tablet ID, typically the USB product ID.
- [CGEventField.tabletProximityEventPointerID](cgeventfield/tabletproximityeventpointerid.md)
  Key to access an integer field that contains the vendor-defined ID of the pointing device.
- [CGEventField.tabletProximityEventDeviceID](cgeventfield/tabletproximityeventdeviceid.md)
  Key to access an integer field that contains the system-assigned device ID.
- [CGEventField.tabletProximityEventSystemTabletID](cgeventfield/tabletproximityeventsystemtabletid.md)
  Key to access an integer field that contains the system-assigned unique tablet ID.
- [CGEventField.tabletProximityEventVendorPointerType](cgeventfield/tabletproximityeventvendorpointertype.md)
  Key to access an integer field that contains the vendor-assigned pointer type.
- [CGEventField.tabletProximityEventVendorPointerSerialNumber](cgeventfield/tabletproximityeventvendorpointerserialnumber.md)
  Key to access an integer field that contains the vendor-defined pointer serial number.
- [CGEventField.tabletProximityEventVendorUniqueID](cgeventfield/tabletproximityeventvendoruniqueid.md)
  Key to access an integer field that contains the vendor-defined unique ID.
- [CGEventField.tabletProximityEventCapabilityMask](cgeventfield/tabletproximityeventcapabilitymask.md)
  Key to access an integer field that contains the device capabilities mask.
- [CGEventField.tabletProximityEventPointerType](cgeventfield/tabletproximityeventpointertype.md)
  Key to access an integer field that contains the pointer type.
- [CGEventField.tabletProximityEventEnterProximity](cgeventfield/tabletproximityevententerproximity.md)
  Key to access an integer field that indicates whether the pen is in proximity to the tablet. The value is non-zero if the pen is in proximity to the tablet and zero when leaving the tablet.
- [CGEventField.eventTargetProcessSerialNumber](cgeventfield/eventtargetprocessserialnumber.md)
  Key to access a field that contains the event target process serial number. The value is a 64-bit long word.
- [CGEventField.eventTargetUnixProcessID](cgeventfield/eventtargetunixprocessid.md)
  Key to access a field that contains the event target Unix process ID.
- [CGEventField.eventSourceUnixProcessID](cgeventfield/eventsourceunixprocessid.md)
  Key to access a field that contains the event source Unix process ID.
- [CGEventField.eventSourceUserData](cgeventfield/eventsourceuserdata.md)
  Key to access a field that contains the event source user-supplied data, up to 64 bits.
- [CGEventField.eventSourceUserID](cgeventfield/eventsourceuserid.md)
  Key to access a field that contains the event source Unix effective UID.
- [CGEventField.eventSourceGroupID](cgeventfield/eventsourcegroupid.md)
  Key to access a field that contains the event source Unix effective GID.
- [CGEventField.eventSourceStateID](cgeventfield/eventsourcestateid.md)
  Key to access a field that contains the event source state ID used to create this event.
- [CGEventField.scrollWheelEventIsContinuous](cgeventfield/scrollwheeleventiscontinuous.md)
  Key to access an integer field that indicates whether a scrolling event contains continuous, pixel-based scrolling data. The value is non-zero when the scrolling data is pixel-based and zero when the scrolling data is line-based.
- [CGEventField.mouseEventWindowUnderMousePointer](cgeventfield/mouseeventwindowundermousepointer.md)
- [CGEventField.mouseEventWindowUnderMousePointerThatCanHandleThisEvent](cgeventfield/mouseeventwindowundermousepointerthatcanhandlethisevent.md)
- [CGEventField.scrollWheelEventMomentumPhase](cgeventfield/scrollwheeleventmomentumphase.md)
- [CGEventField.scrollWheelEventScrollCount](cgeventfield/scrollwheeleventscrollcount.md)
- [CGEventField.scrollWheelEventScrollPhase](cgeventfield/scrollwheeleventscrollphase.md)
### Enumeration Cases
- [CGEventField.mouseEventWindowUnderMousePointer](cgeventfield/mouseeventwindowundermousepointer.md)
- [CGEventField.mouseEventWindowUnderMousePointerThatCanHandleThisEvent](cgeventfield/mouseeventwindowundermousepointerthatcanhandlethisevent.md)
- [CGEventField.scrollWheelEventMomentumPhase](cgeventfield/scrollwheeleventmomentumphase.md)
- [CGEventField.scrollWheelEventScrollCount](cgeventfield/scrollwheeleventscrollcount.md)
- [CGEventField.scrollWheelEventScrollPhase](cgeventfield/scrollwheeleventscrollphase.md)
- [CGEventField.eventUnacceleratedPointerMovementX](cgeventfield/eventunacceleratedpointermovementx.md)
- [CGEventField.eventUnacceleratedPointerMovementY](cgeventfield/eventunacceleratedpointermovementy.md)
- [CGEventField.scrollWheelEventAcceleratedDeltaAxis1](cgeventfield/scrollwheeleventaccelerateddeltaaxis1.md)
- [CGEventField.scrollWheelEventAcceleratedDeltaAxis2](cgeventfield/scrollwheeleventaccelerateddeltaaxis2.md)
- [CGEventField.scrollWheelEventMomentumOptionPhase](cgeventfield/scrollwheeleventmomentumoptionphase.md)
- [CGEventField.scrollWheelEventRawDeltaAxis1](cgeventfield/scrollwheeleventrawdeltaaxis1.md)
- [CGEventField.scrollWheelEventRawDeltaAxis2](cgeventfield/scrollwheeleventrawdeltaaxis2.md)
### Initializers
- [init?(rawValue: UInt32)](cgeventfield/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CGCaptureOptions](cgcaptureoptions.md)
  Configuration parameters that are used when capturing displays.
- [enum CGColorConversionInfoTransformType](cgcolorconversioninfotransformtype.md)
  Constants describing how a color conversion uses color spaces.
- [enum CGColorRenderingIntent](cgcolorrenderingintent.md)
  Handling options for colors that are not located within the destination color space of a graphics context.
- [struct CGConfigureOption](cgconfigureoption.md)
  The scope of the changes in a display configuration transaction.
- [struct CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags.md)
  The configuration parameters that are passed to a display reconfiguration callback function.
- [enum CGDisplayStreamFrameStatus](cgdisplaystreamframestatus.md)
  Describes a frame update event.
- [enum CGDisplayStreamUpdateRectType](cgdisplaystreamupdaterecttype.md)
  Use these constants to determine which rectangles your app is interested in.
- [enum CGError](cgerror.md)
  A uniform type for result codes returned by functions in Core Graphics.
- [struct CGEventFilterMask](cgeventfiltermask.md)
  Specify masks for classes of low-level events that can be filtered during event suppression states.
- [struct CGEventFlags](cgeventflags.md)
  Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [enum CGEventMouseSubtype](cgeventmousesubtype.md)
  Constants used with the [`CGEventField.mouseEventSubtype`](cgeventfield/mouseeventsubtype.md) event field.
- [enum CGEventSourceStateID](cgeventsourcestateid.md)
  Constants that specify the possible source states of an event source.
- [enum CGEventSuppressionState](cgeventsuppressionstate.md)
  Specify the event suppression states that can occur after posting an event.
- [enum CGEventTapLocation](cgeventtaplocation.md)
  Constants that specify possible tapping points for events.
- [enum CGEventTapOptions](cgeventtapoptions.md)
  Constants that specify whether a new event tap is an active filter or a passive listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgeventfield)*