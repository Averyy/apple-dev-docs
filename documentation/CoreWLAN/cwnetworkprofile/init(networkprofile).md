# init(networkProfile:)

**Framework**: Core WLAN  
**Kind**: init  
**Role**: Initializer

Creates and returns a CWNetworkProfile object initialized with the given CWNetworkProfile object.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init(networkProfile: CWNetworkProfile)
```

```objc
- (instancetype) initWithNetworkProfile:(CWNetworkProfile *) networkProfile;
```

#### Return Value

A CWNetworkProfile object.

## Parameters

- `networkProfile`: The CWNetworkProfile object to use to initialize a new CWNetworkProfile object.

## See Also

### Getting a network profile
- [init()](./init%28%29.md)
  Creates and returns a CWNetworkProfile object.
- [+ networkProfile](./networkprofile.md)
  Convenience method for getting a CWNetworkProfile object.
- [+ networkProfileWithNetworkProfile:](./networkprofilewithnetworkprofile_.md)
  Convenience method for getting a CWNetworkProfile object initialized with the given CWNetworkProfile object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corewlan/cwnetworkprofile/init(networkprofile:))*