# init(_:reason:context:result:)

**Framework**: Local Authentication  
**Kind**: init

Creates a local authentication view with a localizable title.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleKey: LocalizedStringKey, reason: Text, context: LAContext? = nil, result: @escaping (Result<Void, any Error>) -> Void) where Label == Text
```

## Parameters

- `titleKey`: A localized title that displays below the authentication view.
- `reason`: A localized reason that describes why your app presents an authentication prompt to the user.
- `context`: A context used to evaluate authentication policies. If  , the system creates one.
- `result`: A closure to call when the authentication succeeds or fails.

## See Also

- [init(reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void, label: () -> Label)](localauthenticationview/init(reason:context:result:label:).md)
  Creates a local authentication view.
- [init<S>(S, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](localauthenticationview/init(_:reason:context:result:)-8ubaq.md)
  Creates a local authentication view with a title.
- [init(Text, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](localauthenticationview/init(_:reason:context:result:)-4pkpi.md)
  Creates a local authentication view with a title text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview/init(_:reason:context:result:)-917ds)*