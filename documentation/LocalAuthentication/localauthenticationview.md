# LocalAuthenticationView

**Framework**: Local Authentication  
**Kind**: struct  
**Role**: Structure

A SwiftUI view that displays an authentication interface.

**Availability**:
- macOS 13.0+

## Declaration

```swift
@MainActor
@preconcurrency struct LocalAuthenticationView<Label> where Label : View
```

#### Overview

Use a [`LocalAuthenticationView`](./localauthenticationview.md) to display a view that prompts users to authenticate with the app. The view visually represents the state of an [`LAPolicy`](./lapolicy.md) evaluation from the [Local Authentication](./LocalAuthentication.md) framework.

The following shows a [`LocalAuthenticationView`](./localauthenticationview.md) in a Mac app with an implicit [`LAContext`](./lacontext.md) instance:

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

If your app’s authorization flow reuses an existing [`LAContext`](./lacontext.md), pass it as part of initializing a [`LocalAuthenticationView`](./localauthenticationview.md) and call its [`evaluatePolicy(_:localizedReason:reply:)`](./lacontext/evaluatepolicy%28_,localizedreason,reply%29.md) method after the view appears.

## Topics

### Authenticating with an implicit context
- [init(reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void, label: () -> Label)](./localauthenticationview/init%28reason,context,result,label%29.md)
  Creates a local authentication view.
- [init<S>(S, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](./localauthenticationview/init%28_,reason,context,result%29-8ubaq.md)
  Creates a local authentication view with a title.
- [init(LocalizedStringKey, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](./localauthenticationview/init%28_,reason,context,result%29-917ds.md)
  Creates a local authentication view with a localizable title.
- [init(Text, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](./localauthenticationview/init%28_,reason,context,result%29-4pkpi.md)
  Creates a local authentication view with a title text view.
### Authenticating with a context you supply
- [init<S>(S, context: LAContext)](./localauthenticationview/init%28_,context%29-9xeoo.md)
  Creates a local authentication view with a required context.
- [init(context: LAContext, label: () -> Label)](./localauthenticationview/init%28context,label%29.md)
  Creates a local authentication view with a label and required context.
- [init(LocalizedStringKey, context: LAContext)](./localauthenticationview/init%28_,context%29-676qx.md)
  Creates a local authentication view with a localizable title and required context.
### Initializers
- [init(LocalizedStringResource, context: LAContext)](./localauthenticationview/init%28_,context%29-7ejbu.md)
  Creates a new view and pairs it with the specified authentication context.
- [init(LocalizedStringResource, reason: Text, context: LAContext?, result: (Result<Void, any Error>) -> Void)](./localauthenticationview/init%28_,reason,context,result%29-88u6u.md)
  Creates a new `LocalAuthenticationView`.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/localauthenticationview)*