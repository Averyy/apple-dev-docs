# authorizationStatus()

**Framework**: Core Motion  
**Kind**: method

A value indicating whether the user has authorized the app to monitor and query for movement disorder data.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class func authorizationStatus() -> CMAuthorizationStatus
```

#### Discussion

The first time your app attempts to monitor or query for movement disorder data, the manager asks the user for permission to collect or retrieve their movement disorder data. To request permission, your app must set a motion usage description in its `Info.plist` file. For more information, see [`Provide the motion usage description`](getting-movement-disorder-symptom-data#Provide-the-motion-usage-description.md).

## See Also

- [class func isAvailable() -> Bool](cmmovementdisordermanager/isavailable.md)
  A Boolean value indicating whether the current device supports the movement disorder manager.
- [class func version() -> String?](cmmovementdisordermanager/version.md)
  Returns a string that describes the movement disorder algorithm’s current version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/authorizationstatus())*