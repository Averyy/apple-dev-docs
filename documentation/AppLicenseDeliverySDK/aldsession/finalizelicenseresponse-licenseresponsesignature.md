# finalizeLicenseResponse(licenseResponse:signature:)

**Framework**: App License Delivery SDK  
**Kind**: method

Returns a signed license in a byte array to send in response to a license request from iOS.

## Declaration

```swift
func finalizeLicenseResponse(licenseResponse: [UInt8], signature: [UInt8]? = nil) throws -> [UInt8]
```

## Mentions

- [Licensing alternative distribution apps](licensing-alternative-distribution-apps.md)

#### Return Value

The signed license in a byte array.

#### Discussion

Encode the return result to `base64` and send it as the `"license"` key in response to an iOS license request.

You can omit the `signature` argument if you include the `signingKey` argument in the [`ALDProvider`](aldprovider.md) initializer. Otherwise, pass in a signature of the license in the `signature` argument, signed by the signing certificate private key.

For more information, see [`Licensing alternative distribution apps`](licensing-alternative-distribution-apps.md).

## Parameters

- `licenseResponse`: The license created by  .
- `signature`: A signature for the license, signed by the signing certificate private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicensedeliverysdk/aldsession/finalizelicenseresponse(licenseresponse:signature:))*