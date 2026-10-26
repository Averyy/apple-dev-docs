# init(handle:identity:displayName:thumbnailImageData:)

**Framework**: SharedWithYouCore  
**Kind**: init  
**Role**: Initializer

Creates and initializes a person object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(handle: String?, identity: SWPerson.Identity?, displayName: String, thumbnailImageData: Data?)
```

```objc
- (instancetype) initWithHandle:(NSString *) handle identity:(SWPersonIdentity *) identity displayName:(NSString *) displayName thumbnailImageData:(NSData *) thumbnailImageData;
```

## Parameters

- `handle`: The phone number or email address for this person.
- `identity`: The identity of this person.
- `displayName`: The name of this person.
- `thumbnailImageData`: The thumbnail image data for this person. If `nil`, this will be inferred by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swperson/init(handle:identity:displayname:thumbnailimagedata:))*