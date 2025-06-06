# Comparing app versions

**Framework**: App Store Connect API

Return a Boolean value that indicates whether two match requests are from compatible app versions.

#### Overview

Use the `areCompatibleAppVersions()` function in the expression of a matchmaking rule to determine if the version of the games that request matches are compatible. This function uses information you enter in App Store Connect — such as the bundle ID, platform, and version properties to determine compatibility. For more information, see [`Add multiplayer compatibility`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/configure-game-center/add-multiplayer-compatibility).

##### Declaration

```other
boolean areCompatibleAppVersions(object $request1, object $request2)
```

##### Parameters

##### Return Value

`true`, if the game instances that request a match are compatible; otherwise, `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/comparing-app-versions)*