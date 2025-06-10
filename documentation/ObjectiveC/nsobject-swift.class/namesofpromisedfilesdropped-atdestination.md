# namesOfPromisedFilesDropped(atDestination:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns the names of the files that the receiver promises to create at a specified location.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func namesOfPromisedFilesDropped(atDestination dropDestination: URL) -> [String]?
```

#### Return Value

An array of the names of files (not full paths) that the receiver promises to create at `dropDestination`.

#### Discussion

This method is invoked when the drop has been accepted by the destination and the destination, in the case of another Cocoa application, invokes the NSDraggingInfo method [`namesOfPromisedFilesDropped(atDestination:)`](https://developer.apple.com/documentation/AppKit/NSDraggingInfo/namesOfPromisedFilesDropped(atDestination:)). For long operations, you can cache `dropDestination` and defer the creation of the files until the `draggedImage:endedAt:operation:` method to avoid blocking the destination application.

## Parameters

- `dropDestination`: A URL object that identifies the location at which the promised files will be created.

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
- [func finalize()](nsobject-swift.class/finalize.md)
  The garbage collector invokes this method on the receiver before disposing of the memory it uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/namesofpromisedfilesdropped(atdestination:))*