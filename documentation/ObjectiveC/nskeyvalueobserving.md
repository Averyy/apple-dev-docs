# NSKeyValueObserving

**Framework**: Objective-C Runtime

An informal protocol that objects adopt to be notified of changes to the specified properties of other objects.

#### Overview

You can observe any object properties including simple attributes, to-one relationships, and to-many relationships. Observers of to-many relationships are informed of the type of change made — as well as which objects are involved in the change.

[`NSObject`](nsobject-swift.class.md) provides an implementation of the [`NSKeyValueObserving`](nskeyvalueobserving.md) protocol that provides an automatic observing capability for all objects. You can further refine notifications by disabling automatic observer notifications and implementing manual notifications using the methods in this protocol.

## Topics

### Change Notification
- [func observeValue(forKeyPath: String?, of: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?)](nsobject-swift.class/observevalue(forkeypath:of:change:context:).md)
  Informs the observing object when the value at the specified key path relative to the observed object has changed.
### Registering for Observation
- [func addObserver(NSObject, forKeyPath: String, options: NSKeyValueObservingOptions, context: UnsafeMutableRawPointer?)](nsobject-swift.class/addobserver(_:forkeypath:options:context:).md)
  Registers the observer object to receive KVO notifications for the key path relative to the object receiving this message.
- [func removeObserver(NSObject, forKeyPath: String)](nsobject-swift.class/removeobserver(_:forkeypath:).md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message.
- [func removeObserver(NSObject, forKeyPath: String, context: UnsafeMutableRawPointer?)](nsobject-swift.class/removeobserver(_:forkeypath:context:).md)
  Stops the observer object from receiving change notifications for the property specified by the key path relative to the object receiving this message, given the context.
### Notifying Observers of Changes
- [func willChangeValue(forKey: String)](nsobject-swift.class/willchangevalue(forkey:).md)
  Informs the observed object that the value of a given property is about to change.
- [func didChangeValue(forKey: String)](nsobject-swift.class/didchangevalue(forkey:).md)
  Informs the observed object that the value of a given property has changed.
- [func willChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](nsobject-swift.class/willchange(_:valuesat:forkey:).md)
  Informs the observed object that the specified change is about to be executed at given indexes for a specified ordered to-many relationship.
- [func didChange(NSKeyValueChange, valuesAt: IndexSet, forKey: String)](nsobject-swift.class/didchange(_:valuesat:forkey:).md)
  Informs the observed object that the specified change has occurred on the indexes for a specified ordered to-many relationship.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsobject-swift.class/willchangevalue(forkey:withsetmutation:using:).md)
  Informs the observed object that the specified change is about to be made to a specified unordered to-many relationship.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsobject-swift.class/didchangevalue(forkey:withsetmutation:using:).md)
  Informs the observed object that the specified change was made to a specified unordered to-many relationship.
### Observing Customization
- [class func automaticallyNotifiesObservers(forKey: String) -> Bool](nsobject-swift.class/automaticallynotifiesobservers(forkey:).md)
  Returns a Boolean value that indicates whether the observed object supports automatic key-value observation for the given key.
- [class func keyPathsForValuesAffectingValue(forKey: String) -> Set<String>](nsobject-swift.class/keypathsforvaluesaffectingvalue(forkey:).md)
  Returns a set of key paths for properties whose values affect the value of the specified key.
- [protocol NSKeyValueObservingCustomization](../Foundation/NSKeyValueObservingCustomization.md)
  Conforming to NSKeyValueObservingCustomization is not required to use Key-Value Observing. Provide an implementation of these functions if you need to disable auto-notifying for a key, or add dependent keys
- [var observationInfo: UnsafeMutableRawPointer?](nsobject-swift.class/observationinfo.md)
  Returns a pointer that identifies information about all of the observers that are registered with the observed object.
### Constants
- [class NSKeyValueObservation](../Foundation/NSKeyValueObservation.md)
- [struct NSKeyValueObservedChange](../Foundation/NSKeyValueObservedChange.md)
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