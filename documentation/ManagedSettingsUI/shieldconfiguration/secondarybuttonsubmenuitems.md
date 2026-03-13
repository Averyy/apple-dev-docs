# secondaryButtonSubmenuItems

**Framework**: ManagedSettingsUI  
**Kind**: property

An array of strings that define the items to display in the secondary button’s submenu.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
let secondaryButtonSubmenuItems: [String]?
```

#### Discussion

When you provide this array, the system displays a submenu on secondary button taps. Add up to three array elements that correspond to custom actions your app implements, for example:

1. “1 more minute”
2. “15 more minutes”
3. “1 more hour”

Or, your app might tailor actions for an education app as:

1. “Finish this lesson.”
2. “Complete homework.”
3. “Take a quiz.”

To respond to menu item taps, implement [`ShieldAction.firstSecondarySubmenuItemPressed`](https://developer.apple.com/documentation/managedsettings/shieldaction/firstsecondarysubmenuitempressed), [`ShieldAction.secondSecondarySubmenuItemPressed`](https://developer.apple.com/documentation/managedsettings/shieldaction/secondsecondarysubmenuitempressed), and [`ShieldAction.thirdSecondarySubmenuItemPressed`](https://developer.apple.com/documentation/managedsettings/shieldaction/thirdsecondarysubmenuitempressed), depending on the number of elements your app adds to the array.

If you provide `nil` or an empty array, the secondary button doesn’t display a submenu and instead invokes the [`ShieldAction.secondaryButtonPressed`](https://developer.apple.com/documentation/managedsettings/shieldaction/secondarybuttonpressed) action when a person presses the secondary button. The system automatically adds a Cancel button to dismiss the menu.

## See Also

- [let secondaryButtonLabel: ShieldConfiguration.Label?](shieldconfiguration/secondarybuttonlabel.md)
  The label of the optional secondary button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration/secondarybuttonsubmenuitems)*