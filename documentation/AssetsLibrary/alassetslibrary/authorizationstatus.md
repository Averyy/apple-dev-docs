# authorizationStatus()

**Framework**: Assets Library  
**Kind**: method

Returns photo data authorization status for this application.

## Declaration

```swift
class func authorizationStatus() -> ALAuthorizationStatus
```

#### Return Value

Photo data authorization status for this application. For the constants returned, see [`ALAuthorizationStatus`](alauthorizationstatus.md).

#### Discussion

This method does not prompt the user for access.

You can use it to detect restricted access and simply hide UI instead of prompting for access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assetslibrary/alassetslibrary/authorizationstatus())*