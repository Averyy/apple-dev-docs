# NSKeyValueObserving

**Framework**: Objective-C Runtime

An informal protocol that objects adopt to be notified of changes to the specified properties of other objects.

#### Overview

You can observe any object properties including simple attributes, to-one relationships, and to-many relationships. Observers of to-many relationships are informed of the type of change made — as well as which objects are involved in the change.

[`NSObject`](nsobject-swift.class.md) provides an implementation of the [`NSKeyValueObserving`](nskeyvalueobserving.md) protocol that provides an automatic observing capability for all objects. You can further refine notifications by disabling automatic observer notifications and implementing manual notifications using the methods in this protocol.

## Topics

### Observing Customization
- [protocol NSKeyValueObservingCustomization : NSObjectProtocol](../Foundation/NSKeyValueObservingCustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
### Constants
- [@objc(_NSKeyValueObservation) class NSKeyValueObservation](../Foundation/NSKeyValueObservation.md)
- [struct NSKeyValueObservedChange<Value>](../Foundation/NSKeyValueObservedChange.md)
- [enum NSKeyValueChange](../Foundation/NSKeyValueChange.md)
  The kinds of changes that can be observed.
- [struct NSKeyValueObservingOptions](../Foundation/NSKeyValueObservingOptions.md)
  The values that can be returned in a change dictionary.
- [struct NSKeyValueChangeKey](../Foundation/NSKeyValueChangeKey.md)
  The keys that can appear in the change dictionary.
- [enum NSKeyValueSetMutationKind](../Foundation/NSKeyValueSetMutationKind.md)

## See Also

- [Key-Value Observing Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nskeyvalueobserving)*