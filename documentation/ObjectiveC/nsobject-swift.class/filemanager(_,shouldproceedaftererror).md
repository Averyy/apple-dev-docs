# fileManager(_:shouldProceedAfterError:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

An `NSFileManager` object sends this message to its handler for each error it encounters when copying, moving, removing, or linking files or directories.

**Availability**:
- iOS 2.0+ - Deprecated in 2.0
- iPadOS 2.0+ - Deprecated in 2.0
- Mac Catalyst 2.0+ - Deprecated in 2.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: See delegate methods for copy, move, remove, and link methods.

## Declaration

```swift
func fileManager(_ fm: FileManager, shouldProceedAfterError errorInfo: [AnyHashable : Any]) -> Bool
```

```objc
- (BOOL) fileManager:(NSFileManager *) fm shouldProceedAfterError:(NSDictionary *) errorInfo;
```

#### Return Value

[`YES`](../yes.md) if the operation (which is often continuous within a loop) should proceed, otherwise [`NO`](../no.md).

#### Discussion

An `NSFileManager` object, `manager`, sends this message for each error it encounters when copying, moving, removing, or linking files or directories. The return value is passed back to the invoker of [`copyPath:toPath:handler:`](../../Foundation/nsfilemanager/copypath_topath_handler_.md), [`movePath:toPath:handler:`](../../Foundation/nsfilemanager/movepath_topath_handler_.md), [`removeFileAtPath:handler:`](../../Foundation/nsfilemanager/removefileatpath_handler_.md), or [`linkPath:toPath:handler:`](../../Foundation/nsfilemanager/linkpath_topath_handler_.md). If an error occurs and your handler has not implemented this method, the invoking method automatically returns [`NO`](../no.md).

## Parameters

- `fm`: The file manager that sent this message.
- `errorInfo`: A dictionary that contains two or three pieces of information (all [`NSString`](../../Foundation/nsstring.md) objects) related to the error:

  | Key | Value |
  | --- | --- |
  | `@"Path"` | The path related to the error (usually the source path) |
  | `@"Error"` | A description of the error |
  | `@"ToPath"` | The destination path (not all errors) |

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
- [func fileManager(FileManager, willProcessPath: String)](./filemanager%28_,willprocesspath%29.md)
  An `NSFileManager` object sends this message to a handler immediately before attempting to move, copy, rename, or delete, or before attempting to link to a given path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/filemanager(_:shouldproceedaftererror:))*