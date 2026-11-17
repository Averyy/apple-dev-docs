# photosPickerOnPrimaryAction(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the primary action handler for the Photos picker.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func photosPickerOnPrimaryAction(_ action: @escaping @MainActor () -> Void) -> some View
```

## Return Value

A Photos picker with specified primary action handler.

## Parameters

- `action`: Action to be performed when the primary action is triggered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photospickeronprimaryaction(_:))*