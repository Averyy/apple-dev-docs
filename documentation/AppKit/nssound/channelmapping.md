# channelMapping

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Provides the receiver’s channel map.

**Availability**:
- macOS 10.5+ - Deprecated in 10.9

## Declaration

```objc
- (NSArray *) channelMapping;
```

## Return Value

The receiver’s audio-channel–to–device–channel mappings.

## Discussion

A **channel map** correlates a sound’s channels to the output-device’s channels. For example, a two-channel sound being played on a five-channel device should have a channel map to optimize the sound-playing experience. The default map, correlates the first sound channel to the first output channel, the second sound channel to the second output channel, and so on.

For details about channel maps, see [Core Audio Overview](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003577) > “[Common Tasks in OS X](https://developer.apple.com/library/archive/documentation/MusicAudio/Conceptual/CoreAudioOverview/ARoadmaptoCommonTasks/ARoadmaptoCommonTasks.html#//apple_ref/doc/uid/TP40003577-CH6).”

## See Also

### Deprecated
- [- setChannelMapping:](./setchannelmapping_.md)
  Specifies the receiver’s channel map.
- [+ soundUnfilteredFileTypes](./soundunfilteredfiletypes.md)
  Provides the list of file types the [`NSSound`](../nssound.md) class understands.
- [+ soundUnfilteredPasteboardTypes](./soundunfilteredpasteboardtypes.md)
  Provides a list of the pasteboard types that the `NSSound` class can accept.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssound/channelmapping)*