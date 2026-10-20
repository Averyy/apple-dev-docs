# init(signers:isEncrypted:signingError:encryptionError:shouldBlockRemoteContent:localizedRemoteContentBlockingReason:)

**Framework**: MailKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(signers: [MEMessageSigner], isEncrypted: Bool, signingError: (any Error)?, encryptionError: (any Error)?, shouldBlockRemoteContent: Bool, localizedRemoteContentBlockingReason: String?)
```

```objc
- (instancetype) initWithSigners:(NSArray<MEMessageSigner *> *) signers isEncrypted:(BOOL) isEncrypted signingError:(NSError *) signingError encryptionError:(NSError *) encryptionError shouldBlockRemoteContent:(BOOL) shouldBlockRemoteContent localizedRemoteContentBlockingReason:(NSString *) localizedRemoteContentBlockingReason;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessagesecurityinformation/init(signers:isencrypted:signingerror:encryptionerror:shouldblockremotecontent:localizedremotecontentblockingreason:))*