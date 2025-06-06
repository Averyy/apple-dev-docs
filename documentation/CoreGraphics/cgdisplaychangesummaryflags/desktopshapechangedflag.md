# desktopShapeChangedFlag

**Framework**: Core Graphics  
**Kind**: property

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
static var desktopShapeChangedFlag: CGDisplayChangeSummaryFlags { get }
```

#### Discussion

The shape of the desktop (the union of display areas) has changed.

## See Also

- [static var beginConfigurationFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/beginconfigurationflag.md)
  The display configuration is about to change.
- [static var movedFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/movedflag.md)
  The location of the upper-left corner of the display in the global display coordinate space has changed.
- [static var setMainFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/setmainflag.md)
  The display is now the main display.
- [static var setModeFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/setmodeflag.md)
  The display mode has changed.
- [static var addFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/addflag.md)
  The display has been added to the active display list.
- [static var removeFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/removeflag.md)
  The display has been removed from the active display list.
- [static var enabledFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/enabledflag.md)
  The display has been enabled.
- [static var disabledFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/disabledflag.md)
  The display has been disabled.
- [static var mirrorFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/mirrorflag.md)
  The display is now mirroring another display.
- [static var unMirrorFlag: CGDisplayChangeSummaryFlags](cgdisplaychangesummaryflags/unmirrorflag.md)
  The display is no longer mirroring another display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/desktopshapechangedflag)*