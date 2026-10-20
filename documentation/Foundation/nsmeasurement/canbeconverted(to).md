# canBeConverted(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Indicates whether the measurement can be converted to the given unit.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func canBeConverted(to unit: Unit) -> Bool
```

```objc
- (BOOL) canBeConvertedToUnit:(NSUnit *) unit;
```

## See Also

### Converting to Other Units
- [func converting(to: Unit) -> Measurement<Unit>](./converting%28to%29.md)
  Returns a measurement created by converting the receiver to the specified unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmeasurement/canbeconverted(to:))*