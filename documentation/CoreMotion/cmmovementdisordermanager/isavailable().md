# isAvailable()

**Framework**: Core Motion  
**Kind**: method  
**Role**: Type Method

A Boolean value indicating whether the current device supports the movement disorder manager.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class func isAvailable() -> Bool
```

```objc
+ (BOOL) isAvailable;
```

## See Also

### Checking Availablility
- [class func authorizationStatus() -> CMAuthorizationStatus](./authorizationstatus%28%29.md)
  A value indicating whether the user has authorized the app to monitor and query for movement disorder data.
- [class func version() -> String?](./version%28%29.md)
  Returns a string that describes the movement disorder algorithm’s current version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager/isavailable())*