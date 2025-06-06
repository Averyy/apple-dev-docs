# cancelOperations()

**Framework**: CloudKit  
**Kind**: method

Cancels any in-progress or pending sync operations.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
final func cancelOperations() async
```

#### Discussion

The sync engine processes cancelation requests asynchronously, meaning it’s possible for in-progress operations to complete even after this method returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/canceloperations())*