# ShieldAction

**Framework**: Managed Settings  
**Kind**: enum

Constants that describe a user’s action for your extension to handle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+

## Declaration

```swift
enum ShieldAction
```

## Topics

### Responding to primary button actions
- [ShieldAction.primaryButtonPressed](shieldaction/primarybuttonpressed.md)
  The user pressed the top button of the buttons on a shield.
### Responding to secondary button actions
- [ShieldAction.secondaryButtonPressed](shieldaction/secondarybuttonpressed.md)
  The user pressed the optional secondary button underneath the primary button of a shield.
- [ShieldAction.firstSecondarySubmenuItemPressed](shieldaction/firstsecondarysubmenuitempressed.md)
  An action that occurs when someone selects the first item in the secondary button’s submenu.
- [ShieldAction.secondSecondarySubmenuItemPressed](shieldaction/secondsecondarysubmenuitempressed.md)
  An action that occurs when someone selects the second item in the secondary button’s submenu.
- [ShieldAction.thirdSecondarySubmenuItemPressed](shieldaction/thirdsecondarysubmenuitempressed.md)
  An action that occurs when someone selects the third item in the secondary button’s submenu.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [class ShieldActionDelegate](shieldactiondelegate.md)
  A class for an extension that handles shield actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldaction)*