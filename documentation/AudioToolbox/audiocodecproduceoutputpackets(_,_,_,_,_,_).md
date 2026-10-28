# AudioCodecProduceOutputPackets(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Retrieves output data from a codec.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioCodecProduceOutputPackets(_ inCodec: AudioCodec, _ outOutputData: UnsafeMutableRawPointer, _ ioOutputDataByteSize: UnsafeMutablePointer<UInt32>, _ ioNumberPackets: UnsafeMutablePointer<UInt32>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ outStatus: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus AudioCodecProduceOutputPackets(AudioCodec inCodec, void *outOutputData, UInt32 *ioOutputDataByteSize, UInt32 *ioNumberPackets, AudioStreamPacketDescription *outPacketDescription, UInt32 *outStatus);
```

## Return Value

Returns `NoErr` if successful. Returns `kAudioCodecStateError` if the codec has not been initialized. Returns `kAudioCodecNotEnoughBufferSpaceError` if the output buffer is not large enough for the requested number of packets. See `Result Codes` for other possible values.

## Discussion

This function causes the codec to produce as many output packets as requested, provided there is sufficient input data. If there is not enough input data to produce the requested number of output packets, the `outStatus` parameter returns the value `kAudioCodecProduceOutputPacketNeedsMoreInputData` and the `ioNumberPackets` parameter indicates the actual number of packets produced. On the other hand, if there is enough input data to produce at least one additional full packet, the `outStatus` parameter returns the value `kAudioCodecProduceOutputPacketSuccessHasMore`.

Note that decoders produce linear PCM data only in multiples of the number of frames in a packet of the encoded format. (See the [`AudioCodecAppendInputData(_:_:_:_:_:)`](./audiocodecappendinputdata%28_,_,_,_,_%29.md) function for definitions of *packet* and *frame* as used by this API.) You can use the [`AudioCodecGetProperty(_:_:_:_:)`](./audiocodecgetproperty%28_,_,_,_%29.md) function to obtain this value from the [`kAudioCodecPropertyPacketFrameSize`](./kaudiocodecpropertypacketframesize.md) property. Similarly, this property indicates how many frames of linear PCM data an encoder needs in order to produce a packet of the specified output format.

Output data can be produced only in multiples of whole packets.

The combination of the [`AudioCodecAppendInputData(_:_:_:_:_:)`](./audiocodecappendinputdata%28_,_,_,_,_%29.md) and [`AudioCodecProduceOutputPackets(_:_:_:_:_:_:)`](./audiocodecproduceoutputpackets%28_,_,_,_,_,_%29.md) functions implement a “push-pull” model of data handling. First, the input data is pushed into the codec, then the resulting output data is pulled out of that same codec.

## Parameters

- `inCodec`: An audio codec object. Because an audio codec object is a Component Manger component instance, you can use the Component Manager (for example, the functions [`FindNextComponent`](../coreservices/api-1516552-findnextcomponent.md) and OpenAComponent) to obtain an audio codec object.
- `outOutputData`: The output data buffer.
- `ioOutputDataByteSize`: Indicates the size of the output data buffer.
- `ioNumberPackets`: On input, the number of packets desired. On output, the number of packets actually placed in the output buffer.
- `outPacketDescription`: An array of `AudioStreamPacketDescription` structures that describes the packet layout of the data returned by the `outOutputData` parameter. Pass `NULL` if you do not want this information returned. Note that this information is provided only when the output format is not linear PCM.
- `outStatus`: On output, information about the codec’s status to allow for proper data management. See [Output Status Constants](./api-1494122-output-status-constants.md) for the possible values that can be returned.

## See Also

### Related Documentation
- [func AudioCodecInitialize(AudioCodec, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioStreamBasicDescription>?, UnsafeRawPointer?, UInt32) -> OSStatus](./audiocodecinitialize%28_,_,_,_,_%29.md)
  Sets up the specified codec to perform a data format translation.
- [func AudioCodecGetProperty(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiocodecgetproperty%28_,_,_,_%29.md)
  Retrieves the value of a codec property.
### Accessing the Data
- [func AudioCodecAppendInputData(AudioCodec, UnsafeRawPointer, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus](./audiocodecappendinputdata%28_,_,_,_,_%29.md)
  Appends audio data to the codec’s input buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecproduceoutputpackets(_:_:_:_:_:_:))*