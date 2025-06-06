# register(_:for:)

**Framework**: Foundation  
**Kind**: method

Registers an `NSClassDescription` object for a given class in the `NSClassDescription` cache.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func register(_ description: NSClassDescription, for aClass: AnyClass)
```

#### Discussion

You should rarely need to directly invoke this method.

## Parameters

- `description`: The class description to register.
- `aClass`: The class for which to register  .

## See Also

- [init?(for: AnyClass)](nsclassdescription/init(for:).md)
  Returns the class description for a given class.
- [class func invalidateClassDescriptionCache()](nsclassdescription/invalidateclassdescriptioncache.md)
  Removes all `NSClassDescription` objects from the cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription/register(_:for:))*