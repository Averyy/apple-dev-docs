# property(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the receiver’s property for a given key.

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
func property(forKey key: Stream.PropertyKey) -> Any?
```

```objc
- (id) propertyForKey:(NSStreamPropertyKey) key;
```

#### Return Value

The receiver’s property for the key `key`.

## Parameters

- `key`: The key for one of the receiver’s properties. See Constants for a description of the available property-key constants and associated values.

## See Also

### Configuring Streams
- [func setProperty(Any?, forKey: Stream.PropertyKey) -> Bool](./setproperty%28_,forkey%29.md)
  Attempts to set the value of a given property of the receiver and returns a Boolean value that indicates whether the value is accepted by the receiver.
- [var delegate: (any StreamDelegate)?](./delegate.md)
  Sets the receiver’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/stream/property(forkey:))*