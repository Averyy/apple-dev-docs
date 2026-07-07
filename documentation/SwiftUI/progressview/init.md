# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a progress view for showing indeterminate progress that generates its label from a localized string resource.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource) where Label == Text
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf. See [`Text`](text.md) for more information about localizing strings. To initialize a indeterminate progress view with a string variable, use the corresponding initializer that takes a `StringProtocol` instance.

## Parameters

- `titleResource`: Text resource for the progress view’s localized title that describes the task in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:))*