# collaborationHighlight(forIdentifier:)

**Framework**: Shared With You  
**Kind**: method

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

#### Return Value

The `SWCollaborationHighlight` associated with the `identifier`.

## Parameters

- `collaborationIdentifier`: The unique identifier that the system uses to find the  .

## See Also

- [class var isSystemCollaborationSupportAvailable: Bool](swhighlightcenter/issystemcollaborationsupportavailable.md)
  A Boolean value that represents full support for Messages collaboration features.
- [func collaborationHighlight(forIdentifier: String) throws -> SWCollaborationHighlight](swhighlightcenter/collaborationhighlight(foridentifier:)-87lhr.md)
  Returns a collaboration highlight for a specified identifier string.
- [func getCollaborationHighlight(for: URL, completionHandler: (SWCollaborationHighlight?, (any Error)?) -> Void)](swhighlightcenter/getcollaborationhighlight(for:completionhandler:).md)
  Returns a collaboration highlight for a specified URL.
- [func getHighlightFor(URL, completionHandler: (SWHighlight?, (any Error)?) -> Void)](swhighlightcenter/gethighlightfor(_:completionhandler:).md)
  Returns a highlight for a specified URL.
- [func getSignedIdentityProof(for: SWCollaborationHighlight, using: Data, completionHandler: (SWPerson.SignedIdentityProof?, (any Error)?) -> Void)](swhighlightcenter/getsignedidentityproof(for:using:completionhandler:).md)
  Signs passed-in data with the local device’s private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/collaborationhighlight(foridentifier:)-23ytv)*