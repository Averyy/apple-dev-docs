# setKeys:triggerChangeNotificationsForDependentKey:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Configures the observed object to post change notifications for a given property if any of the properties specified in a given array changes.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use the method [`keyPathsForValuesAffectingValue(forKey:)`](./keypathsforvaluesaffectingvalue%28forkey%29.md) instead.

## Declaration

```objc
+ (void) setKeys:(NSArray *) keys triggerChangeNotificationsForDependentKey:(NSString *) dependentKey;
```

## Discussion

Invocations of will- and did-change KVO notification methods for any key in `keys` automatically invokes the corresponding change notification methods for `dependentKey`. The observed object does not receive `willChange` or `didChange` messages to generate the notifications.

Dependencies should be registered before any instances of the receiving class are created, so you typically invoke this method in a class’s [`initialize()`](./initialize%28%29.md) method, as illustrated in the following example.

```objc
+ (void)initialize {
    [self setKeys:@[@"firstName", @"lastName"] triggerChangeNotificationsForDependentKey:@"fullName"];
}
```

## Parameters

- `keys`: The names of the properties upon which the value of the property identified by `dependentKey` depends.
- `dependentKey`: The name of a property whose value depends on the properties specified by `keys`.

## See Also

### Deprecated Class Methods
- [class func defaultPlaceholder(for: Any?, with: NSBindingName) -> Any?](./defaultplaceholder%28for,with%29.md)
  Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func setDefaultPlaceholder(Any?, for: Any?, with: NSBindingName)](./setdefaultplaceholder%28_,for,with%29.md)
  Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func useStoredAccessor() -> Bool](./usestoredaccessor%28%29.md)
  Returns `true` if the stored value methods [`storedValue(forKey:)`](./storedvalue%28forkey%29.md) and [`takeStoredValue(_:forKey:)`](./takestoredvalue%28_,forkey%29.md) should use private accessor methods in preference to public accessors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/setkeys:triggerchangenotificationsfordependentkey:)*