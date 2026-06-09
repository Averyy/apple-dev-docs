# MTAudioProcessingTapCreateWithPreferredFormat(_:_:_:_:_:)

**Framework**: Media Toolbox  
**Kind**: func

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func MTAudioProcessingTapCreateWithPreferredFormat(_ allocator: CFAllocator?, _ callbacks: UnsafePointer<MTAudioProcessingTapCallbacks>, _ flags: MTAudioProcessingTapCreationFlags, _ preferredFormat: CMAudioFormatDescription?, _ tapOut: UnsafeMutablePointer<MTAudioProcessingTap?>) -> OSStatus
```

#### Return Value

An OSStatus result code.

#### Discussion

Creates a new processing tap.

This function creates a processing tap. The processing tap will then be used to process decoded data. The processing is performed on audio either before or after any effects or other processing (varispeed, etc) is applied by the audio queue.

## Parameters

- `allocator`: The allocator to use to allocate memory for the new tap. Pass NULL or kCFAllocatorDefault to use the current default allocator.
- `callbacks`: Callbacks struct.  MTAudioProcessingTap will make a copy of this struct.
- `flags`: Flags that are used to control aspects of the processing tap. Valid flags are: - kMTAudioProcessingTapCreationFlag_PreEffects: processing is done before any further effects are applied by the audio queue to the audio.
- kMTAudioProcessingTapCreationFlag_PostEffects: processing is done after all processing is done, including that of other taps.
- `preferredFormat`: A CMAudioFormatDescription for the preferred format of audio processed by the tap. The format ID of the AudioStreamBasicDescription must be kAudioFormatLinearPCM. If the AudioStreamBasicDescription specified a channel count greater than 2, an AudioChannelLayout must also be specified. Because the actual format of the tap may differ from the specified preferred format in its LPCM numeric type, channel interleaving, and sample size, you should provide a prepare callback with particular attention to the mFormatFlags, mBytesPerPacket, and mBitsPerChannel fields of the AudioStreamBasicDescription. If any of these differs from the format in which you wish to operate, you can set up conversions between the tap’s format and your required processing format.
- `tapOut`: The processing tap object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediatoolbox/mtaudioprocessingtapcreatewithpreferredformat(_:_:_:_:_:))*