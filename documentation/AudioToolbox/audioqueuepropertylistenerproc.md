# AudioQueuePropertyListenerProc

**Framework**: Audio Toolbox  
**Kind**: typealias

Called by the system when a specified audio queue property changes value.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioQueuePropertyListenerProc = (UnsafeMutableRawPointer?, AudioQueueRef, AudioQueuePropertyID) -> Void
```

#### Discussion

If you name your callback function `MyAudioQueuePropertyListenerProc`, you would declare it like this:

##### Discussion

Install this callback in an audio queue by calling the [`AudioQueueAddPropertyListener(_:_:_:_:)`](audioqueueaddpropertylistener(_:_:_:_:).md) function. For example, say you want your application to be notified, after you call the [`AudioQueueStop(_:_:)`](audioqueuestop(_:_:).md) function with the `inImmedate` parameter set to `false`, that audio has finished playing. Perform these steps:

1. Define this property listener callback function to listen for changes to the [`kAudioQueueProperty_IsRunning`](kaudioqueueproperty_isrunning.md) property.
2. Install this callback, using the [`AudioQueueAddPropertyListener(_:_:_:_:)`](audioqueueaddpropertylistener(_:_:_:_:).md) function, in the playback audio queue that you want to monitor.

## Parameters

- `inUserData`: The custom data you’ve specified in the   parameter of the   function.
- `inAQ`: The recording or playback audio queue that invoked the callback.
- `inID`: The ID of the property whose value changes you want to observe.

## See Also

- [typealias AudioQueueInputCallback](audioqueueinputcallback.md)
  Called by the system when a recording audio queue has finished filling an audio queue buffer.
- [typealias AudioQueueOutputCallback](audioqueueoutputcallback.md)
  Called by the system when an audio queue buffer is available for reuse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuepropertylistenerproc)*