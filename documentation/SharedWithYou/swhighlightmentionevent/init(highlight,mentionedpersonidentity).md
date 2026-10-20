# init(highlight:mentionedPersonIdentity:)

**Framework**: Shared with You  
**Kind**: init  
**Role**: Initializer

Creates and initializes a mention event.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(highlight: SWHighlight, mentionedPersonIdentity identity: SWPerson.Identity)
```

```objc
- (instancetype) initWithHighlight:(SWHighlight *) highlight mentionedPersonIdentity:(SWPersonIdentity *) identity;
```

## Parameters

- `highlight`: The related hightlight for the event.
- `identity`: The `SWPersonIdentity` of the person the sender mentions.

## See Also

### Creating a mention event
- [init(highlight: SWHighlight, mentionedPersonCloudKitShareHandle: String)](./init%28highlight,mentionedpersoncloudkitsharehandle%29.md)
  Creates and initializes a mention event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swhighlightmentionevent/init(highlight:mentionedpersonidentity:))*