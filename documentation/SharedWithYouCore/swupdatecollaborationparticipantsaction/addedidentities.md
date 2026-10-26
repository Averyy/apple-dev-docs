# addedIdentities

**Framework**: SharedWithYouCore  
**Kind**: property  
**Role**: Instance Property

An array of added identities in a collaboration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var addedIdentities: [SWPerson.Identity] { get }
```

```objc
@property (nonatomic, readonly) NSArray<SWPersonIdentity *> * addedIdentities;
```

## Mentions

- [Adding custom collaboration to your app](../../SharedWithYou/adding-custom-collaboration-to-your-app.md)

## See Also

### Accessing action attributes
- [var collaborationMetadata: SWCollaborationMetadata](./collaborationmetadata.md)
  An object for conveying data during a collaboration.
- [var removedIdentities: [SWPerson.Identity]](./removedidentities.md)
  An array of removed identities in a collaboration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swupdatecollaborationparticipantsaction/addedidentities)*