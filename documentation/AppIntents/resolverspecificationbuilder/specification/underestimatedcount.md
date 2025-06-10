# underestimatedCount

**Framework**: App Intents  
**Kind**: property

A value less than or equal to the number of elements in the sequence, calculated nondestructively.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var underestimatedCount: Int { get }
```

#### Discussion

The default implementation returns 0. If you provide your own implementation, make sure to compute the value nondestructively.

> **Note**: O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/resolverspecificationbuilder/specification/underestimatedcount)*