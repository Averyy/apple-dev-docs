# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

A new property wrapper for the given object type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init(_ objectType: Value.Type) where Value : AnyObject, Value : Observable
```

**Other overloads**:

```swift
init(_ keyPath: KeyPath<FocusedValues, Value?>)
```

## Discussion

Reads the focused value of the given object type.

> ❗ **Important**: This initializer only accepts objects conforming to the `Observable` protocol. For reading environment objects that conform to `ObservableObject`, use `FocusedObject`, instead.

To set the focused value that is read by this, use the `focusedValue(_:)` view modifier.

## Parameters

- `objectType`: The type of object to read the focus value for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedvalue/init(_:)-5wc9p)*