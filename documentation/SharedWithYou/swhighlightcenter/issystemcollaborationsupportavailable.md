# isSystemCollaborationSupportAvailable

**Framework**: Shared with You  
**Kind**: property

A Boolean value that represents full support for Messages collaboration features.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class var isSystemCollaborationSupportAvailable: Bool { get }
```

## See Also

- [func collaborationHighlight(forIdentifier: SWCollaborationIdentifier) throws -> SWCollaborationHighlight](swhighlightcenter/collaborationhighlight(foridentifier:)-23ytv.md)
  Returns a collaboration highlight for a specified collaboration identifier.
- [func collaborationHighlight(forIdentifier: String) throws -> SWCollaborationHighlight](swhighlightcenter/collaborationhighlight(foridentifier:)-87lhr.md)
  Returns a collaboration highlight for a specified identifier string.
- [func getCollaborationHighlight(for: URL, completionHandler: (SWCollaborationHighlight?, (any Error)?) -> Void)](swhighlightcenter/getcollaborationhighlight(for:completionhandler:).md)
  Returns a collaboration highlight for a specified URL.
- [func getHighlightFor(URL, completionHandler: (SWHighlight?, (any Error)?) -> Void)](swhighlightcenter/gethighlightfor(_:completionhandler:).md)
  Returns a highlight for a specified URL.
- [func getSignedIdentityProof(for: SWCollaborationHighlight, using: Data, completionHandler: (SWPerson.SignedIdentityProof?, (any Error)?) -> Void)](swhighlightcenter/getsignedidentityproof(for:using:completionhandler:).md)
  Signs passed-in data with the local device’s private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/issystemcollaborationsupportavailable)*