# isPartial

**Framework**: Assignables  
**Kind**: property  
**Required**: Yes

Documents are considered partial when they are reconstituted missing one or more of their associated document part IDs. When a document is considered partial it is expected that we shouldn’t be able to both read or write to the parts that the document has neither been reconstituted or merged with.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
var isPartial: Bool { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeablepartscontainer/ispartial)*