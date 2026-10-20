# UINavigationBar

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

Navigation bar visibility and configuration during launch.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Details

- **Name**: `UINavigationBar` (Show Navigation bar)
- **Type**: dictionary

#### Discussion

When you provide a dictionary for this key, the system displays a navigation bar during launch. You can optionally set the dictionary’s [`UIImageName`](./uinavigationbar/uiimagename.md) key to define a custom image for the navigation bar.

Omit this key if you don’t want to display a navigation bar during launch.

## Topics

### Optional Image
- [UIImageName](./uinavigationbar/uiimagename.md)
  A custom image that replaces the navigation bar during launch.

## See Also

### Border Elements
- [UITabBar](./uitabbar.md)
  Tab bar visibility and configuration during launch.
- [UIToolbar](./uitoolbar.md)
  Toolbar visibility and configuration during launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreen/uinavigationbar)*