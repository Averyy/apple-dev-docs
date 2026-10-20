# readAttributeBarrierCommandCloseEvents(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+ - Deprecated in 18.2
- iPadOS 16.4+ - Deprecated in 18.2
- Mac Catalyst 16.4+ - Deprecated in 18.2
- macOS 13.3+ - Deprecated in 15.2
- tvOS 16.4+ - Deprecated in 18.2
- visionOS 1.0+ - Deprecated in 2.2
- watchOS 9.4+ - Deprecated in 11.2

> **Deprecated**: This attribute is deprecated

## Declaration

```swift
func readAttributeBarrierCommandCloseEvents(completion: @escaping @Sendable (NSNumber?, (any Error)?) -> Void)
```

```swift
func readAttributeBarrierCommandCloseEvents() async throws -> NSNumber
```

```objc
- (void) readAttributeBarrierCommandCloseEventsWithCompletion:(void (^)(NSNumber *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbarriercontrol/readattributebarriercommandcloseevents(completion:))*