# superclass

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the class description instance for the superclass of the receiver’s class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var superclass: NSScriptClassDescription? { get }
```

```objc
@property (retain, readonly, nullable) NSScriptClassDescription * superclassDescription;
```

#### Return Value

A class description instance that describes the superclass of the receiver’s class. Returns `nil` if the class has no superclass.

#### Discussion

The instance of `NSScriptClassDescription` that describes the superclass can be in the same suite as the receiver or in a different suite.

## See Also

### Getting a Script Class Description
- [init?(for: AnyClass)](./init%28for%29.md)
  Returns the class description for the specified class or, if it is not scriptable, for the first superclass that is.
- [func forKey(String) -> NSScriptClassDescription?](./forkey%28_%29.md)
  Returns the class description instance for the class type of the specified attribute or relationship.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/superclass)*