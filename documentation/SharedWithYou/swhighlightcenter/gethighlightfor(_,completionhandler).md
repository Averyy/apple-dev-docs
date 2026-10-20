# getHighlightFor(_:completionHandler:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Returns a highlight for a specified URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func getHighlightFor(_ URL: URL, completionHandler: @escaping @Sendable (SWHighlight?, (any Error)?) -> Void)
```

```swift
func highlight(for URL: URL) async throws -> SWHighlight
```

```objc
- (void) getHighlightForURL:(NSURL *) URL completionHandler:(void (^)(SWHighlight *highlight, NSError *fetchError)) completionHandler;
```

## Parameters

- `URL`: The URL that the system uses to find the [`SWHighlight`](../swhighlight.md).
- `completionHandler`: Returns the [`SWHighlight`](../swhighlight.md). The system invokes the completion handler on the main thread.

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
- [func getSignedIdentityProof(for: SWCollaborationHighlight, using: Data, completionHandler: (SWPerson.SignedIdentityProof?, (any Error)?) -> Void)](./getsignedidentityproof%28for,using,completionhandler%29.md)
  Signs passed-in data with the local device’s private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/gethighlightfor(_:completionhandler:))*