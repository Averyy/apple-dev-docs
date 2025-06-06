# LocalAuthenticationView

**Framework**: Local Authentication  
**Kind**: struct

A SwiftUI view that displays an authentication interface.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency struct LocalAuthenticationView<Label> where Label : View
```

#### Overview

Use a [`LocalAuthenticationView`](localauthenticationview.md) to display a view that prompts users to authenticate with the app. The view visually represents the state of an [`LAPolicy`](lapolicy.md) evaluation from the [`Local Authentication`](LocalAuthentication.md) framework.

The following shows a [`LocalAuthenticationView`](localauthenticationview.md) in a Mac app with an implicit [`LAContext`](lacontext.md) instance:

```swift
var body: some View {
    LocalAuthenticationView(
        "Continue with Touch ID",
        reason: Text("Access sandcastle competition designs")
    ) { result in
        switch result {
        case .success:
            print("Authorized")
        case .failure(let error):
            print("Authorization failed: \(error)")
        }
    }
    .controlSize(.large)
}
```

If your app’s authorization flow reuses an existing [`LAContext`](lacontext.md), pass it as part of initializing a [`LocalAuthenticationView`](localauthenticationview.md) and call its [`evaluatePolicy(_:localizedReason:reply:)`](lacontext/evaluatepolicy(_:localizedreason:reply:).md) method after the view appears.

## Topics

### Authenticating with an implicit context
- [init(reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void, label: () -> Label)](localauthenticationview/init(reason:context:result:label:).md)
  Creates a local authentication view.
- [init<S>(S, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](localauthenticationview/init(_:reason:context:result:)-8ubaq.md)
  Creates a local authentication view with a title.
- [init(LocalizedStringKey, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](localauthenticationview/init(_:reason:context:result:)-917ds.md)
  Creates a local authentication view with a localizable title.
- [init(Text, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](localauthenticationview/init(_:reason:context:result:)-4pkpi.md)
  Creates a local authentication view with a title text view.
### Authenticating with a context you supply
- [init<S>(S, context: LAContext)](localauthenticationview/init(_:context:)-9xeoo.md)
  Creates a local authentication view with a required context.
- [init(context: LAContext, label: () -> Label)](localauthenticationview/init(context:label:).md)
  Creates a local authentication view with a label and required context.
- [init(LocalizedStringKey, context: LAContext)](localauthenticationview/init(_:context:)-676qx.md)
  Creates a local authentication view with a localizable title and required context.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview)*