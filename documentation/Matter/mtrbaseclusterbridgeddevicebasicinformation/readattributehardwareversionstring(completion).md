# readAttributeHardwareVersionString(completion:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
func readAttributeHardwareVersionString(completion: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
func readAttributeHardwareVersionString() async throws -> String
```

```objc
- (void) readAttributeHardwareVersionStringWithCompletion:(void (^)(NSString *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterbridgeddevicebasicinformation/readattributehardwareversionstring(completion:))*