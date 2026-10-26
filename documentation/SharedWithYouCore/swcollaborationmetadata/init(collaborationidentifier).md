# init(collaborationIdentifier:)

**Framework**: SharedWithYouCore  
**Kind**: init  
**Role**: Initializer

Creates and initializes a collaboration metadata object for the specified global identifier.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(collaborationIdentifier: SWCollaborationIdentifier)
```

```objc
- (instancetype) initWithCollaborationIdentifier:(SWCollaborationIdentifier) collaborationIdentifier;
```

## Parameters

- `collaborationIdentifier`: A globally unique identifier for the item this metadata represents.

## See Also

### Creating collaboration metadata
- [init(localIdentifier: SWLocalCollaborationIdentifier)](./init%28localidentifier%29.md)
  Creates and initializes a collaboration metadata object for the specified local identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata/init(collaborationidentifier:))*