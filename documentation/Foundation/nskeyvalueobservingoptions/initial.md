# initial

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```c
NSKeyValueObservingOptionInitial
```

#### Discussion

The change dictionary in the notification will always contain an [`newKey`](../nskeyvaluechangekey/newkey.md) entry if [`new`](./new.md) is also specified but will never contain an [`oldKey`](../nskeyvaluechangekey/oldkey.md) entry. (In an initial notification the current value of the observed property may be old, but it’s new to the observer.) You can use this option instead of explicitly invoking, at the same time, code that is also invoked by the observer’s [`observeValue(forKeyPath:of:change:context:)`](../../ObjectiveC/nsobject-swift.class/observevalue%28forkeypath,of,change,context%29.md) method. When this option is used with[`addObserver(_:forKeyPath:options:context:)`](../../ObjectiveC/nsobject-swift.class/addobserver%28_,forkeypath,options,context%29.md) a notification will be sent for each indexed object to which the observer is being added.

## See Also

### Constants
- [static var new: NSKeyValueObservingOptions](./new.md)
  Indicates that the change dictionary should provide the new attribute value, if applicable.
- [static var old: NSKeyValueObservingOptions](./old.md)
  Indicates that the change dictionary should contain the old attribute value, if applicable.
- [static var prior: NSKeyValueObservingOptions](./prior.md)
  Whether separate notifications should be sent to the observer before and after each change, instead of a single notification after the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvalueobservingoptions/initial)*