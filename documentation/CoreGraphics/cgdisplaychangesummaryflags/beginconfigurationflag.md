# beginConfigurationFlag

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Type Property

The display configuration is about to change.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
static var beginConfigurationFlag: CGDisplayChangeSummaryFlags { get }
```

```c
kCGDisplayBeginConfigurationFlag
```

## See Also

### Constants
- [static var movedFlag: CGDisplayChangeSummaryFlags](./movedflag.md)
  The location of the upper-left corner of the display in the global display coordinate space has changed.
- [static var setMainFlag: CGDisplayChangeSummaryFlags](./setmainflag.md)
  The display is now the main display.
- [static var setModeFlag: CGDisplayChangeSummaryFlags](./setmodeflag.md)
  The display mode has changed.
- [static var addFlag: CGDisplayChangeSummaryFlags](./addflag.md)
  The display has been added to the active display list.
- [static var removeFlag: CGDisplayChangeSummaryFlags](./removeflag.md)
  The display has been removed from the active display list.
- [static var enabledFlag: CGDisplayChangeSummaryFlags](./enabledflag.md)
  The display has been enabled.
- [static var disabledFlag: CGDisplayChangeSummaryFlags](./disabledflag.md)
  The display has been disabled.
- [static var mirrorFlag: CGDisplayChangeSummaryFlags](./mirrorflag.md)
  The display is now mirroring another display.
- [static var unMirrorFlag: CGDisplayChangeSummaryFlags](./unmirrorflag.md)
  The display is no longer mirroring another display.
- [static var desktopShapeChangedFlag: CGDisplayChangeSummaryFlags](./desktopshapechangedflag.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdisplaychangesummaryflags/beginconfigurationflag)*