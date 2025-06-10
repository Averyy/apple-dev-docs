# AudioStreamPacketDependencyDescription

**Framework**: Core Audio Types  
**Kind**: struct

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct AudioStreamPacketDependencyDescription
```

#### Overview

```None
                1 if the packet is independently decodable, 0 otherwise.
```

```None
                The count of packets that must be decoded after this packet in order to refresh the decoder,
                if the packet is independently decodable.  This value should be ignored if
                ``mIsIndependentlyDecodable`` is 0.
```

```None
                Currently unused.
```

```None
                Reserved for future use.
```

For independently decodable packets, the [`mPreRollCount`](audiostreampacketdependencydescription/mprerollcount.md) indicates how many additional packets need to be decoded after this packet in order for the decoder to start returning optimal output, if this is the first packet decoded since the decoder was initialized.

```None
For example, if this packet is packet #123 of some given packet stream, and ``mIsIndependentlyDecodable``
is 0, or ``mIsIndependentlyDecodable`` is 1 and ``mPreRollCount`` is non-zero, and the client desires optimal
output starting with the output corresponding with packet #123 (because for example the client
is an audio player whose user seeks to a starting playback position corresponding with packet #123),
the client would scan back, starting at packet #122, searching for an independently decodable
packet with a preroll not intersecting packet #123.  If for packet #122 ``mIsIndependentlyDecodable``
is 0, or ``mIsIndependentlyDecodable`` is 1 but ``mPreRollCount`` is 2 or more, the client would still not
get optimal output for packet #123 if starting here, so the client continues to scan back.
If for packet #121 ``mIsIndependentlyDecodable`` is 1 and ``mPreRollCount`` is 2 or less, the client would
start decoding from this point, but discard the output equivalent of the two extra input packets
(desired first output packet - actual first decoded packet, or 122 - 120 == 2).
```

## Topics

### Initializers
- [init()](audiostreampacketdependencydescription/init.md)
- [init(mIsIndependentlyDecodable: UInt32, mPreRollCount: UInt32, mFlags: UInt32, mReserved: UInt32)](audiostreampacketdependencydescription/init(misindependentlydecodable:mprerollcount:mflags:mreserved:).md)
### Instance Properties
- [var mFlags: UInt32](audiostreampacketdependencydescription/mflags.md)
- [var mIsIndependentlyDecodable: UInt32](audiostreampacketdependencydescription/misindependentlydecodable.md)
- [var mPreRollCount: UInt32](audiostreampacketdependencydescription/mprerollcount.md)
- [var mReserved: UInt32](audiostreampacketdependencydescription/mreserved.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiostreampacketdependencydescription)*