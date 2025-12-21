# fileManager(_:shouldProceedAfterError:)

**Framework**: Objective-C Runtime  
**Kind**: method

An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool
```

#### Return Value

[`YES`](yes.md) if the operation (which is often continuous within a loop) should proceed, otherwise [`NO`](no.md).

#### Discussion

An `NSFileManager` object, `manager`, sends this message for each error it encounters when copying, moving, removing, or linking files or directories. The return value is passed back to the invoker of [`copyPath:toPath:handler:`](https://developer.apple.com/documentation/Foundation/NSFileManager/copyPath:toPath:handler:), [`movePath:toPath:handler:`](https://developer.apple.com/documentation/Foundation/NSFileManager/movePath:toPath:handler:), [`removeFileAtPath:handler:`](https://developer.apple.com/documentation/Foundation/NSFileManager/removeFileAtPath:handler:), or [`linkPath:toPath:handler:`](https://developer.apple.com/documentation/Foundation/NSFileManager/linkPath:toPath:handler:). If an error occurs and your handler has not implemented this method, the invoking method automatically returns [`NO`](no.md).

## Parameters

- `fm`: The file manager that sent this message.
- `errorInfo`: A dictionary that contains two or three pieces of information (all   objects) related to the error:

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
- [func fileManager(FileManager, willProcessPath: String)](nsobject-swift.class/filemanager(_:willprocesspath:).md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/filemanager(_:shouldproceedaftererror:))*