# initial

**Framework**: Foundation  
**Kind**: property

If specified, a notification should be sent to the observer immediately, before the observer registration method even returns.

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
static var initial: NSKeyValueObservingOptions { get }
```

#### Discussion

The change dictionary in the notification will always contain an [`newKey`](nskeyvaluechangekey/newkey.md) entry if [`new`](nskeyvalueobservingoptions/new.md) is also specified but will never contain an [`oldKey`](nskeyvaluechangekey/oldkey.md) entry. (In an initial notification the current value of the observed property may be old, but it’s new to the observer.) You can use this option instead of explicitly invoking, at the same time, code that is also invoked by the observer’s doc://com.apple.documentation/documentation/objectivec/nsobject/1416553-observevalue method. When this option is used withdoc://com.apple.documentation/documentation/objectivec/nsobject/1412787-addobserver a notification will be sent for each indexed object to which the observer is being added.

## See Also

- [static var new: NSKeyValueObservingOptions](nskeyvalueobservingoptions/new.md)
  Indicates that the change dictionary should provide the new attribute value, if applicable.
- [static var old: NSKeyValueObservingOptions](nskeyvalueobservingoptions/old.md)
  Indicates that the change dictionary should contain the old attribute value, if applicable.
- [static var prior: NSKeyValueObservingOptions](nskeyvalueobservingoptions/prior.md)
  Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/initial)*