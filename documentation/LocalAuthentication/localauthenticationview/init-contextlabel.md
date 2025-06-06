# init(context:label:)

**Framework**: Local Authentication  
**Kind**: init

Creates a local authentication view with a label and required context.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency init(context: LAContext, @ViewBuilder label: () -> Label)
```

## Parameters

- `context`: A context used to evaluate authentication policies.
- `label`: A label that displays below the authentication view.

## See Also

- [init<S>(S, context: LAContext)](localauthenticationview/init(_:context:)-9xeoo.md)
  Creates a local authentication view with a required context.
- [init(LocalizedStringKey, context: LAContext)](localauthenticationview/init(_:context:)-676qx.md)
  Creates a local authentication view with a localizable title and required context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview/init(context:label:))*