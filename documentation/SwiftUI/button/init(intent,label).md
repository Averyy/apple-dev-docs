# init(intent:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a button that performs an `AppIntent`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
init<I>(intent: I, @ViewBuilder label: () -> Label) where I : AppIntent
```

Available when `Label` conforms to `View`.

## Parameters

- `intent`: The `AppIntent` to execute.
- `label`: A view that describes the purpose of the button’s `action`.

## See Also

### Creating a button to perform an App Intent
- [init(_:intent:)](./init%28_,intent%29.md)
  Creates a button that performs an `AppIntent` and generates its label from a localized string key.
- [init(_:role:intent:)](./init%28_,role,intent%29.md)
  Creates a button with a specified role that performs an `AppIntent` and generates its label from a string.
- [init(role: ButtonRole?, intent: some AppIntent, label: () -> Label)](./init%28role,intent,label%29.md)
  Creates a button with a specified role that performs an `AppIntent`.
- [init(_:image:role:intent:)](./init%28_,image,role,intent%29.md)
  Creates a button with a specified role that generates its label from a string and an image resource.
- [init(_:systemImage:role:intent:)](./init%28_,systemimage,role,intent%29.md)
  Creates a button with a specified role that generates its label from a string and a system image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/button/init(intent:label:))*