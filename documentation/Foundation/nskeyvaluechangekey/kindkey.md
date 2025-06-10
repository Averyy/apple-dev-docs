# kindKey

**Framework**: Foundation  
**Kind**: property

An `NSNumber` object that contains a value corresponding to one of the [`NSKeyValueChange`](nskeyvaluechange.md) enums, indicating what sort of change has occurred.

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
static let kindKey: NSKeyValueChangeKey
```

#### Discussion

A value of [`NSKeyValueChange.setting`](nskeyvaluechange/setting.md) indicates that the observed object has received a doc://com.apple.documentation/documentation/objectivec/nsobject/1415969-setvalue message, or that the key-value-coding-compliant set method for the key has been invoked, or that one of the doc://com.apple.documentation/documentation/objectivec/nsobject/1416222-willchangevalue or doc://com.apple.documentation/documentation/objectivec/nsobject/1411809-didchangevalue methods has otherwise been invoked.

A value of [`NSKeyValueChange.insertion`](nskeyvaluechange/insertion.md), [`NSKeyValueChange.removal`](nskeyvaluechange/removal.md), or [`NSKeyValueChange.replacement`](nskeyvaluechange/replacement.md) indicates that mutating messages have been sent a key-value observing compliant collection proxy, or that one of the key-value-coding-compliant collection mutation methods for the key has been invoked, or a collection will change or did change method has been otherwise been invoked.

You can use the [`uintValue`](nsnumber/uintvalue.md) method on the `NSNumber` object to retrieve the value of the change kind.

## See Also

- [static let indexesKey: NSKeyValueChangeKey](nskeyvaluechangekey/indexeskey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.insertion`](nskeyvaluechange/insertion.md), [`NSKeyValueChange.removal`](nskeyvaluechange/removal.md), or [`NSKeyValueChange.replacement`](nskeyvaluechange/replacement.md), the value of this key is an `NSIndexSet` object that contains the indexes of the inserted, removed, or replaced objects.
- [static let newKey: NSKeyValueChangeKey](nskeyvaluechangekey/newkey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.setting`](nskeyvaluechange/setting.md), and [`new`](nskeyvalueobservingoptions/new.md) was specified when the observer was registered, the value of this key is the new value for the attribute.
- [static let notificationIsPriorKey: NSKeyValueChangeKey](nskeyvaluechangekey/notificationispriorkey.md)
  If the [`prior`](nskeyvalueobservingoptions/prior.md) option was specified when the observer was registered this notification is sent prior to a change.
- [static let oldKey: NSKeyValueChangeKey](nskeyvaluechangekey/oldkey.md)
  If the value of the [`kindKey`](nskeyvaluechangekey/kindkey.md) entry is [`NSKeyValueChange.setting`](nskeyvaluechange/setting.md), and [`old`](nskeyvalueobservingoptions/old.md) was specified when the observer was registered, the value of this key is the value before the attribute was changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluechangekey/kindkey)*