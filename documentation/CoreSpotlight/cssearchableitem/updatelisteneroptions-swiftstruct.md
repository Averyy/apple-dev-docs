# CSSearchableItem.UpdateListenerOptions

**Framework**: Core Spotlight  
**Kind**: struct

The set of options that contain metadata-associated summarization and prioritization of a searchable item.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct UpdateListenerOptions
```

#### Discussion

To receive updates to specific properties on searchable items, implement the [`searchableItemsDidUpdate(_:)`](cssearchableindexdelegate/searchableitemsdidupdate(_:).md) delegate method.

## Topics

### Initializers
- [init(rawValue: UInt)](cssearchableitem/updatelisteneroptions-swift.struct/init(rawvalue:).md)
  An unsigned integer that describes the listener options.
### Type Properties
- [static var priority: CSSearchableItem.UpdateListenerOptions](cssearchableitem/updatelisteneroptions-swift.struct/priority.md)
  A value that describes the listener priority options.
- [static var summarization: CSSearchableItem.UpdateListenerOptions](cssearchableitem/updatelisteneroptions-swift.struct/summarization.md)
  A value that describes the listener summarization options.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitem/updatelisteneroptions-swift.struct)*