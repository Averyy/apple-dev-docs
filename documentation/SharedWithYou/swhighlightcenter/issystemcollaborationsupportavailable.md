# isSystemCollaborationSupportAvailable

**Framework**: Shared with You  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, nonatomic, readonly, getter=isSystemCollaborationSupportAvailable) BOOL systemCollaborationSupportAvailable;
```

## See Also

### Retrieving collaboration highlights
- [func collaborationHighlight(forIdentifier: SWCollaborationIdentifier) throws -> SWCollaborationHighlight](./collaborationhighlight%28foridentifier%29-23ytv.md)
  Returns a collaboration highlight for a specified collaboration identifier.
- [func collaborationHighlight(forIdentifier: String) throws -> SWCollaborationHighlight](./collaborationhighlight%28foridentifier%29-87lhr.md)
  Returns a collaboration highlight for a specified identifier string.
- [func getCollaborationHighlight(for: URL, completionHandler: (SWCollaborationHighlight?, (any Error)?) -> Void)](./getcollaborationhighlight%28for,completionhandler%29.md)
  Returns a collaboration highlight for a specified URL.
- [func getHighlightFor(URL, completionHandler: (SWHighlight?, (any Error)?) -> Void)](./gethighlightfor%28_,completionhandler%29.md)
  Returns a highlight for a specified URL.
- [func getSignedIdentityProof(for: SWCollaborationHighlight, using: Data, completionHandler: (SWPerson.SignedIdentityProof?, (any Error)?) -> Void)](./getsignedidentityproof%28for,using,completionhandler%29.md)
  Signs passed-in data with the local device’s private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter/issystemcollaborationsupportavailable)*