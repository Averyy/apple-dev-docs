# defaultChoice

**Framework**: PermissionKit  
**Kind**: property

The default answer choice associated with the question.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var defaultChoice: PermissionChoice { get }
```

#### Discussion

This default choice mirrors the expected experience as if the user has opted out of asking experiences.

> **Note**: This default answer choice must also be present in the list of possible choices provided in the question.

## See Also

- [var choices: [PermissionChoice]](permissionquestion/choices.md)
  The possible answer choices associated with this question.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/defaultchoice)*