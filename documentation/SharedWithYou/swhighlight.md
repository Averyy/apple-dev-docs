# SWHighlight

**Framework**: Shared With You  
**Kind**: class

An object that represents a universal link to share by any number of contacts in one or more conversations.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class SWHighlight
```

## Mentions

- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)
- [Making your app content shareable](making-your-app-content-shareable.md)

#### Overview

The system doesn’t expose the identities of the contacts to the app. It tracks shared universal links for the current user and determines which links to elevate for consumption in an app. When the system deems a link to be useful, it surfaces that link to the hosting app in the form of an `SWHighlight` object.

## Topics

### Viewing highlight attributes
- [var identifier: any NSCopying & NSSecureCoding](swhighlight/identifier.md)
  The unique identifier for the highlight.
- [var url: URL](swhighlight/url.md)
  The surfaced content URL for the highlight.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [SWCollaborationHighlight](swcollaborationhighlight.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SWHighlightCenter](swhighlightcenter.md)
  An object that contains a priority-ordered list of universal links to share with the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlight)*