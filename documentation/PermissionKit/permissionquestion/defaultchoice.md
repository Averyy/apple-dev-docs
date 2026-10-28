# defaultChoice

**Framework**: PermissionKit  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

This default choice will default to the most restrictive choice.

> **Requires**: This default answer choice must also be present in the list of possible choices provided in the question.

## See Also

### Working with choices
- [var choices: [PermissionChoice]](./choices.md)
  The possible answer choices associated with this question.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/defaultchoice)*