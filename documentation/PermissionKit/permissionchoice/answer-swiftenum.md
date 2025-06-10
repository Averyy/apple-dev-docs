# PermissionChoice.Answer

**Framework**: PermissionKit  
**Kind**: enum

An answer to the permission request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum Answer
```

## Topics

### Determining the permission request response
- [PermissionChoice.Answer.approval](permissionchoice/answer-swift.enum/approval.md)
  An approved permission response.
- [PermissionChoice.Answer.denial](permissionchoice/answer-swift.enum/denial.md)
  A denied permission response.
### Decoding
- [init(from: any Decoder) throws](permissionchoice/answer-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (PermissionChoice.Answer, PermissionChoice.Answer) -> Bool](permissionchoice/answer-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](permissionchoice/answer-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](permissionchoice/answer-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](permissionchoice/answer-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](permissionchoice/answer-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var answer: PermissionChoice.Answer](permissionchoice/answer-swift.property.md)
  The kind of answer this choice is. The system will use this to properly stylize the choice when displaying it to the user.
- [static let approve: PermissionChoice](permissionchoice/approve.md)
  The system-preferred choice to approve a permission request.
- [static let decline: PermissionChoice](permissionchoice/decline.md)
  The system-preferred choice to decline a permission request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionchoice/answer-swift.enum)*