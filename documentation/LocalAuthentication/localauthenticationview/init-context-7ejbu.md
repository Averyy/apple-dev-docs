# init(_:context:)

**Framework**: Local Authentication  
**Kind**: init

Creates a new view and pairs it with the specified authentication context.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(_ title: LocalizedStringResource, context: LAContext) where Label == Text
```

#### Discussion

The authentication is controlled using the provided authentication context. When `evaluatePolicy` or `evaluateAccessControl` is called on this context, the UI will be presented using this view rather than using the standard authentication alert.

## Parameters

- `title`: Title shown below the authentication view.
- `context`:    instance to control the authentication.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview/init(_:context:)-7ejbu)*