# useStoredAccessor()

**Framework**: Objective-C Runtime  
**Kind**: method

Returns `true` if the stored value methods [`storedValue(forKey:)`](nsobject-swift.class/storedvalue(forkey:).md) and [`takeStoredValue(_:forKey:)`](nsobject-swift.class/takestoredvalue(_:forkey:).md) should use private accessor methods in preference to public accessors.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func useStoredAccessor() -> Bool
```

#### Discussion

Returning [`NO`](no.md) causes the stored value methods to use the same accessor method or instance variable search order as the corresponding basic key-value coding methods ([`value(forKey:)`](nsobject-swift.class/value(forkey:).md) and [`takeValue(_:forKey:)`](nsobject-swift.class/takevalue(_:forkey:).md)). The default implementation returns [`YES`](yes.md).

Applications should use the `valueForKey:` and `setValue:forKey:` methods instead of `storedValueForKey:` and `takeStoredValue:forKey:`.

## See Also

- [class func defaultPlaceholder(for: Any?, with: NSBindingName) -> Any?](nsobject-swift.class/defaultplaceholder(for:with:).md)
  Returns an object that will be used as the placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.
- [class func setDefaultPlaceholder(Any?, for: Any?, with: NSBindingName)](nsobject-swift.class/setdefaultplaceholder(_:for:with:).md)
  Sets `placeholder` as the default placeholder for the `binding`, when a key value coding compliant property of an instance of the receiving class returns the value specified by `marker`, and no other placeholder has been specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/usestoredaccessor())*