# wait(untilSignaledValue:timeoutMS:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func wait(untilSignaledValue value: UInt64, timeoutMS milliseconds: UInt64) -> Bool
```

```objc
- (BOOL) waitUntilSignaledValue:(uint64_t) value timeoutMS:(uint64_t) milliseconds;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsharedevent/wait(untilsignaledvalue:timeoutms:))*