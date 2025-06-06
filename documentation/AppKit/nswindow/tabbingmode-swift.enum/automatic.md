# NSWindow.TabbingMode.automatic

**Framework**: AppKit  
**Kind**: case

A window that automatically tabs together based on the user’s tabbing preference.

**Availability**:
- macOS 10.12+

## Declaration

```swift
case automatic
```

#### Discussion

A window with the [`NSWindow.TabbingMode.automatic`](nswindow/tabbingmode-swift.enum/automatic.md) tabbing mode consults the value of [`userTabbingPreference`](nswindow/usertabbingpreference-swift.type.property.md) to decide if it should join a tab group with other windows.

## See Also

- [NSWindow.TabbingMode.disallowed](nswindow/tabbingmode-swift.enum/disallowed.md)
  A window that explicitly does not prefer to tab together with other windows.
- [NSWindow.TabbingMode.preferred](nswindow/tabbingmode-swift.enum/preferred.md)
  A window that explicitly prefers to tab together with other windows with the same tabbing identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/tabbingmode-swift.enum/automatic)*