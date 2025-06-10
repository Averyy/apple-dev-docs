# estimatedAttachmentByteCount

**Framework**: Swift  
**Kind**: property

An estimate of the number of bytes of memory needed to store this value as an attachment.

**Availability**:
- Swift 6.2+
- Xcode 17.0+

## Declaration

```swift
var estimatedAttachmentByteCount: Int? { get }
```

#### Discussion

The testing library uses this property to determine if an attachment should be held in memory or should be immediately persisted to storage. Larger attachments are more likely to be persisted, but the algorithm the testing library uses is an implementation detail and is subject to change.

The value of this property is approximately equal to the number of bytes that will actually be needed, or `nil` if the value cannot be computed efficiently. The default implementation of this property returns `nil`.

> **Note**: O(1) unless `Self` conforms to `Collection`, in which case up to O() where  is the length of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/estimatedattachmentbytecount)*