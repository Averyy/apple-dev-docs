# PermissionChoice.Answer

**Framework**: PermissionKit  
**Kind**: enum  
**Role**: Enumeration

An answer to the permission request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Answer
```

## Topics

### Determining the permission request response
- [PermissionChoice.Answer.approval](./answer-swift.enum/approval.md)
  An approved permission response.
- [PermissionChoice.Answer.denial](./answer-swift.enum/denial.md)
  A denied permission response.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Accessing answers
- [var answer: PermissionChoice.Answer](./answer-swift.property.md)
  The type of answer this choice represents.
- [static let approve: PermissionChoice](./approve.md)
  The system-preferred choice to approve a permission request.
- [static let decline: PermissionChoice](./decline.md)
  The system-preferred choice to decline a permission request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionchoice/answer-swift.enum)*