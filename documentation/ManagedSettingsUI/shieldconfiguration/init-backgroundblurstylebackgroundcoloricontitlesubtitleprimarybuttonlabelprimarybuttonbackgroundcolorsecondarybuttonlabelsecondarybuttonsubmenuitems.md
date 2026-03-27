# init(backgroundBlurStyle:backgroundColor:icon:title:subtitle:primaryButtonLabel:primaryButtonBackgroundColor:secondaryButtonLabel:secondaryButtonSubmenuItems:)

**Framework**: Managed Settings UI  
**Kind**: init

Initializes a shield configuration with optional submenu items for the secondary button.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst ?+

## Declaration

```swift
init(backgroundBlurStyle: UIBlurEffect.Style? = nil, backgroundColor: UIColor? = nil, icon: UIImage? = nil, title: ShieldConfiguration.Label? = nil, subtitle: ShieldConfiguration.Label? = nil, primaryButtonLabel: ShieldConfiguration.Label? = nil, primaryButtonBackgroundColor: UIColor? = nil, secondaryButtonLabel: ShieldConfiguration.Label? = nil, secondaryButtonSubmenuItems: [String]? = nil)
```

#### Discussion

This initializer extends the shield configuration structure to display a submenu when someone taps the secondary button.

## Parameters

- `backgroundBlurStyle`: A blur style to apply to the background color.
- `backgroundColor`: A color to display for the shield’s background.
- `icon`: An icon to display on the shield.
- `title`: A title for the shield.
- `subtitle`: Additional text to display on the shield.
- `primaryButtonLabel`: A label for the shield’s main button.
- `primaryButtonBackgroundColor`: A background color for the shield’s main button.
- `secondaryButtonLabel`: An additional button to display on the shield.
- `secondaryButtonSubmenuItems`: A list of one to three items to display in a submenu after someone taps the secondary button.

## See Also

- [init(backgroundBlurStyle: UIBlurEffect.Style?, backgroundColor: UIColor?, icon: UIImage?, title: ShieldConfiguration.Label?, subtitle: ShieldConfiguration.Label?, primaryButtonLabel: ShieldConfiguration.Label?, primaryButtonBackgroundColor: UIColor?, secondaryButtonLabel: ShieldConfiguration.Label?)](shieldconfiguration/init(backgroundblurstyle:backgroundcolor:icon:title:subtitle:primarybuttonlabel:primarybuttonbackgroundcolor:secondarybuttonlabel:).md)
  Creates a shield configuration with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration/init(backgroundblurstyle:backgroundcolor:icon:title:subtitle:primarybuttonlabel:primarybuttonbackgroundcolor:secondarybuttonlabel:secondarybuttonsubmenuitems:))*