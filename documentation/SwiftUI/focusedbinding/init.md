# init(_:)

**Framework**: SwiftUI  
**Kind**: init

A new property wrapper for the given key path.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(_ keyPath: KeyPath<FocusedValues, Binding<Value>?>)
```

#### Discussion

The value of the property wrapper is updated dynamically as focus changes and different published bindings go in and out of scope.

## Parameters

- `keyPath`: The key path for the focus value to read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedbinding/init(_:))*