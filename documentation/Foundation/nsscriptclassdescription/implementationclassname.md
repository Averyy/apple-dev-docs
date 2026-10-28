# implementationClassName

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the name of the Objective-C class instantiated to implement the scripting class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var implementationClassName: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * implementationClassName;
```

## Return Value

An Objective-C class name.

## Discussion

The name returned by the [`className`](./classname.md) method for an instance of `NSScriptClassDescription` resulting from an sdef class declaration is the human-readable name for the class—that is, the name that is used in a script. To obtain the name of the Objective-C class instantiated to implement the class, use `implementationClassName`.

## See Also

### Getting basic information about the script class
- [var className: String?](./classname.md)
  Returns the name of the class the receiver describes, as provided at initialization time.
- [var defaultSubcontainerAttributeKey: String?](./defaultsubcontainerattributekey.md)
  Returns the value of the `DefaultSubcontainerAttribute` entry of the class dictionary from which the receiver was instantiated.
- [func isLocationRequiredToCreate(forKey: String) -> Bool](./islocationrequiredtocreate%28forkey%29.md)
  Returns a Boolean value indicating whether an insertion location must be specified when creating a new object in the specified to-many relationship of the receiver.
- [var suiteName: String?](./suitename.md)
  Returns the name of the receiver’s suite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/implementationclassname)*