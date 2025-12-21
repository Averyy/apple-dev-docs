# start()

**Framework**: Network Extension  
**Kind**: method  
**Required**: Yes

Tells the extension to start the authentication provider, in response to a request from the framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
func start() async -> Bool
```

#### Return Value

`true` if the provider started successfully; `false`, otherwise.

#### Discussion

Use this method to prepare your provider to handle future calls to [`handleCommand(_:)`](nehotspotauthenticationprovider/handlecommand(_:).md).

## See Also

- [func stop(reason: NEProviderStopReason) async](nehotspotauthenticationprovider/stop(reason:).md)
  Tells the exension to stop the authentication provider, in response to a request from the framework.
- [enum NEProviderStopReason](neproviderstopreason.md)
  Reasons why the provider extension was stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspotauthenticationprovider/start())*