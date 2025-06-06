# ApplicationToken

**Framework**: ManagedSettings  
**Kind**: typealias

A representation of an application.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
typealias ApplicationToken = Token<Application>
```

#### Discussion

Use `ApplicationToken` to restrict and filter device applications without access to personal user data. [`FamilyActivitySelection`](https://developer.apple.com/documentation/FamilyControls/FamilyActivitySelection) provides tokens that devices within the same Family Sharing group can use to identify applications.

## See Also

- [struct Application](application.md)
  A representation of an application on the user’s device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/applicationtoken)*