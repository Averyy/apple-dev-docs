# CMSEncoderCopySignerTimestampWithPolicy(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Returns the timestamp of a signer of a CMS message using a particular policy, if present.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func CMSEncoderCopySignerTimestampWithPolicy(_ cmsEncoder: CMSEncoder, _ timeStampPolicy: CFTypeRef?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

## Parameters

- `cmsEncoder`: A CMSEncoder reference returned by the   function.
- `timeStampPolicy`: A timestamp policy. Specify   (or use the   function instead) to get the default, which is a policy using  . See   in   for more about policies.
- `signerIndex`: A number indicating which signer to examine. Signer index numbers start with 0. Use the   function to determine the total number of signers for a message.
- `timestamp`: The address of an absolute time value where the result should be stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodercopysignertimestampwithpolicy(_:_:_:_:))*