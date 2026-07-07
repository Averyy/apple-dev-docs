# ShieldAction.secondSecondarySubmenuItemPressed

**Framework**: Managed Settings  
**Kind**: case

An action that occurs when someone selects the second item in the secondary button’s submenu.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
case secondSecondarySubmenuItemPressed
```

#### Discussion

The system invokes this callback on your app’s [`ShieldActionDelegate`](shieldactiondelegate.md) for the second item in the submenu when your app defines the [`secondaryButtonSubmenuItems`](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration/secondarybuttonsubmenuitems) array with two or more elements.

## See Also

- [ShieldAction.secondaryButtonPressed](shieldaction/secondarybuttonpressed.md)
  The user pressed the optional secondary button underneath the primary button of a shield.
- [ShieldAction.firstSecondarySubmenuItemPressed](shieldaction/firstsecondarysubmenuitempressed.md)
  An action that occurs when someone selects the first item in the secondary button’s submenu.
- [ShieldAction.thirdSecondarySubmenuItemPressed](shieldaction/thirdsecondarysubmenuitempressed.md)
  An action that occurs when someone selects the third item in the secondary button’s submenu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldaction/secondsecondarysubmenuitempressed)*