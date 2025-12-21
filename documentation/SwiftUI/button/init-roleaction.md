# init(role:action:)

**Framework**: SwiftUI  
**Kind**: init

Creates a button that displays a default label.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@preconcurrency
init(role: ButtonRole, action: @escaping @MainActor () -> Void)
```

#### Discussion

For example, the following view would display a button with a ‘x’ symbol in the toolbar.

struct NewContactSheet: View { var body: some View { NavigationStack { NewContactEditor() .toolbar { Button(role: .cancel) { dismissView() } } } } }

## Parameters

- `role`: A semantic role describing the button.
- `action`: The action to perform when the user triggers the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(role:action:))*