# BuildBetaDetail.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a Build Beta Details resource.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BuildBetaDetail.Attributes
```

## Properties

- `autoNotifyEnabled` (boolean): A Boolean value that enables you to send test invitations to users automatically when the build is available to external groups.
- `externalBuildState` (ExternalBetaState): A state that indicates if the build is available for external testing.
- `internalBuildState` (InternalBetaState): A state that indicates if the build is available for internal testing.

## See Also

- [Build Beta Details](build-beta-details.md)
  TestFlight-specific information about beta builds.
- [object BuildBetaDetail.Relationships](buildbetadetail/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildbetadetail/attributes-data.dictionary)*