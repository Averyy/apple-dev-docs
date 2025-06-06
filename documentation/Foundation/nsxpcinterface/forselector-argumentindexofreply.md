# forSelector(_:argumentIndex:ofReply:)

**Framework**: Foundation  
**Kind**: method

Returns the interface previously set for the specified selector and parameter.

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
func forSelector(_ sel: Selector, argumentIndex arg: Int, ofReply: Bool) -> NSXPCInterface?
```

#### Discussion

See [`setInterface(_:for:argumentIndex:ofReply:)`](nsxpcinterface/setinterface(_:for:argumentindex:ofreply:).md) for more explanation.

## Parameters

- `sel`: Specifies which method in the protocol you want information about.
- `arg`: Specifies the position (starting at index 0) of the parameter for which you want to obtain the current interface. This may be either the position of a parameter in the method itself or the position in its reply block.
- `ofReply`: Pass   if   is an index into the parameters of the reply block, or   if it is an index into the parameters of the method itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcinterface/forselector(_:argumentindex:ofreply:))*