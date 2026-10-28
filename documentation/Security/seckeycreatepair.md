# SecKeyCreatePair

**Framework**: Security  
**Kind**: func  
**Role**: Function

Creates an asymmetric key pair and stores it in a keychain.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecKeyCreatePair(SecKeychainRef keychainRef, CSSM_ALGORITHMS algorithm, uint32 keySizeInBits, CSSM_CC_HANDLE contextHandle, CSSM_KEYUSE publicKeyUsage, uint32 publicKeyAttr, CSSM_KEYUSE privateKeyUsage, uint32 privateKeyAttr, SecAccessRef initialAccess, SecKeyRef*publicKey, SecKeyRef*privateKey);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

This function uses default values for any attributes required by specific key-generation algorithms. Algorithms supported by the AppleCSP module are listed in [Apple Cryptographic Service Provider Functional Specification](https://developer.apple.com/library/archive/documentation/Security/Reference/SecAppleCryptoSpec/Apple_Cryptographic_Service_Provider_Functional_Specification.pdf). For details about algorithms and default values for key-generation parameters, download the CDSA security framework from Apple’s Open Source website at [https://opensource.apple.com/](https://opensource.apple.com/) and read the file `Supported_CSP_Algorithms.doc` in the Documentation folder.

If you need extra parameters to generate a key—as required by some algorithms—call [`SecKeychainGetCSPHandle`](./seckeychaingetcsphandle.md) to obtain a CSSM CSP handle and then call `CSSM_CSP_CreateKeyGenContext` to create a context. With this context, use `CSSM_UpdateContextAttributes` to add additional parameters. Finally, call `CSSM_DeleteContext` to dispose of the context after calling this function.

## Parameters

- `keychainRef`: The keychain object for the keychain in which to store the private and public key items. Specify `NULL` for the default keychain.
- `algorithm`: The algorithm to use to generate the key pair. Possible values are defined in `Security.framework/cssmtype.h`. Algorithms supported by the AppleCSP module are listed in [Apple Cryptographic Service Provider Functional Specification](https://developer.apple.com/library/archive/documentation/Security/Reference/SecAppleCryptoSpec/Apple_Cryptographic_Service_Provider_Functional_Specification.pdf). This parameter is ignored if the `contextHandle` parameter is not `0`.
- `keySizeInBits`: A key size for the key pair. See [Apple Cryptographic Service Provider Functional Specification](https://developer.apple.com/library/archive/documentation/Security/Reference/SecAppleCryptoSpec/Apple_Cryptographic_Service_Provider_Functional_Specification.pdf) for permissible key sizes for each algorithm supported by the AppleCSP module.
- `contextHandle`: A CSSM CSP handle, or `0`. If this argument is not `0`, the `algorithm` and `keySizeInBits` parameters are ignored.
- `publicKeyUsage`: A bit mask indicating all permitted uses for the new public key. The possible values for the `CSSM_KEYUSE` data type are defined in `Security.framework/cssmtype.h`.
- `publicKeyAttr`: A bit mask defining attribute values for the new public key. The bit mask values are equivalent to those defined for `CSSM_KEYATTR_FLAGS` in `Security.framework/cssmtype.h`.
- `privateKeyUsage`: A bit mask indicating all permitted uses for the new private key. The possible values for the `CSSM_KEYUSE` data type are defined in `Security.framework/cssmtype.h`.
- `privateKeyAttr`: A bit mask defining attribute values for the new private key. The bit mask values are defined in `CSSM_KEYATTR_FLAGS` in `Security.framework/cssmtype.h`. Supported values are `CSSM_KETATTR_EXTRACTABLE` (the key can be taken out of the keychain) and `CSSM_KEYATTR_SENSITIVE` (an extractable key can be taken out of the keychain only in wrapped form—that is, encrypted). (Note that you must set *both* of these bits if you want the key to be extractable in wrapped form.) For any other value of this attribute, the key cannot be taken out of the keychain under any circumstances.
- `initialAccess`: An access object that sets the initial access control list for each of the keys returned. See Creating an Access Object in [Keychain services](./keychain-services.md) for functions that create an access object. For default access, specify `NULL`. The default is free access to the tool or application that calls this function, with attempted access to sensitive information by any other application causing a confirmation dialog to be displayed.
- `publicKey`: On return, points to the keychain item object of the new public key. Use this object as input to the [`SecKeyGetCSSMKey`](./seckeygetcssmkey.md) function to obtain the `CSSM_KEY` structure containing the key. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.
- `privateKey`: On return, points to the keychain item object of the new private key. Use this object as input to the [`SecKeyGetCSSMKey`](./seckeygetcssmkey.md) function to obtain the `CSSM_KEY` structure containing the key. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeycreatepair)*