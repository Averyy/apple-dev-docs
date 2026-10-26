# setSamplePositions:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Configures the custom sample positions to use in MSAA rendering.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) setSamplePositions:(const MTLSamplePosition *) positions count:(NSUInteger) count;
```

## Parameters

- `positions`: Array of [`MTLSamplePosition`](../mtlsampleposition.md) instances.
- `count`: Number of [`MTLSamplePosition`](../mtlsampleposition.md) instances in the array. This value needs to be a valid sample count, or `0` to disable custom sample positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/setsamplepositions:count:)*