# oldKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

If the value of the [`kindKey`](./kindkey.md) entry is [`NSKeyValueChange.setting`](../nskeyvaluechange/setting.md), and [`old`](../nskeyvalueobservingoptions/old.md) was specified when the observer was registered, the value of this key is the value before the attribute was changed.

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
static let oldKey: NSKeyValueChangeKey
```

```c
extern NSKeyValueChangeKey const NSKeyValueChangeOldKey;
```

## Discussion

For [`NSKeyValueChange.removal`](../nskeyvaluechange/removal.md) or [`NSKeyValueChange.replacement`](../nskeyvaluechange/replacement.md), if [`old`](../nskeyvalueobservingoptions/old.md) was specified when the observer was registered, the value is an `NSArray` instance that contains the objects that have been removed or have been replaced by other objects, respectively.

## See Also

### Type Properties
- [static let indexesKey: NSKeyValueChangeKey](./indexeskey.md)
  If the value of the [`kindKey`](./kindkey.md) entry is [`NSKeyValueChange.insertion`](../nskeyvaluechange/insertion.md), [`NSKeyValueChange.removal`](../nskeyvaluechange/removal.md), or [`NSKeyValueChange.replacement`](../nskeyvaluechange/replacement.md), the value of this key is an `NSIndexSet` object that contains the indexes of the inserted, removed, or replaced objects.
- [static let kindKey: NSKeyValueChangeKey](./kindkey.md)
  An `NSNumber` object that contains a value corresponding to one of the [`NSKeyValueChange`](../nskeyvaluechange.md) enums, indicating what sort of change has occurred.
- [static let newKey: NSKeyValueChangeKey](./newkey.md)
  If the value of the [`kindKey`](./kindkey.md) entry is [`NSKeyValueChange.setting`](../nskeyvaluechange/setting.md), and [`new`](../nskeyvalueobservingoptions/new.md) was specified when the observer was registered, the value of this key is the new value for the attribute.
- [static let notificationIsPriorKey: NSKeyValueChangeKey](./notificationispriorkey.md)
  If the [`prior`](../nskeyvalueobservingoptions/prior.md) option was specified when the observer was registered this notification is sent prior to a change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluechangekey/oldkey)*