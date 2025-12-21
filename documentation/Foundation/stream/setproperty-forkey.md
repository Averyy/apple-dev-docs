# setProperty(_:forKey:)

**Framework**: Foundation  
**Kind**: method

Attempts to set the value of a given property of the receiver and returns a Boolean value that indicates whether the value is accepted by the receiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setProperty(_ property: Any?, forKey key: Stream.PropertyKey) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the value is accepted by the receiver, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `property`: The value for  .
- `key`: The key for one of the receiver’s properties. See Constants for a description of the available property-key constants and expected values.

## See Also

- [func property(forKey: Stream.PropertyKey) -> Any?](stream/property(forkey:).md)
  Returns the receiver’s property for a given key.
- [var delegate: (any StreamDelegate)?](stream/delegate.md)
  Sets the receiver’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/setproperty(_:forkey:))*