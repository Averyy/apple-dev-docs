# resolveCounterRange(_:)

**Framework**: Metal  
**Kind**: method

Transforms samples of a GPU’s counter set from the driver’s internal format to a standard Metal data structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
func resolveCounterRange(_ range: Range<Int>) throws -> Data?
```

## Mentions

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Return Value

A [`Data`](https://developer.apple.com/documentation/Foundation/Data) instance in Swift, or an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) instance in Objective-C, if the method successfully resolves the range of samples in the buffer; otherwise, `nil`.

#### Discussion

You can only call this method on a counter sample buffer that you create with [`MTLStorageMode.shared`](mtlstoragemode/shared.md) (see [`storageMode`](mtlcountersamplebufferdescriptor/storagemode.md)). For an example of how and when to use this method, see [`Converting a GPU’s Counter Data into a Readable Format`](converting-a-gpus-counter-data-into-a-readable-format.md).

> **Note**:  The GPU stores [`MTLCounterErrorValue`](mtlcountererrorvalue.md) in `destinationBuffer` each time it encounters an error resolving a sample.

## Parameters

- `range`: A range that indicates which sample instances the method resolves in the counter sample buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountersamplebuffer/resolvecounterrange(_:))*