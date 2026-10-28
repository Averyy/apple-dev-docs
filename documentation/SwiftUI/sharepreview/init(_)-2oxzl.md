# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a preview representation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(_ title: Text)
```

Available when `Image` is `Never` and `Icon` is `Never`.

**Other overloads**:

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource)
```

```swift
init(_ titleKey: LocalizedStringKey)
```

```swift
init<S>(_ title: S) where S : StringProtocol
```

## Parameters

- `title`: A title to show in a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharepreview/init(_:)-2oxzl)*