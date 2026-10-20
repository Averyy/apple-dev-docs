# xpcType(for:argumentIndex:ofReply:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func xpcType(for sel: Selector, argumentIndex arg: Int, ofReply: Bool) -> xpc_type_t?
```

```objc
- (xpc_type_t) XPCTypeForSelector:(SEL) sel argumentIndex:(NSUInteger) arg ofReply:(BOOL) ofReply;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcinterface/xpctype(for:argumentindex:ofreply:))*