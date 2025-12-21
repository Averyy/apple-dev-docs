# expirationDate

**Framework**: PermissionKit  
**Kind**: property

The date that this question expires, if any.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var expirationDate: Date?
```

#### Discussion

Once the date passes, the person that receives the question can no longer respond.

## See Also

- [let id: UUID](permissionquestion/id.md)
  A unique identifier for the question.
- [let topic: Topic](permissionquestion/topic.md)
  A topic that can be used to interpret a person’s request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/permissionquestion/expirationdate)*