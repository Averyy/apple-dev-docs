# writeOrder(_:)

**Framework**: HomeKit  
**Kind**: method

Writes the display order of the media sources to the accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func writeOrder(_ order: [Int]) async throws
```

#### Discussion

An error is thrown if the source ordering fails to be written to the accessory.

## Parameters

- `order`: The new display order for the media sources. Provides an ordered list of   values for   services associated with the profile.

## See Also

- [var delegate: (any HMMediaSourceDisplayOrderProfile.Delegate)?](hmmediasourcedisplayorderprofile/delegate-swift.property.md)
  The property that handles updates to the display order.
- [var order: [Int]](hmmediasourcedisplayorderprofile/order.md)
  The display order of input media sources.
- [let canModifyOrder: Bool](hmmediasourcedisplayorderprofile/canmodifyorder.md)
  A Boolean that indicates if the display order of the input media sources can be modified.
- [HMMediaSourceDisplayOrderProfile.Delegate](hmmediasourcedisplayorderprofile/delegate-swift.protocol.md)
  The protocol through which a delegate receives updates on the order of input media sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmediasourcedisplayorderprofile/writeorder(_:))*