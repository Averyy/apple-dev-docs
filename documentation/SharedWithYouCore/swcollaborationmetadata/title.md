# title

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

The title of the content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * title;
```

## Discussion

The app that hosts the collaboration provides this title.

## See Also

### Accessing metadata attributes
- [var collaborationIdentifier: SWCollaborationIdentifier](./collaborationidentifier.md)
  A globally unique identifier that the app hosting the collaboration provides.
- [var defaultShareOptions: SWCollaborationShareOptions?](./defaultshareoptions.md)
  The collaboration options that the content supports.
- [var initiatorHandle: String?](./initiatorhandle.md)
  The handle of the person who initiates the collaboration.
- [var initiatorNameComponents: PersonNameComponents?](./initiatornamecomponents.md)
  The name of the person who initiates the collaboration.
- [var localIdentifier: SWLocalCollaborationIdentifier](./localidentifier.md)
  A locally unique identifier for the item the metadata represents.
- [var userSelectedShareOptions: SWCollaborationShareOptions?](./userselectedshareoptions.md)
  The selected collaboration options from the person who sends the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata/title)*