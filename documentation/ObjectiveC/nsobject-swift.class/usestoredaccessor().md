# useStoredAccessor()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Returns `true` if the stored value methods [`storedValue(forKey:)`](./storedvalue%28forkey%29.md) and [`takeStoredValue(_:forKey:)`](./takestoredvalue%28_,forkey%29.md) should use private accessor methods in preference to public accessors.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: This method has no direct replacement, although see [`accessInstanceVariablesDirectly`](./accessinstancevariablesdirectly.md).

## Declaration

```swift
class func useStoredAccessor() -> Bool
```

```objc
+ (BOOL) useStoredAccessor;
```

#### Discussion

Returning [`NO`](../no.md) causes the stored value methods to use the same accessor method or instance variable search order as the corresponding basic key-value coding methods ([`value(forKey:)`](./value%28forkey%29.md) and [`takeValue(_:forKey:)`](./takevalue%28_,forkey%29.md)). The default implementation returns [`YES`](../yes.md).

Applications should use the `valueForKey:` and `setValue:forKey:` methods instead of `storedValueForKey:` and `takeStoredValue:forKey:`.

## See Also

### Deprecated Class Methods
- [class func defaultPlaceholder(for: Any?, with: NSBindingName) -> Any?](./defaultplaceholder%28for,with%29.md)
  Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func setDefaultPlaceholder(Any?, for: Any?, with: NSBindingName)](./setdefaultplaceholder%28_,for,with%29.md)
  Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [+ setKeys:triggerChangeNotificationsForDependentKey:](./setkeys_triggerchangenotificationsfordependentkey_.md)
  Configures the observed object to post change notifications for a given property if any of the properties specified in a given array changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/usestoredaccessor())*