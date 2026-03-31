# AskPermissionAction

**Framework**: PermissionKit  
**Kind**: struct

An action that sends a permission question to a parent or guardian.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)
- macOS 26.5+ (Beta)
- visionOS 26.5+ (Beta)

## Declaration

```swift
struct AskPermissionAction
```

#### Overview

Use the `EnvironmentValues/askPermission` environment value to get an instance of this action, then call the instance to send a permission question. You can call the instance directly because it defines a [`callAsFunction(_:)`](askpermissionaction/callasfunction(_:).md) method.

For example:

```swift
struct MyView: View {
    @Environment(\.askPermission) private var askPermission

    var body: some View {
        Button("Ask Permission") {
            try await askPermission(question)
        }
    }
}
```

## Topics

### Instance Methods
- [func callAsFunction<Topic>(PermissionQuestion<Topic>) async throws](askpermissionaction/callasfunction(_:).md)
  Sends a permission question to a parent or guardian.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/askpermissionaction)*