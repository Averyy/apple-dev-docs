# init(_:icon:)

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
init(_ titleKey: LocalizedStringKey, icon: Icon)
```

Available when `Image` is `Never` and `Icon` conforms to `Transferable`.

**Other overloads**:

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource, icon: Icon)
```

```swift
init(_ title: Text, icon: Icon)
```

```swift
init<S>(_ title: S, icon: Icon) where S : StringProtocol
```

## Parameters

- `titleKey`: A key identifying a title to show in a preview.
- `icon`: An icon to show in a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/sharepreview/init(_:icon:)-8pv9z)*