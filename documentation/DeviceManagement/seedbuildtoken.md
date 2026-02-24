# SeedBuildToken

**Framework**: Device Management  
**Kind**: dictionary

Describes a beta enrollment token available for the given organization.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object SeedBuildToken
```

## Properties

- `os` (string): The platform related to beta build. Possible values are: `homePodOS`, `iOS`, `OSX`, `tvOS`, `visionOS`, `watchOS`]
- `title` (string): The public facing name, like “iOS 17 Public Beta”.
- `token` (string): The token to use when requesting the beta build.

## See Also

- [object GetSeedBuildTokenResponse](getseedbuildtokenresponse.md)
  Provides a list of beta enrollment tokens available for the given organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/seedbuildtoken)*