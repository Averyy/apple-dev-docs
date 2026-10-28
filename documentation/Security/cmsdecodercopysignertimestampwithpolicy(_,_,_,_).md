# CMSDecoderCopySignerTimestampWithPolicy(_:_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns the timestamp of a signer of a CMS message using a given policy, if present.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func CMSDecoderCopySignerTimestampWithPolicy(_ cmsDecoder: CMSDecoder, _ timeStampPolicy: CFTypeRef?, _ signerIndex: Int, _ timestamp: UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus
```

```c
OSStatus CMSDecoderCopySignerTimestampWithPolicy(CMSDecoderRef cmsDecoder, CFTypeRef timeStampPolicy, size_t signerIndex, CFAbsoluteTime *timestamp);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Parameters

- `cmsDecoder`: A CMSDecoder reference returned by the [`CMSDecoderCreate(_:)`](./cmsdecodercreate%28_%29.md) function.
- `timeStampPolicy`: A timestamp policy. Specify `NULL` (or use the [`CMSDecoderCopySignerTimestamp(_:_:_:)`](./cmsdecodercopysignertimestamp%28_,_,_%29.md) function instead) to get the default, which is a policy using [`kSecPolicyAppleTimeStamping`](./ksecpolicyappletimestamping.md). See [Policies](./policies.md) in [Certificate, Key, and Trust Services](./certificate-key-and-trust-services.md) for more about policies.
- `signerIndex`: A number indicating which signer to examine. Signer index numbers start with 0. Use the [`CMSDecoderGetNumSigners(_:_:)`](./cmsdecodergetnumsigners%28_,_%29.md) function to determine the total number of signers for a message.
- `timestamp`: The address of an absolute time value where the result should be stored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsdecodercopysignertimestampwithpolicy(_:_:_:_:))*