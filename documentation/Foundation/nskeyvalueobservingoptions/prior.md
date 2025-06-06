# prior

**Framework**: Foundation  
**Kind**: property

Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.

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
static var prior: NSKeyValueObservingOptions { get }
```

#### Discussion

The change dictionary in a notification sent before a change always contains an [`notificationIsPriorKey`](nskeyvaluechangekey/notificationispriorkey.md) entry whose value is an `NSNumber` object that contains the Boolean value [`true`](https://developer.apple.com/documentation/swift/true), but never contains an [`newKey`](nskeyvaluechangekey/newkey.md) entry. When this option is specified the change dictionary in a notification sent after a change contains the same entries that it would contain if this option were not specified. You can use this option when the observer’s own key-value observing-compliance requires it to invoke one of the `-willChange...` methods for one of its own properties, and the value of that property depends on the value of the observed object’s property. (In that situation it’s too late to easily invoke `-willChange...` properly in response to receiving an [`observeValue(forKeyPath:of:change:context:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/observeValue(forKeyPath:of:change:context:)) message after the change.)

## See Also

- [static var new: NSKeyValueObservingOptions](nskeyvalueobservingoptions/new.md)
  Indicates that the change dictionary should provide the new attribute value, if applicable.
- [static var old: NSKeyValueObservingOptions](nskeyvalueobservingoptions/old.md)
  Indicates that the change dictionary should contain the old attribute value, if applicable.
- [static var initial: NSKeyValueObservingOptions](nskeyvalueobservingoptions/initial.md)
  If specified, a notification should be sent to the observer immediately, before the observer registration method even returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/prior)*