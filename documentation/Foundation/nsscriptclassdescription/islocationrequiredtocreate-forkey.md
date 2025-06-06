# isLocationRequiredToCreate(forKey:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func isLocationRequiredToCreate(forKey toManyRelationshipKey: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if an insertion location must be specified; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

A script command object that creates a new object in a to-many relationship needs to know whether an explicitly specified insertion location is required. It can get this information from an instance of `NSScriptClassDescription`. For example, `NSMakeCommand` uses this method to determine whether or not a specific `make` AppleScript command must have an `at` parameter.

## Parameters

- `toManyRelationshipKey`: The key for the to-many relationship that may require an insertion location.

## See Also

- [var className: String?](nsscriptclassdescription/classname.md)
  Returns the name of the class the receiver describes, as provided at initialization time.
- [var defaultSubcontainerAttributeKey: String?](nsscriptclassdescription/defaultsubcontainerattributekey.md)
  Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [var implementationClassName: String?](nsscriptclassdescription/implementationclassname.md)
  Returns the name of the Objective-C class instantiated to implement the scripting class.
- [var suiteName: String?](nsscriptclassdescription/suitename.md)
  Returns the name of the receiver’s suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/islocationrequiredtocreate(forkey:))*