# GetBootstrapTokenRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Command

The get bootstrap token request details.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 10.15+
- visionOS 26.0+

## Declaration

```
object GetBootstrapTokenRequest
```

## Mentions

- [Deploying software updates using declarative management](./deploying-software-updates-using-declarative-management.md)

## Properties

- `AwaitingConfiguration` (boolean): If `true`, the device is awaiting a [`Device Configured`](./device-configured-command.md) command before proceeding through Setup Assistant.

  **Default**: `false`
- `MessageType` (string) *(required)*: The message type, which requires a value of `GetBootstrapToken`.

  **Allowed Values**: `GetBootstrapToken`

## See Also

### Requests and responses
- [object GetBootstrapTokenResponse](./getbootstraptokenresponse.md)
  The get bootstrap token response details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getbootstraptokenrequest)*