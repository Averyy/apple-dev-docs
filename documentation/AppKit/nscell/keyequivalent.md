# keyEquivalent

**Framework**: AppKit  
**Kind**: property

The key equivalent associated with clicking the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var keyEquivalent: String { get }
```

#### Discussion

Subclasses can override this property and return a string with a valid character for the key equivalent. The default implementation of this property returns an empty string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/keyequivalent)*