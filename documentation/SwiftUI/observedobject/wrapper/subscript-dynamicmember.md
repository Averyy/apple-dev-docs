# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Gets a binding to the value of a specified key path.

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

- `keyPath`: A key path to a specific  value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/observedobject/wrapper/subscript(dynamicmember:))*