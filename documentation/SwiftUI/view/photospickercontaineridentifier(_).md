# photosPickerContainerIdentifier(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Limits the Photos picker to only show items in the specified container.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func photosPickerContainerIdentifier(_ containerIdentifier: String?) -> some View
```

## Return Value

A Photos picker only showing items in the specified container.

## Parameters

- `containerIdentifier`: The local identifier of the container. Usually it’s the local identifier of an asset collection. An identifier that doesn’t resolve is treated as `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/photospickercontaineridentifier(_:))*