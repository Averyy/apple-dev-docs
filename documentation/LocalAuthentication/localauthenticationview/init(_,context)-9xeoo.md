# init(_:context:)

**Framework**: Local Authentication  
**Kind**: init  
**Role**: Initializer

Creates a local authentication view with a required context.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency init<S>(_ title: S, context: LAContext) where Label == Text, S : StringProtocol
```

## Parameters

- `title`: A title that displays below the authentication view.
- `context`: A context used to evaluate authentication policies.

## See Also

### Authenticating with a context you supply
- [init(context: LAContext, label: () -> Label)](./init%28context,label%29.md)
  Creates a local authentication view with a label and required context.
- [init(LocalizedStringKey, context: LAContext)](./init%28_,context%29-676qx.md)
  Creates a local authentication view with a localizable title and required context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview/init(_:context:)-9xeoo)*