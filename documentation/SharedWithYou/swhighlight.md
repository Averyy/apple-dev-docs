# SWHighlight

**Framework**: Shared with You  
**Kind**: class  
**Role**: Class

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

```objc
@interface SWHighlight : NSObject
```

## Mentions

- [Adding shared content collaboration to your app](./adding-shared-content-collaboration-to-your-app.md)
- [Making your app content shareable](./making-your-app-content-shareable.md)

#### Overview

The system doesn’t expose the identities of the contacts to the app. It tracks shared universal links for the current user and determines which links to elevate for consumption in an app. When the system deems a link to be useful, it surfaces that link to the hosting app in the form of an `SWHighlight` object.

## Topics

### Viewing highlight attributes
- [var identifier: any NSCopying & NSSecureCoding](./swhighlight/identifier.md)
  The unique identifier for the highlight.
- [var url: URL](./swhighlight/url.md)
  The surfaced content URL for the highlight.
### Initializers
- [init?(coder: NSCoder)](./swhighlight/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [SWCollaborationHighlight](./swcollaborationhighlight.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Highlights
- [class SWHighlightCenter](./swhighlightcenter.md)
  An object that contains a priority-ordered list of universal links to share with the current user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlight)*