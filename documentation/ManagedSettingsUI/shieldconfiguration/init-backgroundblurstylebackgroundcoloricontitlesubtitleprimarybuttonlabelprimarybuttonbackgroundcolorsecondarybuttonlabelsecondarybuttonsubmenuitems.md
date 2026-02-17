# init(backgroundBlurStyle:backgroundColor:icon:title:subtitle:primaryButtonLabel:primaryButtonBackgroundColor:secondaryButtonLabel:secondaryButtonSubmenuItems:)

**Framework**: ManagedSettingsUI  
**Kind**: init

Creates a shield configuration with the specified values.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
init(backgroundBlurStyle: UIBlurEffect.Style? = nil, backgroundColor: UIColor? = nil, icon: UIImage? = nil, title: ShieldConfiguration.Label? = nil, subtitle: ShieldConfiguration.Label? = nil, primaryButtonLabel: ShieldConfiguration.Label? = nil, primaryButtonBackgroundColor: UIColor? = nil, secondaryButtonLabel: ShieldConfiguration.Label? = nil, secondaryButtonSubmenuItems: [String]? = nil)
```

#### Discussion

The system provides a default for any options that you don’t specify.

## Parameters

- `backgroundBlurStyle`: A blur style to apply to the  .
- `backgroundColor`: A color to display in the shield’s background.
- `icon`: An icon to display on the shield.
- `title`: A title for the shield.
- `subtitle`: Additional text to display on the shield.
- `primaryButtonLabel`: A label for the shield’s main button.
- `primaryButtonBackgroundColor`: A background color for the shield’s main button.
- `secondaryButtonLabel`: An additional button to display on the shield.
- `secondaryButtonSubmenuItems`: List of items to display in the sub menu after selecting the secondary button


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettingsui/shieldconfiguration/init(backgroundblurstyle:backgroundcolor:icon:title:subtitle:primarybuttonlabel:primarybuttonbackgroundcolor:secondarybuttonlabel:secondarybuttonsubmenuitems:))*