# stop(reason:)

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

Tells the exension to stop the authentication provider, in response to a request from the framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
func stop(reason: NEProviderStopReason) async
```

#### Discussion

Perform any needed shutdown tasks in your implementation of this method. After stopping, the provider receives no further commands from the framework.

## Parameters

- `reason`: The reason for stopping the provider.

## See Also

- [func start() async -> Bool](nehotspotauthenticationprovider/start.md)
  Tells the extension to start the authentication provider, in response to a request from the framework.
- [enum NEProviderStopReason](neproviderstopreason.md)
  Reasons why the provider extension was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotauthenticationprovider/stop(reason:))*