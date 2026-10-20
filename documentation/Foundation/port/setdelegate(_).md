# setDelegate(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s delegate to a given object.

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
func setDelegate(_ anObject: (any PortDelegate)?)
```

```objc
- (void) setDelegate:(id<NSPortDelegate>) anObject;
```

## Parameters

- `anObject`: The delegate for the receiver.

## See Also

### Working with the delegate
- [func delegate() -> (any PortDelegate)?](./delegate%28%29.md)
  Returns the receiver’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/port/setdelegate(_:))*