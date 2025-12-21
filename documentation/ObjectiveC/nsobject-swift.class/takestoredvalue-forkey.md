# takeStoredValue(_:forKey:)

**Framework**: Objective-C Runtime  
**Kind**: method

Sets the value of the property identified by a given key.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func takeStoredValue(_ value: Any?, forKey key: String)
```

#### Discussion

This method is used to initialize the receiver with values from an object store (generally, this storage is ultimately from a database) or to restore a value from a snapshot. The default implementation is similar to the implementation of [`takeValue(_:forKey:)`](nsobject-swift.class/takevalue(_:forkey:).md), but it resolves `key` with a different method/instance variable search order:

1. Searches for a private accessor method based on `key` (a method preceded by an underbar). For example, with a `key` of “lastName”, [`takeStoredValue(_:forKey:)`](nsobject-swift.class/takestoredvalue(_:forkey:).md) looks for a method named `_setLastName:`.
2. If a private accessor is not found, searches for an instance variable based on `key` and sets its `value` directly. For example, with a `key` of “lastName”, [`takeStoredValue(_:forKey:)`](nsobject-swift.class/takestoredvalue(_:forkey:).md) looks for an instance variable named `_lastName` or `lastName`.
3. If neither a private accessor nor an instance variable is found, [`takeStoredValue(_:forKey:)`](nsobject-swift.class/takestoredvalue(_:forkey:).md) searches for a public accessor method based on `key`. For the `key` “lastName”, this would be `setLastName:`.
4. If `key` is unknown, [`takeStoredValue(_:forKey:)`](nsobject-swift.class/takestoredvalue(_:forkey:).md) calls [`handleTakeValue(_:forUnboundKey:)`](nsobject-swift.class/handletakevalue(_:forunboundkey:).md).

This different search order allows an object to bypass processing that is performed before setting a value through a public API. However, if you always want to use the search order in [`takeValue(_:forKey:)`](nsobject-swift.class/takevalue(_:forkey:).md), you can implement the class method [`useStoredAccessor()`](nsobject-swift.class/usestoredaccessor().md) to return [`NO`](no.md). And as with [`value(forKey:)`](nsobject-swift.class/value(forkey:).md), you can prevent direct access of an instance variable with the class method [`accessInstanceVariablesDirectly`](nsobject-swift.class/accessinstancevariablesdirectly.md).

## See Also

- [func accessibilityAttributeNames() -> [NSAccessibility.Attribute]](nsobject-swift.class/accessibilityattributenames.md)
  Returns an array of attribute names supported by the receiver.
- [func accessibilityAttributeValue(NSAccessibility.Attribute) -> Any?](nsobject-swift.class/accessibilityattributevalue(_:).md)
  Returns the value of the specified attribute in the receiver.
- [func accessibilityAttributeValue(NSAccessibility.ParameterizedAttribute, forParameter: Any?) -> Any?](nsobject-swift.class/accessibilityattributevalue(_:forparameter:).md)
  Returns the value of the receiver’s parameterized attribute corresponding to the specified attribute name and parameter.
- [func accessibilityActionDescription(NSAccessibility.Action) -> String?](nsobject-swift.class/accessibilityactiondescription(_:).md)
  Returns a localized description of the specified action.
- [func accessibilityActionNames() -> [NSAccessibility.Action]](nsobject-swift.class/accessibilityactionnames.md)
  Returns an array of action names supported by the accessibility element.
- [func accessibilityArrayAttributeCount(NSAccessibility.Attribute) -> Int](nsobject-swift.class/accessibilityarrayattributecount(_:).md)
  Returns the count of the specified accessibility array attribute.
- [func accessibilityArrayAttributeValues(NSAccessibility.Attribute, index: Int, maxCount: Int) -> [Any]](nsobject-swift.class/accessibilityarrayattributevalues(_:index:maxcount:).md)
  Returns a subarray of values of an accessibility array attribute.
- [func accessibilityIndex(ofChild: Any) -> Int](nsobject-swift.class/accessibilityindex(ofchild:).md)
  Returns the index of the specified accessibility child in the parent.
- [func accessibilityIsAttributeSettable(NSAccessibility.Attribute) -> Bool](nsobject-swift.class/accessibilityisattributesettable(_:).md)
  Returns a Boolean value that indicates whether the value for the specified attribute in the receiver can be set.
- [func accessibilityIsIgnored() -> Bool](nsobject-swift.class/accessibilityisignored.md)
  Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy.
- [func accessibilityParameterizedAttributeNames() -> [NSAccessibility.ParameterizedAttribute]](nsobject-swift.class/accessibilityparameterizedattributenames.md)
  Returns a list of parameterized attribute names supported by the receiver.
- [func accessibilityPerformAction(NSAccessibility.Action)](nsobject-swift.class/accessibilityperformaction(_:).md)
  Performs the action associated with the specified action.
- [func accessibilitySetOverrideValue(Any?, forAttribute: NSAccessibility.Attribute) -> Bool](nsobject-swift.class/accessibilitysetoverridevalue(_:forattribute:).md)
  Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value.
- [func accessibilitySetValue(Any?, forAttribute: NSAccessibility.Attribute)](nsobject-swift.class/accessibilitysetvalue(_:forattribute:).md)
  Sets the value of the specified attribute in the receiver to the specified value.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](nsobject-swift.class/filemanager(_:shouldproceedaftererror:).md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/takestoredvalue(_:forkey:))*