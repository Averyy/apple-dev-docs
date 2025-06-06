# classes(for:argumentIndex:ofReply:)

**Framework**: Foundation  
**Kind**: method

Returns the current list of allowed classes that can appear within the specified collection object argument to the specified method.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func classes(for sel: Selector, argumentIndex arg: Int, ofReply: Bool) -> Set<AnyHashable>
```

#### Discussion

See [`setClasses(_:for:argumentIndex:ofReply:)`](nsxpcinterface/setclasses(_:for:argumentindex:ofreply:).md) for more explanation.

## Parameters

- `sel`: Specifies which method in the protocol you want information about.
- `arg`: Specifies the position (starting at index 0) of the parameter for which you want to obtain the current set of allowed classes. This may be either the position of a parameter in the method itself or the position in its reply block.
- `ofReply`: Pass   if   is an index into the parameters of the reply block, or   if it is an index into the parameters of the method itself.

## See Also

- [Daemons and Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcinterface/classes(for:argumentindex:ofreply:))*