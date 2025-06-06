# setValidationHandler(_:)

**Framework**: Core Media  
**Kind**: method

Sets validation handler for the queue to call before enqueuing buffers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func setValidationHandler(_ body: @escaping (CMBufferQueue, CMBuffer) throws -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueue/setvalidationhandler(_:))*