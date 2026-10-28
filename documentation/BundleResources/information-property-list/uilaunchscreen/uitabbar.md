# UITabBar

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

Tab bar visibility and configuration during launch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Details

- **Name**: `UITabBar` (Show Tab bar)
- **Type**: dictionary

## Discussion

When you provide a dictionary for this key, the system displays a tab bar during launch. You can optionally set the dictionary’s [`UIImageName`](./uitabbar/uiimagename.md) key to define a custom image for the tab bar.

Omit this key if you don’t want to display a tab bar during launch.

## Topics

### Optional Image
- [UIImageName](./uitabbar/uiimagename.md)
  A custom image that replaces the tab bar during launch.

## See Also

### Border Elements
- [UINavigationBar](./uinavigationbar.md)
  Navigation bar visibility and configuration during launch.
- [UIToolbar](./uitoolbar.md)
  Toolbar visibility and configuration during launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreen/uitabbar)*