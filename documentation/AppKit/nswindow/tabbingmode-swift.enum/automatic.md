# NSWindow.TabbingMode.automatic

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

A window that automatically tabs together based on the user’s tabbing preference.

**Availability**:
- macOS 10.12+

## Declaration

```swift
case automatic
```

```c
NSWindowTabbingModeAutomatic
```

## Discussion

A window with the [`NSWindow.TabbingMode.automatic`](./automatic.md) tabbing mode consults the value of [`userTabbingPreference`](../usertabbingpreference-swift.type.property.md) to decide if it should join a tab group with other windows.

## See Also

### Modes
- [NSWindow.TabbingMode.disallowed](./disallowed.md)
  A window that explicitly does not prefer to tab together with other windows.
- [NSWindow.TabbingMode.preferred](./preferred.md)
  A window that explicitly prefers to tab together with other windows with the same tabbing identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/tabbingmode-swift.enum/automatic)*