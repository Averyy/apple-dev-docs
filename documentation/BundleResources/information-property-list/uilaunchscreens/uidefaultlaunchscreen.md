# UIDefaultLaunchScreen

**Framework**: Bundle Resources  
**Kind**: typealias

The default launch screen configuration.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

#### Discussion

Provide the identifier, stored in the [`UILaunchScreenIdentifier`](information-property-list/uilaunchscreens/uilaunchscreendefinitions/uilaunchscreenidentifier.md) key, of one of the launch screen definitions in your [`UILaunchScreenDefinitions`](information-property-list/uilaunchscreens/uilaunchscreendefinitions.md) array. The system displays the named launch screen when launching your app in response to a URL scheme that you don’t enumerate in the [`UIURLToLaunchStoryboardAssociations`](information-property-list/uilaunchstoryboards/uiurltolaunchstoryboardassociations.md) dictionary, or when the user launches your app directly.

## See Also

- [UIURLToLaunchScreenAssociations](information-property-list/uilaunchscreens/uiurltolaunchscreenassociations.md)
  The mapping of URL schemes to launch screen configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uilaunchscreens/uidefaultlaunchscreen)*