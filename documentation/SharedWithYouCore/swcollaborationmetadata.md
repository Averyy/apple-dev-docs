# SWCollaborationMetadata

**Framework**: SharedWithYouCore  
**Kind**: class  
**Role**: Class

A model object for conveying data during a collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class SWCollaborationMetadata
```

```objc
@interface SWCollaborationMetadata : NSObject
```

## Mentions

- [Adding custom collaboration to your app](../SharedWithYou/adding-custom-collaboration-to-your-app.md)
- [Adding shared content collaboration to your app](../SharedWithYou/adding-shared-content-collaboration-to-your-app.md)

#### Overview

Use `SWCollaborationMetadata` to share content without using iCloud. The system wraps the metadata object in an [`NSItemProvider`](../Foundation/nsitemprovider.md) object to implement a custom collaboration infrastructure.

If your app uses SwiftUI, `SWCollaborationMetadata` is compatible with the [`Transferable`](../CoreTransferable/transferable.md) protocol and the [`ShareLink`](../SwiftUI/sharelink.md) view.

## Topics

### Creating collaboration metadata
- [init(localIdentifier: SWLocalCollaborationIdentifier)](./swcollaborationmetadata/init%28localidentifier%29.md)
  Creates and initializes a collaboration metadata object for the specified local identifier.
- [init(collaborationIdentifier: SWCollaborationIdentifier)](./swcollaborationmetadata/init%28collaborationidentifier%29.md)
  Creates and initializes a collaboration metadata object for the specified global identifier.
### Accessing metadata attributes
- [var collaborationIdentifier: SWCollaborationIdentifier](./swcollaborationmetadata/collaborationidentifier.md)
  A globally unique identifier that the app hosting the collaboration provides.
- [var defaultShareOptions: SWCollaborationShareOptions?](./swcollaborationmetadata/defaultshareoptions.md)
  The collaboration options that the content supports.
- [var initiatorHandle: String?](./swcollaborationmetadata/initiatorhandle.md)
  The handle of the person who initiates the collaboration.
- [var initiatorNameComponents: PersonNameComponents?](./swcollaborationmetadata/initiatornamecomponents.md)
  The name of the person who initiates the collaboration.
- [var localIdentifier: SWLocalCollaborationIdentifier](./swcollaborationmetadata/localidentifier.md)
  A locally unique identifier for the item the metadata represents.
- [var title: String?](./swcollaborationmetadata/title.md)
  The title of the content.
- [var userSelectedShareOptions: SWCollaborationShareOptions?](./swcollaborationmetadata/userselectedshareoptions.md)
  The selected collaboration options from the person who sends the invitation.
### Initializers
- [init?(coder: NSCoder)](./swcollaborationmetadata/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSItemProviderReading](../Foundation/nsitemproviderreading.md)
- [NSItemProviderWriting](../Foundation/nsitemproviderwriting.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Transferable](../CoreTransferable/transferable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata)*