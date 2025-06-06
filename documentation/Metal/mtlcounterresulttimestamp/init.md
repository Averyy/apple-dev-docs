# init()

**Framework**: Metal  
**Kind**: init

Creates a default timestamp result.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init()
```

#### Discussion

Metal creates [`MTLCounterResultTimestamp`](mtlcounterresulttimestamp.md) instances for you when you resolve the counter set’s data (see [`Converting a GPU’s Counter Data into a Readable Format`](converting-a-gpus-counter-data-into-a-readable-format.md)). There’s no reason for you to manually create one in your app.

## See Also

- [init(timestamp: UInt64)](mtlcounterresulttimestamp/init(timestamp:).md)
  Creates a timestamp result from a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresulttimestamp/init())*