# askPermission

**Framework**: SwiftUI  
**Kind**: property

An action that sends a permission question to a parent or guardian.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- macOS 26.5+
- visionOS 26.5+

## Declaration

```swift
var askPermission: AskPermissionAction { get }
```

#### Discussion

Use this environment value to get an `AskPermissionAction` instance for the current [`Environment`](environment.md). Then call the instance to send a permission question. You call the instance directly because it defines a `AskPermissionAction/callAsFunction(_:)` method that Swift calls when you call the instance directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/askpermission)*