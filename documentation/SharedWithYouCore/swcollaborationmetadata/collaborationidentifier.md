# collaborationIdentifier

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

A globally unique identifier that the app hosting the collaboration provides.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var collaborationIdentifier: SWCollaborationIdentifier { get }
```

```objc
@property (nonatomic, copy, readonly) SWCollaborationIdentifier collaborationIdentifier;
```

## Discussion

This identifier is unique across platforms and sharing sessions.

## See Also

### Accessing metadata attributes
- [var defaultShareOptions: SWCollaborationShareOptions?](./defaultshareoptions.md)
  The collaboration options that the content supports.
- [var initiatorHandle: String?](./initiatorhandle.md)
  The handle of the person who initiates the collaboration.
- [var initiatorNameComponents: PersonNameComponents?](./initiatornamecomponents.md)
  The name of the person who initiates the collaboration.
- [var localIdentifier: SWLocalCollaborationIdentifier](./localidentifier.md)
  A locally unique identifier for the item the metadata represents.
- [var title: String?](./title.md)
  The title of the content.
- [var userSelectedShareOptions: SWCollaborationShareOptions?](./userselectedshareoptions.md)
  The selected collaboration options from the person who sends the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata/collaborationidentifier)*