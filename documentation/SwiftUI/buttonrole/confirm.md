# confirm

**Framework**: SwiftUI  
**Kind**: property

A role that indicates a button that confirms an operation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
static let confirm: ButtonRole
```

#### Discussion

The following view would display a confirm button in the toolbar.

struct NewContactSheet: View { var body: some View { NavigationStack { NewContactEditor() .toolbar { Button(role: .confirm) { saveChanges() } } } } }


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/buttonrole/confirm)*