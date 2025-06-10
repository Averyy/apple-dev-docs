# defaultChoice

**Framework**: PermissionKit  
**Kind**: property

The default answer choice associated with the question.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
final var defaultChoice: PermissionChoice { get }
```

#### Discussion

This default choice mirrors the expected experience as if the user has opted out of asking experiences.

> **Note**: This default answer choice must also be present in the list of possible choices provided in the question.

## See Also

- [let id: UUID](permissionquestion/id-swift.property.md)
  A unique identifier for the question.
- [let topic: Topic](permissionquestion/topic.md)
  A topic that can be used to interpret a user’s request.
- [var choices: [PermissionChoice]](permissionquestion/choices.md)
  The possible answer choices associated with this question.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/defaultchoice)*