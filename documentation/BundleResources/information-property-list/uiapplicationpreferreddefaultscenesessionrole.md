# UIApplicationPreferredDefaultSceneSessionRole

**Framework**: Bundle Resources  
**Kind**: typealias

The preferred initial scene session role for your app.

**Availability**:
- visionOS 1.0+

#### Discussion

The system references this key to determine the preferred initial scene session role to create the first scene for your app. If you specify [`UISceneSessionRoleImmersiveSpaceApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md) or [`CPSceneSessionRoleImmersiveSpaceApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cpscenesessionroleimmersivespaceapplication.md), the system creates an immersive space scene which connects to your application at launch. To define the style that [`UISceneSessionRoleImmersiveSpaceApplication`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md) uses initially, use the [`UISceneInitialImmersionStyle`](information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication/uisceneinitialimmersionstyle.md) key.

## See Also

- [UIApplicationSceneManifest](information-property-list/uiapplicationscenemanifest.md)
  The information about the app’s scene-based life-cycle support.
- [NSMainStoryboardFile](information-property-list/nsmainstoryboardfile.md)
  The name of an app’s storyboard resource file.
- [UIMainStoryboardFile](information-property-list/uimainstoryboardfile.md)
  The name of the app’s main storyboard file.
- [NSMainNibFile](information-property-list/nsmainnibfile.md)
  The name of an app’s main user interface file.
- [LSUIElement](information-property-list/lsuielement.md)
  A Boolean value indicating whether the app is an agent app that runs in the background and doesn’t appear in the Dock.
- [UISupportsTrueScreenSizeOnMac](information-property-list/uisupportstruescreensizeonmac.md)
  A Boolean value that indicates whether your iPad app supports arbitrary screen sizes and resolutions when running on a Mac.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationpreferreddefaultscenesessionrole)*