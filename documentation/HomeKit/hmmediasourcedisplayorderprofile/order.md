# order

**Framework**: HomeKit  
**Kind**: property

The display order of input media sources.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var order: [Int] { get }
```

#### Discussion

Provides an ordered list of [`HMCharacteristicTypeIdentifier`](hmcharacteristictypeidentifier.md) values for [`HMServiceTypeInputSource`](hmservicetypeinputsource.md) services associated with the profile.

## See Also

- [func writeOrder([Int]) async throws](hmmediasourcedisplayorderprofile/writeorder(_:).md)
  Writes the display order of the media sources to the accessory.
- [var delegate: (any HMMediaSourceDisplayOrderProfile.Delegate)?](hmmediasourcedisplayorderprofile/delegate-swift.property.md)
  The property that handles updates to the display order.
- [let canModifyOrder: Bool](hmmediasourcedisplayorderprofile/canmodifyorder.md)
  A Boolean that indicates if the display order of the input media sources can be modified.
- [HMMediaSourceDisplayOrderProfile.Delegate](hmmediasourcedisplayorderprofile/delegate-swift.protocol.md)
  The protocol through which a delegate receives updates on the order of input media sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmediasourcedisplayorderprofile/order)*