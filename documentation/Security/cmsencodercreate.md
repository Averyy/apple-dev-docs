# CMSEncoderCreate(_:)

**Framework**: Security  
**Kind**: func

Creates a CMSEncoder reference.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func CMSEncoderCreate(_ cmsEncoderOut: UnsafeMutablePointer<CMSEncoder?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This is the first function in a sequence of encoder functions that you call to sign or encrypt a message. The other functions in the sequence require you to pass in the CMSEncoder reference returned by this function. In many cases, you can call the [`CMSEncode`](cmsencode.md) function alone instead of this sequence of encoder functions.

## Parameters

- `cmsEncoderOut`: On return, points to a CMSEncoder reference. You must use the   function to free this reference when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmsencodercreate(_:))*