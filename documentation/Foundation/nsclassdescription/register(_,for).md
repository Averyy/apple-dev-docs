# register(_:for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Registers an `NSClassDescription` object for a given class in the `NSClassDescription` cache.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func register(_ description: NSClassDescription, for aClass: AnyClass)
```

```objc
+ (void) registerClassDescription:(NSClassDescription *) description forClass:(Class) aClass;
```

#### Discussion

You should rarely need to directly invoke this method.

## Parameters

- `description`: The class description to register.
- `aClass`: The class for which to register `description`.

## See Also

### Working with class descriptions
- [init?(for: AnyClass)](./init%28for%29.md)
  Returns the class description for a given class.
- [class func invalidateClassDescriptionCache()](./invalidateclassdescriptioncache%28%29.md)
  Removes all `NSClassDescription` objects from the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription/register(_:for:))*