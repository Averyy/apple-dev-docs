# defaultSubcontainerAttributeKey

**Framework**: Foundation  
**Kind**: property

Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var defaultSubcontainerAttributeKey: String? { get }
```

#### Return Value

The value of the default subcontainer attribute entry. Returns `nil` if the there was no such entry.

## See Also

- [var className: String?](nsscriptclassdescription/classname.md)
  Returns the name of the class the receiver describes, as provided at initialization time.
- [var implementationClassName: String?](nsscriptclassdescription/implementationclassname.md)
  Returns the name of the Objective-C class instantiated to implement the scripting class.
- [func isLocationRequiredToCreate(forKey: String) -> Bool](nsscriptclassdescription/islocationrequiredtocreate(forkey:).md)
  Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.
- [var suiteName: String?](nsscriptclassdescription/suitename.md)
  Returns the name of the receiver’s suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/defaultsubcontainerattributekey)*