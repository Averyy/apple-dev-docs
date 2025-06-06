# className

**Framework**: Foundation  
**Kind**: property

Returns the name of the class the receiver describes, as provided at initialization time.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var className: String? { get }
```

#### Return Value

A class name. This may be either the human-readable name for the class—that is, the name that is used in a script—or the name of the Objective-C class that is instantiated to implement the class. To reliably obtain the implementation name, use [`implementationClassName`](nsscriptclassdescription/implementationclassname.md).

## See Also

- [var defaultSubcontainerAttributeKey: String?](nsscriptclassdescription/defaultsubcontainerattributekey.md)
  Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [var implementationClassName: String?](nsscriptclassdescription/implementationclassname.md)
  Returns the name of the Objective-C class instantiated to implement the scripting class.
- [func isLocationRequiredToCreate(forKey: String) -> Bool](nsscriptclassdescription/islocationrequiredtocreate(forkey:).md)
  Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.
- [var suiteName: String?](nsscriptclassdescription/suitename.md)
  Returns the name of the receiver’s suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/classname)*