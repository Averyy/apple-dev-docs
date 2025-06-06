# init(_:comparator:order:)

**Framework**: Foundation  
**Kind**: init

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(_ keyPath: any KeyPath<Compared, String?> & Sendable, comparator: String.StandardComparator = .localizedStandard, order: SortOrder) where Compared : NSObject
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/sortdescriptor/init(_:comparator:order:)-76h8b)*