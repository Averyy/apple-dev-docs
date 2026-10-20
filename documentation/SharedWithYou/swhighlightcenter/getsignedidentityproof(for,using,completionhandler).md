# getSignedIdentityProof(for:using:completionHandler:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Signs passed-in data with the local device’s private key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func getSignedIdentityProof(for collaborationHighlight: SWCollaborationHighlight, using data: Data, completionHandler: @escaping @Sendable (SWPerson.SignedIdentityProof?, (any Error)?) -> Void)
```

```swift
func signedIdentityProof(for collaborationHighlight: SWCollaborationHighlight, using data: Data) async throws -> SWPerson.SignedIdentityProof
```

```objc
- (void) getSignedIdentityProofForCollaborationHighlight:(SWCollaborationHighlight *) collaborationHighlight usingData:(NSData *) data completionHandler:(void (^)(SWSignedPersonIdentityProof *, NSError *)) completionHandler;
```

## Mentions

- [Adding custom collaboration to your app](../adding-custom-collaboration-to-your-app.md)

#### Discussion

When a collaboration message is sent, the system sends it individually to each of a person’s devices. Messages identifies each device using a cryptographic public key. Since the goal is to allow access only on this set of devices, the root hash is derived from the set of public keys registered to each recipient.

The root hash is the root node of a data structure called a Merkle tree. A Merkle tree is a binary tree that is built by performing a sequence of hashing operations. In order to derive an identity for the user based on their public keys, the keys are used as the leaves of this tree. The hashing algorithm used in the Merkle tree ensures that the root node can only be computed from that set of keys.

> **Related Sessions from WWDC22**:  Session 10093: [Integrate your custom collaboration app with Messages](https://developer.apple.com/videos/play/wwdc2022/10093/)

## Parameters

- `collaborationHighlight`: The collaboration highlight that corresponds to the `data`.
- `data`: The `NSData` that the system signs.
- `completionHandler`: Returns the signed data along with proof of inclusion for the Merkle tree if signing succeeds, otherwise an error. The system invokes the completion handler on the main thread.

## See Also

### Retrieving collaboration highlights
- [class var isSystemCollaborationSupportAvailable: Bool](./issystemcollaborationsupportavailable.md)
  A Boolean value that represents full support for Messages collaboration features.
- [func collaborationHighlight(forIdentifier: SWCollaborationIdentifier) throws -> SWCollaborationHighlight](./collaborationhighlight%28foridentifier%29-23ytv.md)
  Returns a collaboration highlight for a specified collaboration identifier.
- [func collaborationHighlight(forIdentifier: String) throws -> SWCollaborationHighlight](./collaborationhighlight%28foridentifier%29-87lhr.md)
  Returns a collaboration highlight for a specified identifier string.
- [func getCollaborationHighlight(for: URL, completionHandler: (SWCollaborationHighlight?, (any Error)?) -> Void)](./getcollaborationhighlight%28for,completionhandler%29.md)
  Returns a collaboration highlight for a specified URL.
- [func getHighlightFor(URL, completionHandler: (SWHighlight?, (any Error)?) -> Void)](./gethighlightfor%28_,completionhandler%29.md)
  Returns a highlight for a specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/getsignedidentityproof(for:using:completionhandler:))*