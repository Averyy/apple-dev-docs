# writeAttributeWriteOnlyInt8u(withValue:params:completionHandler:)

**Framework**: Matter  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.2+ - Deprecated in 16.4
- iPadOS 16.2+ - Deprecated in 16.4
- Mac Catalyst 16.2+ - Deprecated in 16.4
- macOS 13.1+ - Deprecated in 13.3
- tvOS 16.2+ - Deprecated in 16.4
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.2+ - Deprecated in 9.4

> **Deprecated**: Please use writeAttributeWriteOnlyInt8uWithValue:params:completion:

## Declaration

```swift
func writeAttributeWriteOnlyInt8u(withValue value: NSNumber, params: MTRWriteParams?, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func writeAttributeWriteOnlyInt8u(withValue value: NSNumber, params: MTRWriteParams?) async throws
```

```objc
- (void) writeAttributeWriteOnlyInt8uWithValue:(NSNumber *) value params:(MTRWriteParams *) params completionHandler:(MTRStatusCompletion) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrbaseclustertestcluster/writeattributewriteonlyint8u(withvalue:params:completionhandler:))*