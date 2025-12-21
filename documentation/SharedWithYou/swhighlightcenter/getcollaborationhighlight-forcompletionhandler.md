# getCollaborationHighlight(for:completionHandler:)

**Framework**: Shared with You  
**Kind**: method

Returns a collaboration highlight for a specified URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func collaborationHighlight(for URL: URL) async throws -> SWCollaborationHighlight
```

## Parameters

- `URL`: The URL that the system uses to find the  .
- `completionHandler`: Returns the  . The system invokes the completion handler on the main thread.

## See Also

- [class var isSystemCollaborationSupportAvailable: Bool](swhighlightcenter/issystemcollaborationsupportavailable.md)
  A Boolean value that represents full support for Messages collaboration features.
- [func collaborationHighlight(forIdentifier: SWCollaborationIdentifier) throws -> SWCollaborationHighlight](swhighlightcenter/collaborationhighlight(foridentifier:)-23ytv.md)
  Returns a collaboration highlight for a specified collaboration identifier.
- [func collaborationHighlight(forIdentifier: String) throws -> SWCollaborationHighlight](swhighlightcenter/collaborationhighlight(foridentifier:)-87lhr.md)
  Returns a collaboration highlight for a specified identifier string.
- [func getHighlightFor(URL, completionHandler: (SWHighlight?, (any Error)?) -> Void)](swhighlightcenter/gethighlightfor(_:completionhandler:).md)
  Returns a highlight for a specified URL.
- [func getSignedIdentityProof(for: SWCollaborationHighlight, using: Data, completionHandler: (SWPerson.SignedIdentityProof?, (any Error)?) -> Void)](swhighlightcenter/getsignedidentityproof(for:using:completionhandler:).md)
  Signs passed-in data with the local device’s private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/getcollaborationhighlight(for:completionhandler:))*