# initiatorHandle

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

The handle of the person who initiates the collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var initiatorHandle: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * initiatorHandle;
```

## Discussion

The app that initiates a collaboration sets the `initiatorHandle` to allow the user to confirm the handle before the system begins the collaboration. The value of the handle will not be transmitted to recipients, and is `nil` before the system initiates a collaboration.

## See Also

### Accessing metadata attributes
- [var collaborationIdentifier: SWCollaborationIdentifier](./collaborationidentifier.md)
  A globally unique identifier that the app hosting the collaboration provides.
- [var defaultShareOptions: SWCollaborationShareOptions?](./defaultshareoptions.md)
  The collaboration options that the content supports.
- [var initiatorNameComponents: PersonNameComponents?](./initiatornamecomponents.md)
  The name of the person who initiates the collaboration.
- [var localIdentifier: SWLocalCollaborationIdentifier](./localidentifier.md)
  A locally unique identifier for the item the metadata represents.
- [var title: String?](./title.md)
  The title of the content.
- [var userSelectedShareOptions: SWCollaborationShareOptions?](./userselectedshareoptions.md)
  The selected collaboration options from the person who sends the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata/initiatorhandle)*