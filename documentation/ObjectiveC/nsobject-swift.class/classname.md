# className

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

A string containing the name of the class.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var className: String { get }
```

```objc
@property (copy, readonly) NSString * className;
```

## See Also

### Scripting
- [var classCode: FourCharCode](./classcode.md)
  The receiver’s Apple event type code, as stored in the `NSScriptClassDescription` object for the object’s class.
- [func copyScriptingValue(Any, forKey: String, withProperties: [String : Any]) -> Any?](./copyscriptingvalue%28_,forkey,withproperties%29.md)
  Creates and returns one or more scripting objects to be inserted into the specified relationship by copying the passed-in value and setting the properties in the copied object or objects.
- [func newScriptingObject(of: AnyClass, forValueForKey: String, withContentsValue: Any?, properties: [String : Any]) -> Any?](./newscriptingobject%28of,forvalueforkey,withcontentsvalue,properties%29.md)
  Creates and returns an instance of a scriptable class, setting its contents and properties, for insertion into the relationship identified by the key.
- [var scriptingProperties: [String : Any]?](./scriptingproperties.md)
  An `NSString`-keyed dictionary of the receiver’s scriptable properties.
- [func scriptingValue(for: NSScriptObjectSpecifier) -> Any?](./scriptingvalue%28for%29.md)
  Given an object specifier, returns the specified object or objects in the receiving container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/classname)*