# storedValue(forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns the property identified by a given key.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: If you are using the `NSManagedObject` class, use [`primitiveValue(forKey:)`](../../CoreData/nsmanagedobject/primitivevalue%28forkey%29.md) instead.

## Declaration

```swift
func storedValue(forKey key: String) -> Any?
```

```objc
- (id) storedValueForKey:(NSString *) key;
```

#### Discussion

This method is used when the value is retrieved for storage in an object store (generally, this storage is ultimately in a database) or for inclusion in a snapshot. The default implementation is similar to the implementation of [`value(forKey:)`](./value%28forkey%29.md), but it resolves `key` with a different method/instance variable search order:

1. Searches for a private accessor method based on `key` (a method preceded by an underbar). For example, with a `key` of “lastName”, [`storedValue(forKey:)`](./storedvalue%28forkey%29.md) looks for a method named `_getLastName` or `_lastName`.
2. If a private accessor is not found, searches for an instance variable based on `key` and returns its value directly. For example, with a `key` of “lastName”, [`storedValue(forKey:)`](./storedvalue%28forkey%29.md) looks for an instance variable named `_lastName` or `lastName`.
3. If neither a private accessor nor an instance variable is found, [`storedValue(forKey:)`](./storedvalue%28forkey%29.md) searches for a public accessor method based on `key`. For the `key` “lastName”, this would be `getLastName` or `lastName`.
4. If `key` is unknown, [`storedValue(forKey:)`](./storedvalue%28forkey%29.md) calls [`handleTakeValue(_:forUnboundKey:)`](./handletakevalue%28_,forunboundkey%29.md).

This different search order allows an object to bypass processing that is performed before returning a value through a public API. However, if you always want to use the search order in [`value(forKey:)`](./value%28forkey%29.md), you can implement the class method [`useStoredAccessor()`](./usestoredaccessor%28%29.md) to return [`NO`](../no.md). And as with [`value(forKey:)`](./value%28forkey%29.md), you can prevent direct access of an instance variable with the class method [`accessInstanceVariablesDirectly`](./accessinstancevariablesdirectly.md).

## See Also

### Deprecated Methods
- [func accessibilityAttributeNames() -> [NSAccessibility.Attribute]](./accessibilityattributenames%28%29.md)
  Returns an array of attribute names supported by the receiver.
- [func accessibilityAttributeValue(NSAccessibility.Attribute) -> Any?](./accessibilityattributevalue%28_%29.md)
  Returns the value of the specified attribute in the receiver.
- [func accessibilityAttributeValue(NSAccessibility.ParameterizedAttribute, forParameter: Any?) -> Any?](./accessibilityattributevalue%28_,forparameter%29.md)
  Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter.
- [func accessibilityActionDescription(NSAccessibility.Action) -> String?](./accessibilityactiondescription%28_%29.md)
  Returns a localized description of the specified action.
- [func accessibilityActionNames() -> [NSAccessibility.Action]](./accessibilityactionnames%28%29.md)
  Returns an array of action names supported by the accessibility element.
- [func accessibilityArrayAttributeCount(NSAccessibility.Attribute) -> Int](./accessibilityarrayattributecount%28_%29.md)
  Returns the count of the specified accessibility array attribute.
- [func accessibilityArrayAttributeValues(NSAccessibility.Attribute, index: Int, maxCount: Int) -> [Any]](./accessibilityarrayattributevalues%28_,index,maxcount%29.md)
  Returns a subarray of values of an accessibility array attribute.
- [func accessibilityIndex(ofChild: Any) -> Int](./accessibilityindex%28ofchild%29.md)
  Returns the index of the specified accessibility child in the parent.
- [func accessibilityIsAttributeSettable(NSAccessibility.Attribute) -> Bool](./accessibilityisattributesettable%28_%29.md)
  Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set.
- [func accessibilityIsIgnored() -> Bool](./accessibilityisignored%28%29.md)
  Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy.
- [func accessibilityParameterizedAttributeNames() -> [NSAccessibility.ParameterizedAttribute]](./accessibilityparameterizedattributenames%28%29.md)
  Returns a list of parameterized attribute names supported by the receiver.
- [func accessibilityPerformAction(NSAccessibility.Action)](./accessibilityperformaction%28_%29.md)
  Performs the action associated with the specified action.
- [func accessibilitySetOverrideValue(Any?, forAttribute: NSAccessibility.Attribute) -> Bool](./accessibilitysetoverridevalue%28_,forattribute%29.md)
  Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value.
- [func accessibilitySetValue(Any?, forAttribute: NSAccessibility.Attribute)](./accessibilitysetvalue%28_,forattribute%29.md)
  Sets the value of the specified attribute in the receiver to the specified value.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](./filemanager%28_,shouldproceedaftererror%29.md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/storedvalue(forkey:))*