# init(_:context:)

**Framework**: Local Authentication  
**Kind**: init

Creates a local authentication view with a localizable title and required context.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency init(_ titleKey: LocalizedStringKey, context: LAContext) where Label == Text
```

## Parameters

- `titleKey`: A localized title that displays below the authentication view.
- `context`: A context used to evaluate authentication policies.

## See Also

- [init<S>(S, context: LAContext)](localauthenticationview/init(_:context:)-9xeoo.md)
  Creates a local authentication view with a required context.
- [init(context: LAContext, label: () -> Label)](localauthenticationview/init(context:label:).md)
  Creates a local authentication view with a label and required context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview/init(_:context:)-676qx)*