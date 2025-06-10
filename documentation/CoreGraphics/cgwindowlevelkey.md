# CGWindowLevelKey

**Framework**: Core Graphics  
**Kind**: enum

Keys that represent the standard window levels in macOS. Quartz includes these keys to support application frameworks like Cocoa. Applications do not need to use them directly.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
enum CGWindowLevelKey
```

## Topics

### Constants
- [CGWindowLevelKey.baseWindow](cgwindowlevelkey/basewindow.md)
- [CGWindowLevelKey.minimumWindow](cgwindowlevelkey/minimumwindow.md)
- [CGWindowLevelKey.desktopWindow](cgwindowlevelkey/desktopwindow.md)
- [CGWindowLevelKey.backstopMenu](cgwindowlevelkey/backstopmenu.md)
- [CGWindowLevelKey.normalWindow](cgwindowlevelkey/normalwindow.md)
- [CGWindowLevelKey.floatingWindow](cgwindowlevelkey/floatingwindow.md)
- [CGWindowLevelKey.tornOffMenuWindow](cgwindowlevelkey/tornoffmenuwindow.md)
- [CGWindowLevelKey.dockWindow](cgwindowlevelkey/dockwindow.md)
- [CGWindowLevelKey.mainMenuWindow](cgwindowlevelkey/mainmenuwindow.md)
- [CGWindowLevelKey.statusWindow](cgwindowlevelkey/statuswindow.md)
- [CGWindowLevelKey.modalPanelWindow](cgwindowlevelkey/modalpanelwindow.md)
- [CGWindowLevelKey.popUpMenuWindow](cgwindowlevelkey/popupmenuwindow.md)
- [CGWindowLevelKey.draggingWindow](cgwindowlevelkey/draggingwindow.md)
- [CGWindowLevelKey.screenSaverWindow](cgwindowlevelkey/screensaverwindow.md)
- [CGWindowLevelKey.maximumWindow](cgwindowlevelkey/maximumwindow.md)
- [CGWindowLevelKey.overlayWindow](cgwindowlevelkey/overlaywindow.md)
- [CGWindowLevelKey.helpWindow](cgwindowlevelkey/helpwindow.md)
- [CGWindowLevelKey.utilityWindow](cgwindowlevelkey/utilitywindow.md)
- [CGWindowLevelKey.desktopIconWindow](cgwindowlevelkey/desktopiconwindow.md)
- [CGWindowLevelKey.cursorWindow](cgwindowlevelkey/cursorwindow.md)
- [CGWindowLevelKey.assistiveTechHighWindow](cgwindowlevelkey/assistivetechhighwindow.md)
- [CGWindowLevelKey.numberOfWindowLevelKeys](cgwindowlevelkey/numberofwindowlevelkeys.md)
### Initializers
- [init?(rawValue: Int32)](cgwindowlevelkey/init(rawvalue:).md)

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
- [enum CGEventField](cgeventfield.md)
  Constants used as keys to access specialized fields in low-level events.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgwindowlevelkey)*