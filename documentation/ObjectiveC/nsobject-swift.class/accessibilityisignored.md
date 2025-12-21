# accessibilityIsIgnored()

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a Boolean value indicating whether the receiver should be ignored in the parent-child accessibility hierarchy.

**Availability**:
- macOS 10.1+

## Declaration

```swift
func accessibilityIsIgnored() -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiver should be ignored; otherwise, [`NO`](no.md).

#### Discussion

When asking for an object’s children, do not include ignored children; instead, replace the ignored children with their own unignored children. The same applies when asking for an object’s parent: skip the ignored parent and treat the first unignored ancestor as the real parent.  Likewise, when a hit-test or focus test is satisfied by an ignored element, use the element’s first unignored ancestor (or descendant in certain cases, such as single-celled controls) instead.

Ignored elements let you provide a simplified version of the view and object ownership hierarchies. Accessibility clients can bypass intermediate objects, letting users access the real user interface objects more quickly. For example, `NSControl` objects are ignored when they are single-celled; the visible parent-child relationship is between the control’s parent (or a higher ancestor if the parent is ignored, too) and the control’s cell.

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
- [func fileManager(FileManager, willProcessPath: String)](nsobject-swift.class/filemanager(_:willprocesspath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilityisignored())*