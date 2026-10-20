# collaborationHighlight(forIdentifier:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Returns a collaboration highlight for a specified collaboration identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func collaborationHighlight(forIdentifier collaborationIdentifier: SWCollaborationIdentifier) throws -> SWCollaborationHighlight
```

```objc
- (SWCollaborationHighlight *) collaborationHighlightForIdentifier:(SWCollaborationIdentifier) collaborationIdentifier error:(NSError **) error;
```

#### Return Value

The `SWCollaborationHighlight` associated with the `identifier`.

## Parameters

- `collaborationIdentifier`: The unique identifier that the system uses to find the [`SWCollaborationHighlight`](../swcollaborationhighlight.md).

## See Also

### Retrieving collaboration highlights
- [class var isSystemCollaborationSupportAvailable: Bool](./issystemcollaborationsupportavailable.md)
  A Boolean value that represents full support for Messages collaboration features.
- [func collaborationHighlight(forIdentifier: String) throws -> SWCollaborationHighlight](./collaborationhighlight%28foridentifier%29-87lhr.md)
  Returns a collaboration highlight for a specified identifier string.
- [func getCollaborationHighlight(for: URL, completionHandler: (SWCollaborationHighlight?, (any Error)?) -> Void)](./getcollaborationhighlight%28for,completionhandler%29.md)
  Returns a collaboration highlight for a specified URL.
- [func getHighlightFor(URL, completionHandler: (SWHighlight?, (any Error)?) -> Void)](./gethighlightfor%28_,completionhandler%29.md)
  Returns a highlight for a specified URL.
- [func getSignedIdentityProof(for: SWCollaborationHighlight, using: Data, completionHandler: (SWPerson.SignedIdentityProof?, (any Error)?) -> Void)](./getsignedidentityproof%28for,using,completionhandler%29.md)
  Signs passed-in data with the local device’s private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/collaborationhighlight(foridentifier:)-23ytv)*