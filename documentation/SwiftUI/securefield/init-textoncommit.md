# init(_:text:onCommit:)

**Framework**: SwiftUI  
**Kind**: init

Creates an instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, text: Binding<String>, onCommit: @escaping () -> Void)
```

## Parameters

- `titleKey`: The key for the localized title of  , describing   its purpose.
- `text`: The text to display and edit.
- `onCommit`: The action to perform when the user performs an action   (usually pressing the Return key) while the secure field has focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/securefield/init(_:text:oncommit:))*