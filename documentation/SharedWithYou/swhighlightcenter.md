# SWHighlightCenter

**Framework**: Shared With You  
**Kind**: class

An object that contains a priority-ordered list of universal links to share with the current user.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class SWHighlightCenter
```

## Mentions

- [Adding custom collaboration to your app](adding-custom-collaboration-to-your-app.md)
- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)
- [Making your app content shareable](making-your-app-content-shareable.md)

#### Overview

The system determines which links it surfaces. The app is responsible for updating its UI to reflect the latest highlights list that the system provides.

## Topics

### Setting the delegate
- [var delegate: (any SWHighlightCenterDelegate)?](swhighlightcenter/delegate.md)
  The delegate object for the highlight center.
- [protocol SWHighlightCenterDelegate](swhighlightcenterdelegate.md)
  The protocol you use to notify the delegate when the list or rank order of surfaced highlights changes.
### Accessing highlights
- [var highlights: [SWHighlight]](swhighlightcenter/highlights.md)
  An array of shared highlights.
- [class var highlightCollectionTitle: String](swhighlightcenter/highlightcollectiontitle.md)
  A localized title to display with a collection of highlights.
### Retrieving collaboration highlights
- [class var isSystemCollaborationSupportAvailable: Bool](swhighlightcenter/issystemcollaborationsupportavailable.md)
  A Boolean value that represents full support for Messages collaboration features.
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
### Posting highlight events
- [func postNotice(for: any SWHighlightEvent)](swhighlightcenter/postnotice(for:).md)
  Posts a specified event to the highlight center for display.
- [func clearNotices(for: SWCollaborationHighlight)](swhighlightcenter/clearnotices(for:).md)
  Clears the notices for a specified collaboration highlight.
### Handling errors
- [enum SWHighlightCenterErrorCode](swhighlightcentererrorcode.md)
  The error codes for the highlight center.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class SWHighlight](swhighlight.md)
  An object that represents a universal link to share by any number of contacts in one or more conversations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightcenter)*