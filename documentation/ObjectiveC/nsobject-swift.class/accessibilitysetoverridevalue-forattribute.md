# accessibilitySetOverrideValue(_:forAttribute:)

**Framework**: Objective-C Runtime  
**Kind**: method

Overrides the specified attribute in the receiver or adds it if it does not exist, and sets its value to the specified value.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func accessibilitySetOverrideValue(_ value: Any?, forAttribute attribute: NSAccessibility.Attribute) -> Bool
```

#### Return Value

[`YES`](yes.md) if the override was successful; otherwise, [`NO`](no.md).

#### Discussion

This method is for changing the set of attributes on an instance, as an alternative to subclassing.

This method works only on objects whose class already implements the `NSAccessibility` protocol. If the specified attribute is already supported by the object, the value specified by this method wins.

If the specified attribute does not exist, it is created outside the `NSAccessibility` protocol, so `accessibilityAttributeNames` still returns the old list, which does not contain the new attribute. Likewise, `accessibilityAttributeValue` does not return attributes created by the override process nor does it return their overridden values.

The values of overridden attributes are not settable by accessibility clients.

If you need to undo the effect of using this method, call it again, passing `nil` for the value.

Ensure that you invoke this method on the actual object that represents the user interface element. For example, for `NSButton`, use the underlying `NSButtonCell` object. `NSButton` itself is ignored by accessibility.

This method works only on an object representing a single user interface element. So, for example, you cannot use it when a single object represents multiple user interface elements, as with `NSSegmentedCell`, which has only a single object but provides user interface elements for each segment.

## Parameters

- `value`: The attribute value to be set.
- `attribute`: The name of the attribute. See   constants for lists of attribute names.

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
- [func accessibilitySetValue(Any?, forAttribute: NSAccessibility.Attribute)](nsobject-swift.class/accessibilitysetvalue(_:forattribute:).md)
  Sets the value of the specified attribute in the receiver to the specified value.
- [func fileManager(FileManager, shouldProceedAfterError: [AnyHashable : Any]) -> Bool](nsobject-swift.class/filemanager(_:shouldproceedaftererror:).md)
  An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.
- [func fileManager(FileManager, willProcessPath: String)](nsobject-swift.class/filemanager(_:willprocesspath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitysetoverridevalue(_:forattribute:))*