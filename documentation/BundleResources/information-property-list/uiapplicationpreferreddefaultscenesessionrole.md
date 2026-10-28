# UIApplicationPreferredDefaultSceneSessionRole

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The preferred initial scene session role for your app.

**Availability**:
- visionOS 1.0+

## Details

- **Name**: `UIApplicationPreferredDefaultSceneSessionRole`
- **Type**: string

## Possible Values

- `UIWindowSceneSessionRoleApplication`
- `UIWindowSceneSessionRoleVolumetricApplication`
- `UISceneSessionRoleImmersiveSpaceApplication`
- `CPSceneSessionRoleImmersiveSpaceApplication`

## Discussion

The system references this key to determine the preferred initial scene session role to create the first scene for your app. If you specify [`UISceneSessionRoleImmersiveSpaceApplication`](./uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md) or [`CPSceneSessionRoleImmersiveSpaceApplication`](./uiapplicationscenemanifest/uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md), the system creates an immersive space scene which connects to your application at launch. To define the style that [`UISceneSessionRoleImmersiveSpaceApplication`](./uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md) uses initially, use the [`UISceneInitialImmersionStyle`](./uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication/uisceneinitialimmersionstyle.md) key.

## See Also

### Main user interface
- [UIApplicationSceneManifest](./uiapplicationscenemanifest.md)
  The information about the app’s scene-based life-cycle support.
- [NSMainStoryboardFile](./nsmainstoryboardfile.md)
  The name of an app’s storyboard resource file.
- [UIMainStoryboardFile](./uimainstoryboardfile.md)
  The name of the app’s main storyboard file.
- [NSMainNibFile](./nsmainnibfile.md)
  The name of an app’s main user interface file.
- [LSUIElement](./lsuielement.md)
  A Boolean value indicating whether the app is an agent app that runs in the background and doesn’t appear in the Dock.
- [UISupportsTrueScreenSizeOnMac](./uisupportstruescreensizeonmac.md)
  A Boolean value that indicates whether your iPad app supports arbitrary screen sizes and resolutions when running on a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationpreferreddefaultscenesessionrole)*