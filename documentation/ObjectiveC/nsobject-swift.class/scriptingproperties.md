# scriptingProperties

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

An `NSString`-keyed dictionary of the receiver’s scriptable properties.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var scriptingProperties: [String : Any]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,id> * scriptingProperties;
```

#### Discussion

An `NSString`-keyed dictionary of the receiver’s scriptable properties, including all of those that are declared as Attributes and ToOneRelationships in the `.scriptSuite` property list entries for the class and its scripting superclasses, with the exception of ones keyed by “scriptingProperties.” Each key in the dictionary must be identical to the key for an Attribute or ToOneRelationship. The values of the dictionary must be Objective-C objects that are convertible to `NSAppleEventDescriptor` objects.

## See Also

### Scripting
- [var classCode: FourCharCode](./classcode.md)
  The receiver’s Apple event type code, as stored in the `NSScriptClassDescription` object for the object’s class.
- [var className: String](./classname.md)
  A string containing the name of the class.
- [func copyScriptingValue(Any, forKey: String, withProperties: [String : Any]) -> Any?](./copyscriptingvalue%28_,forkey,withproperties%29.md)
  Creates and returns one or more scripting objects to be inserted into the specified relationship by copying the passed-in value and setting the properties in the copied object or objects.
- [func newScriptingObject(of: AnyClass, forValueForKey: String, withContentsValue: Any?, properties: [String : Any]) -> Any?](./newscriptingobject%28of,forvalueforkey,withcontentsvalue,properties%29.md)
  Creates and returns an instance of a scriptable class, setting its contents and properties, for insertion into the relationship identified by the key.
- [func scriptingValue(for: NSScriptObjectSpecifier) -> Any?](./scriptingvalue%28for%29.md)
  Given an object specifier, returns the specified object or objects in the receiving container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/scriptingproperties)*