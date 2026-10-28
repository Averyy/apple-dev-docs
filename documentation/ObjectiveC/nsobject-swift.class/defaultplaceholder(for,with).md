# defaultPlaceholder(for:with:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```swift
class func defaultPlaceholder(for marker: Any?, with binding: NSBindingName) -> Any?
```

```objc
+ (id) defaultPlaceholderForMarker:(id) marker withBinding:(NSBindingName) binding;
```

## Discussion

The `marker` can be `nil` or one of the constants described in [Selection Markers](../../AppKit/selection-markers.md).

## See Also

### Deprecated Class Methods
- [class func setDefaultPlaceholder(Any?, for: Any?, with: NSBindingName)](./setdefaultplaceholder%28_,for,with%29.md)
  Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func useStoredAccessor() -> Bool](./usestoredaccessor%28%29.md)
  Returns `true` if the stored value methods [`storedValue(forKey:)`](./storedvalue%28forkey%29.md) and [`takeStoredValue(_:forKey:)`](./takestoredvalue%28_,forkey%29.md) should use private accessor methods in preference to public accessors.
- [+ setKeys:triggerChangeNotificationsForDependentKey:](./setkeys_triggerchangenotificationsfordependentkey_.md)
  Configures the observed object to post change notifications for a given property if any of the properties specified in a given array changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/defaultplaceholder(for:with:))*