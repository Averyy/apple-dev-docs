# attestPendingKey:clientDataHash:completion:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 15.4+

## Declaration

```objc
- (void) attestPendingKey:(ASAuthorizationProviderExtensionKeyType) keyType clientDataHash:(NSData *) clientDataHash completion:(void (^)(NSArray *attestationCertificates, NSError *error)) completion;
```

## Discussion

Provides a new or cached attestation for the specified pending key type.

## Parameters

- `keyType`: The pending key type for the attestation.
- `clientDataHash`: A SHA256 hash of a unique, single-use data block that embeds a challenge from your server.
- `completion`: A closure that the method calls upon completion with the following parameters:

  - attestationCertificates An array of certificates that verify the validity of the pending key associated with the keyType. Send this to your server for processing.
  - error A DCError instance that indicates the reason for failure, or nil on success.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionloginmanager/attestpendingkey:clientdatahash:completion:)*