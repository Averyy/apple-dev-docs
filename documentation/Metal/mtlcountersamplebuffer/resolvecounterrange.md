# resolveCounterRange:

**Framework**: Metal  
**Kind**: method

Transforms samples of a GPU’s counter set from the driver’s internal format to a standard Metal data structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
- (NSData *) resolveCounterRange:(NSRange) range;
```

#### Return Value

An [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) instance if the method successfully resolves the range of samples in the buffer; otherwise, `nil`.

#### Discussion

You can only call this method on a counter sample buffer that you create with [`MTLStorageMode.shared`](mtlstoragemode/shared.md) (see [`storageMode`](mtlcountersamplebufferdescriptor/storagemode.md)). For an example of how and when to use this method, see [`Converting a GPU’s counter data into a readable format`](converting-a-gpus-counter-data-into-a-readable-format.md).

> **Note**:  The GPU stores [`MTLCounterErrorValue`](mtlcountererrorvalue.md) in `destinationBuffer` each time it encounters an error resolving a sample.

## Parameters

- `range`: A range that indicates which sample instances the method resolves in the counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/resolvecounterrange:)*