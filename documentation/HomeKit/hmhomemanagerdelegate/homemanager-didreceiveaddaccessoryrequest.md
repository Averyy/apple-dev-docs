# homeManager(_:didReceiveAddAccessoryRequest:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate to add an accessory to a home by using a setup payload.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
optional func homeManager(_ manager: HMHomeManager, didReceiveAddAccessoryRequest request: HMAddAccessoryRequest)
```

#### Discussion

HomeKit calls this method when it needs help adding an accessory to a home, which typically occurs when the accessory requires explicit user authentication that HomeKit can’t negotiate. HomeKit asks the accessory manufacturer’s app, which it locates using information provided by the accessory, to complete the authentication.

If you manufacture an accessory like this, handle the [`homeManager(_:didReceiveAddAccessoryRequest:)`](hmhomemanagerdelegate/homemanager(_:didreceiveaddaccessoryrequest:).md) call in your app by creating an [`HMAccessoryOwnershipToken`](hmaccessoryownershiptoken.md) instance in a way that’s appropriate for your accessory, outside of HomeKit:

```swift
let data = negotiateTokenData(accessory: request.accessoryName)
guard let token = HMAccessoryOwnershipToken(data: data) else { return }
```

Use the resulting token to create an [`HMAccessorySetupPayload`](hmaccessorysetuppayload.md) instance. If the request’s [`requiresSetupPayloadURL`](hmaddaccessoryrequest/requiressetuppayloadurl.md) flag is `true`, get the payload URL corresponding to the named accessory, and include that in the setup payload as well:

```swift
var payload: HMAccessorySetupPayload?
if request.requiresSetupPayloadURL {
    let payloadURL = getPayloadURL(accessory: request.accessoryName)
    payload = request.makePayload(url: payloadURL, ownershipToken: token)
} else {
    payload = request.makePayload(ownershipToken: token)
}
```

Complete the setup by calling the home’s [`addAndSetupAccessories(with:completionHandler:)`](hmhome/addandsetupaccessories(with:completionhandler:).md) method with the payload:

```swift
if let payload = payload {
    request.home.addAndSetupAccessories(with: payload) { accessories, error in
        // Handle errors.
    }
}
```

## Parameters

- `manager`: The home manager making the request.
- `request`: A description of the accessory to add.

## See Also

- [class HMAddAccessoryRequest](hmaddaccessoryrequest.md)
  A request to add an accessory to a particular home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/homemanager(_:didreceiveaddaccessoryrequest:))*