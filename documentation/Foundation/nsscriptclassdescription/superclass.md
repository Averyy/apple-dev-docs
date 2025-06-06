# superclass

**Framework**: Foundation  
**Kind**: property

Returns the class description instance for the superclass of the receiver’s class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var superclass: NSScriptClassDescription? { get }
```

#### Return Value

A class description instance that describes the superclass of the receiver’s class. Returns `nil` if the class has no superclass.

#### Discussion

The instance of `NSScriptClassDescription` that describes the superclass can be in the same suite as the receiver or in a different suite.

## See Also

- [init?(for: AnyClass)](nsscriptclassdescription/init(for:).md)
  Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.
- [func forKey(String) -> NSScriptClassDescription?](nsscriptclassdescription/forkey(_:).md)
  Returns the class description instance for the class type of the specified attribute or relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/superclass)*