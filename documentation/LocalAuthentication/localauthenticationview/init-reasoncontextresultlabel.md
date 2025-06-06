# init(reason:context:result:label:)

**Framework**: Local Authentication  
**Kind**: init

Creates a local authentication view.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency init(reason: Text, context: LAContext? = nil, result: @escaping (Result<Void, any Error>) -> Void, @ViewBuilder label: () -> Label)
```

## Parameters

- `reason`: A localized reason that describes why your app presents an authentication prompt to the user.
- `context`: A context used to evaluate authentication policies. If  , the system creates one.
- `result`: A closure to call when the authentication succeeds or fails.
- `label`: A label that displays below the authentication view.

## See Also

- [init<S>(S, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](localauthenticationview/init(_:reason:context:result:)-8ubaq.md)
  Creates a local authentication view with a title.
- [init(LocalizedStringKey, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](localauthenticationview/init(_:reason:context:result:)-917ds.md)
  Creates a local authentication view with a localizable title.
- [init(Text, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](localauthenticationview/init(_:reason:context:result:)-4pkpi.md)
  Creates a local authentication view with a title text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview/init(reason:context:result:label:))*