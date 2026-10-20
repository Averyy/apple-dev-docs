# contentCaptureProtected(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 26.0+

## Declaration

```swift
nonisolated
func contentCaptureProtected(_ isActive: Bool = true) -> some View
```

## See Also

### Privacy and redaction
- [func privacySensitive(Bool) -> some View](./privacysensitive%28_%29.md)
  Marks the view as containing sensitive, private user data.
- [func redacted(reason: RedactionReasons) -> some View](./redacted%28reason%29.md)
  Adds a reason to apply a redaction to this view hierarchy.
- [func unredacted() -> some View](./unredacted%28%29.md)
  Removes any reason to apply a redaction to this view hierarchy.
- [func invalidatableContent(Bool) -> some View](./invalidatablecontent%28_%29.md)
  Mark the receiver as their content might be invalidated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contentcaptureprotected(_:))*