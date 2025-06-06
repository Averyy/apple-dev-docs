# NSKeyValueChangeKey

**Framework**: Foundation  
**Kind**: struct

The keys that can appear in the change dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct NSKeyValueChangeKey
```

#### Discussion

These constants are used as keys in the change dictionary passed to [`observeValue(forKeyPath:of:change:context:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/observeValue(forKeyPath:of:change:context:)).

## Topics

### Type Properties
- [static let indexesKey: NSKeyValueChangeKey](nskeyvaluechangekey/indexeskey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.insertion`](nskeyvaluechange/insertion.md), [`NSKeyValueChange.removal`](nskeyvaluechange/removal.md), or [`NSKeyValueChange.replacement`](nskeyvaluechange/replacement.md), the value of this key is an `NSIndexSet` object that contains the indexes of the inserted, removed, or replaced objects.
- [static let kindKey: NSKeyValueChangeKey](nskeyvaluechangekey/kindkey.md)
  An `NSNumber` object that contains a value corresponding to one of the [`NSKeyValueChange`](nskeyvaluechange.md) enums, indicating what sort of change has occurred.
- [static let newKey: NSKeyValueChangeKey](nskeyvaluechangekey/newkey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.setting`](nskeyvaluechange/setting.md), and [`new`](nskeyvalueobservingoptions/new.md) was specified when the observer was registered, the value of this key is the new value for the attribute.
- [static let notificationIsPriorKey: NSKeyValueChangeKey](nskeyvaluechangekey/notificationispriorkey.md)
  If the [`prior`](nskeyvalueobservingoptions/prior.md) option was specified when the observer was registered this notification is sent prior to a change.
- [static let oldKey: NSKeyValueChangeKey](nskeyvaluechangekey/oldkey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.setting`](nskeyvaluechange/setting.md), and [`old`](nskeyvalueobservingoptions/old.md) was specified when the observer was registered, the value of this key is the value before the attribute was changed.
### Initializers
- [init(rawValue: String)](nskeyvaluechangekey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AsyncCharacterSequence](asynccharactersequence.md)
  An asynchronous sequence of characters.
- [struct AsyncLineSequence](asynclinesequence.md)
  An asynchronous sequence of lines of text.
- [struct AsyncUnicodeScalarSequence](asyncunicodescalarsequence.md)
  An asychronous sequence of Unicode scalar values.
- [struct Expression](expression.md)
- [struct NSAttributedStringFormattingContextKey](nsattributedstringformattingcontextkey.md)
- [struct NSKeyValueObservedChange](nskeyvalueobservedchange.md)
- [struct NSKeyValueOperator](nskeyvalueoperator.md)
  These constants define the available array operators. See [`Using Collection Operators`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/CollectionOperators.html) for more information.
- [struct PresentationIntent](presentationintent.md)
  A type that defines presentation intent for blocks of characters like paragraphs, lists, block quotes, and tables.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluechangekey)*