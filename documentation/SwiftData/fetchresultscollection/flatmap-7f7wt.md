# flatMap(_:)

**Framework**: SwiftData  
**Kind**: method

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift ?+

## Declaration

```swift
func flatMap<ElementOfResult>(_ transform: (Self.Element) throws -> ElementOfResult?) rethrows -> [ElementOfResult]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/fetchresultscollection/flatmap(_:)-7f7wt)*