# readAttributeNetworkName(completion:)

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
func readAttributeNetworkName(completion: @escaping @Sendable (String?, (any Error)?) -> Void)
```

```swift
func readAttributeNetworkName() async throws -> String
```

```objc
- (void) readAttributeNetworkNameWithCompletion:(void (^)(NSString *value, NSError *error)) completion;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclusterthreadnetworkdiagnostics/readattributenetworkname(completion:))*