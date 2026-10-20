# scriptingValue(for:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Given an object specifier, returns the specified object or objects in the receiving container.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func scriptingValue(for objectSpecifier: NSScriptObjectSpecifier) -> Any?
```

```objc
- (id) scriptingValueForSpecifier:(NSScriptObjectSpecifier *) objectSpecifier;
```

#### Return Value

The specified object or objects in the receiving container.

#### Discussion

This method might successfully return an object, an array of objects, or `nil`, depending on the kind of object specifier. Because `nil` is a valid return value, failure is signaled by invoking the object specifier’s `setEvaluationError:` method before returning.

#### Discussion

You can override this method to customize the evaluation of object specifiers without requiring that the scripting container make up indexes for contained objects that don’t naturally have indexes (as can be the case if you implement [`indicesOfObjects(byEvaluatingObjectSpecifier:)`](./indicesofobjects%28byevaluatingobjectspecifier%29.md) instead).

Your override of this method doesn’t need to also invoke any of the `NSScriptCommand` error signaling methods, though it can, to record very specific information. The `NSUnknownKeySpecifierError` and `NSInvalidIndexSpecifierError` numbers are special, in that Cocoa may continue evaluating an outer specifier if they’re encountered, for the convenience of scripters.

## Parameters

- `objectSpecifier`: An object specifier to be evaluated.

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
- [var scriptingProperties: [String : Any]?](./scriptingproperties.md)
  An `NSString`-keyed dictionary of the receiver’s scriptable properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/scriptingvalue(for:))*