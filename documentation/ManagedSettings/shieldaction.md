# ShieldAction

**Framework**: ManagedSettings  
**Kind**: enum

Constants that describe a user’s action for your extension to handle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum ShieldAction
```

## Topics

### Buttons
- [ShieldAction.primaryButtonPressed](shieldaction/primarybuttonpressed.md)
  The user pressed the top button of the buttons on a shield.
- [ShieldAction.secondaryButtonPressed](shieldaction/secondarybuttonpressed.md)
  The user pressed the optional secondary button underneath the primary button of a shield.
### Enumeration Cases
- [ShieldAction.firstSecondarySubmenuItemPressed](shieldaction/firstsecondarysubmenuitempressed.md)
  The user pressed the first item in the secondary button sub menu
- [ShieldAction.secondSecondarySubmenuItemPressed](shieldaction/secondsecondarysubmenuitempressed.md)
  The user pressed the second item in the secondary button sub menu
- [ShieldAction.thirdSecondarySubmenuItemPressed](shieldaction/thirdsecondarysubmenuitempressed.md)
  The user pressed the third item in the secondary button sub menu

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [enum ShieldActionResponse](shieldactionresponse.md)
  Constants your extension that handles shield actions can use to tell the system how to respond to an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldaction)*