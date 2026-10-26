# getSamplePositions:count:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Retrieves the previously-configured custom sample positions.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (NSUInteger) getSamplePositions:(MTLSamplePosition *) positions count:(NSUInteger) count;
```

#### Return Value

The number of previously-configured custom sample positions.

#### Discussion

This method stores the app’s last set custom sample positions into an output array. Metal only modifies the array when the `count` parameter consists of a length sufficient to store the number of sample positions.

## Parameters

- `positions`: The destination array where Metal stores [`MTLSamplePosition`](../mtlsampleposition.md) instances.
- `count`: Number of [`MTLSamplePosition`](../mtlsampleposition.md) instances in the array. This array needs to be large enough to store all sample positions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpassdescriptor/getsamplepositions:count:)*