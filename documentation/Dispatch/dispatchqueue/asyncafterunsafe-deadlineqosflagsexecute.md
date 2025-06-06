# asyncAfterUnsafe(deadline:qos:flags:execute:)

**Framework**: Dispatch  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
func asyncAfterUnsafe(deadline: DispatchTime, qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], execute work: @escaping () -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/asyncafterunsafe(deadline:qos:flags:execute:))*