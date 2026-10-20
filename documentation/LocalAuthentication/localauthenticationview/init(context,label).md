# init(context:label:)

**Framework**: Local Authentication  
**Kind**: init  
**Role**: Initializer

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

### Authenticating with a context you supply
- [init<S>(S, context: LAContext)](./init%28_,context%29-9xeoo.md)
  Creates a local authentication view with a required context.
- [init(LocalizedStringKey, context: LAContext)](./init%28_,context%29-676qx.md)
  Creates a local authentication view with a localizable title and required context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview/init(context:label:))*