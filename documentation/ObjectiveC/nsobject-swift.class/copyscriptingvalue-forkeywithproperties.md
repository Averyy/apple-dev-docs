# copyScriptingValue(_:forKey:withProperties:)

**Framework**: Objective-C Runtime  
**Kind**: method

Creates and returns one or more scripting objects to be inserted into the specified relationship by copying the passed-in value and setting the properties in the copied object or objects.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func copyScriptingValue(_ value: Any, forKey key: String, withProperties properties: [String : Any]) -> Any?
```

#### Return Value

The copied object or objects. Returns `nil` if an error occurs.

#### Discussion

You can override the `copyScriptingValue` method to take more control when your application is sent a `duplicate` command. This method is invoked on the prospective container of the copied object or objects. The `properties` are derived from the `with properties` parameter of the `duplicate` command. The returned objects or objects are then inserted into the container using key-value coding.

When this method is invoked by Cocoa, neither the value nor the properties will have yet been coerced using the `NSScriptKeyValueCoding` method [`coerceValue(_:forKey:)`](nsobject-swift.class/coercevalue(_:forkey:).md). For sdef-declared scriptability, however, the types of the passed-in objects reliably match the relevant sdef declarations.

The default implementation of this method copies scripting objects by sending `copyWithZone:` to the object or objects specified by `value`. You override this method for situations where this is not sufficient, such as in Core Data applications, in which new objects must be initialized with `[NSManagedObject initWithEntity:insertIntoManagedObjectContext:]`.

## Parameters

- `value`: For example, if the property is a to-many relationship,   will always be an array of objects to be copied, and this method must therefore return an array of objects.
- `key`: A key that identifies the relationship into which to insert the copied object or objects.
- `properties`: The properties to be set in the copied object or objects.  Derived from the “with properties” parameter of a   command. (See also the Discussion section.)

## See Also

- [var classCode: FourCharCode](nsobject-swift.class/classcode.md)
  The receiver’s Apple event type code, as stored in the `NSScriptClassDescription` object for the object’s class.
- [var className: String](nsobject-swift.class/classname.md)
  A string containing the name of the class.
- [func newScriptingObject(of: AnyClass, forValueForKey: String, withContentsValue: Any?, properties: [String : Any]) -> Any?](nsobject-swift.class/newscriptingobject(of:forvalueforkey:withcontentsvalue:properties:).md)
  Creates and returns an instance of a scriptable class, setting its contents and properties, for insertion into the relationship identified by the key.
- [var scriptingProperties: [String : Any]?](nsobject-swift.class/scriptingproperties.md)
  An `NSString`-keyed dictionary of the receiver’s scriptable properties.
- [func scriptingValue(for: NSScriptObjectSpecifier) -> Any?](nsobject-swift.class/scriptingvalue(for:).md)
  Given an object specifier, returns the specified object or objects in the receiving container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/copyscriptingvalue(_:forkey:withproperties:))*