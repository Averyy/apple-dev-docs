# suiteName

**Framework**: Foundation  
**Kind**: property

Returns the name of the receiver’s suite.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var suiteName: String? { get }
```

#### Return Value

The receiver’s suite name. Within an application’s scriptability information, named suites contain related sets of information.

## See Also

- [var className: String?](nsscriptclassdescription/classname.md)
  Returns the name of the class the receiver describes, as provided at initialization time.
- [var defaultSubcontainerAttributeKey: String?](nsscriptclassdescription/defaultsubcontainerattributekey.md)
  Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [var implementationClassName: String?](nsscriptclassdescription/implementationclassname.md)
  Returns the name of the Objective-C class instantiated to implement the scripting class.
- [func isLocationRequiredToCreate(forKey: String) -> Bool](nsscriptclassdescription/islocationrequiredtocreate(forkey:).md)
  Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/suitename)*