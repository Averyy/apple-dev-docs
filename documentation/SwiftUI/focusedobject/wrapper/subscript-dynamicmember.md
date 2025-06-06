# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Returns a binding to the value of a given key path.

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
@MainActor
@preconcurrency subscript<T>(dynamicMember keyPath: ReferenceWritableKeyPath<ObjectType, T>) -> Binding<T> { get }
```

#### Return Value

A new binding.

## Parameters

- `keyPath`: A key path to a specific value on the   wrapped object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedobject/wrapper/subscript(dynamicmember:))*