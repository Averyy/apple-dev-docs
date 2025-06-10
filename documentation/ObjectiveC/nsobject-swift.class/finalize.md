# finalize()

**Framework**: Objective-C Runtime  
**Kind**: method

The garbage collector invokes this method on the receiver before disposing of the memory it uses.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
func finalize()
```

#### Discussion

The garbage collector invokes this method on the receiver before disposing of the memory it uses. When garbage collection is enabled, this method is invoked instead of `dealloc`.

You can override this method to relinquish resources the receiver has obtained, as shown in the following example:

```objc
- (void)finalize {
    if (log_file != NULL) {
        fclose(log_file);
        log_file = NULL;
    }
    [super finalize];
}
```

Typically, however, you are encouraged to relinquish resources prior to finalization if at all possible. For more details, see Implementing a finalize Method.

##### Special Considerations

It is an error to store `self` into a new or existing live object (colloquially known as “resurrection”), which implies that this method will be called only once. However, the receiver may be messaged after finalization by other objects also being finalized at this time, so your override should guard against future use of resources that have been reclaimed, as shown by the `log_file = NULL` statement in the example. The `finalize` method itself will never be invoked more than once for a given object.

> ❗ **Important**:  `finalize` methods must be thread-safe.

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
- [func fontManager(Any, willIncludeFont: String) -> Bool](nsobject-swift.class/fontmanager(_:willincludefont:).md)
  Requests permission from the Font panel delegate to display the given font name in the Font panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/finalize())*