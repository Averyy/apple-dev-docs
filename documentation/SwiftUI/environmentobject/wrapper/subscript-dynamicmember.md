# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Returns a binding to the resulting value of a given key path.

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
@MainActor
@preconcurrency subscript<Subject>(dynamicMember keyPath: ReferenceWritableKeyPath<ObjectType, Subject>) -> Binding<Subject> { get }
```

#### Return Value

A new binding.

## Parameters

- `keyPath`: A key path to a specific resulting value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentobject/wrapper/subscript(dynamicmember:))*