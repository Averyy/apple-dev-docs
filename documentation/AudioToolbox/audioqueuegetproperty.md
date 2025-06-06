# AudioQueueGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Gets an audio queue property value.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioQueueGetProperty(_ inAQ: AudioQueueRef, _ inID: AudioQueuePropertyID, _ outData: UnsafeMutableRawPointer, _ ioDataSize: UnsafeMutablePointer<UInt32>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Before calling this function, you can use the [`AudioQueueGetPropertySize(_:_:_:)`](audioqueuegetpropertysize(_:_:_:).md) function to determine the size, in bytes, of the value of a specified property. Some properties have values of a specific size, as described in [`AudioQueuePropertyID`](audioqueuepropertyid.md).

##### Special Considerations

Some Core Audio property values are C types and others are Core Foundation objects.

If you call this function to retrieve a value that is a Core Foundation object, then this function—despite the use of “Get” in its name—duplicates the object. You are responsible for releasing the object, as described in [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029) in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## Parameters

- `inAQ`: The audio queue that you want to get a property value from.
- `inID`: The ID of the property whose value you want to get. See  .
- `outData`: On output, the desired property value.
- `ioDataSize`: On input, the maximum bytes of space the caller expects to receive. On output, the actual data size of the property value.

## See Also

- [func AudioQueueSetProperty(AudioQueueRef, AudioQueuePropertyID, UnsafeRawPointer, UInt32) -> OSStatus](audioqueuesetproperty(_:_:_:_:).md)
  Sets an audio queue property value.
- [func AudioQueueGetPropertySize(AudioQueueRef, AudioQueuePropertyID, UnsafeMutablePointer<UInt32>) -> OSStatus](audioqueuegetpropertysize(_:_:_:).md)
  Gets the size of the value of an audio queue property.
- [func AudioQueueAddPropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueaddpropertylistener(_:_:_:_:).md)
  Adds a property listener callback to an audio queue.
- [func AudioQueueRemovePropertyListener(AudioQueueRef, AudioQueuePropertyID, AudioQueuePropertyListenerProc, UnsafeMutableRawPointer?) -> OSStatus](audioqueueremovepropertylistener(_:_:_:_:).md)
  Removes a property listener callback from an audio queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioqueuegetproperty(_:_:_:_:))*