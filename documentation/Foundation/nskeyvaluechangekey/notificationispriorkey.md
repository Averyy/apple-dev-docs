# notificationIsPriorKey

**Framework**: Foundation  
**Kind**: property

If the [`prior`](nskeyvalueobservingoptions/prior.md) option was specified when the observer was registered this notification is sent prior to a change.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let notificationIsPriorKey: NSKeyValueChangeKey
```

#### Discussion

The change dictionary contains an [`notificationIsPriorKey`](nskeyvaluechangekey/notificationispriorkey.md) entry whose value is an `NSNumber` object that contains the Boolean value [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [static let indexesKey: NSKeyValueChangeKey](nskeyvaluechangekey/indexeskey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.insertion`](nskeyvaluechange/insertion.md), [`NSKeyValueChange.removal`](nskeyvaluechange/removal.md), or [`NSKeyValueChange.replacement`](nskeyvaluechange/replacement.md), the value of this key is an `NSIndexSet` object that contains the indexes of the inserted, removed, or replaced objects.
- [static let kindKey: NSKeyValueChangeKey](nskeyvaluechangekey/kindkey.md)
  An `NSNumber` object that contains a value corresponding to one of the [`NSKeyValueChange`](nskeyvaluechange.md) enums, indicating what sort of change has occurred.
- [static let newKey: NSKeyValueChangeKey](nskeyvaluechangekey/newkey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.setting`](nskeyvaluechange/setting.md), and [`new`](nskeyvalueobservingoptions/new.md) was specified when the observer was registered, the value of this key is the new value for the attribute.
- [static let oldKey: NSKeyValueChangeKey](nskeyvaluechangekey/oldkey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.setting`](nskeyvaluechange/setting.md), and [`old`](nskeyvalueobservingoptions/old.md) was specified when the observer was registered, the value of this key is the value before the attribute was changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluechangekey/notificationispriorkey)*