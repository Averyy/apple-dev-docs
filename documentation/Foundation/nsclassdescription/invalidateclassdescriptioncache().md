# invalidateClassDescriptionCache()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Removes all `NSClassDescription` objects from the cache.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func invalidateClassDescriptionCache()
```

```objc
+ (void) invalidateClassDescriptionCache;
```

#### Discussion

You should rarely need to invoke this method. Use it whenever a registered `NSClassDescription` object might be replaced by a different version, such as when you have loaded a new provider of `NSClassDescription` objects, or when you are about to remove a provider of `NSClassDescription` objects.

## See Also

### Working with class descriptions
- [init?(for: AnyClass)](./init%28for%29.md)
  Returns the class description for a given class.
- [class func register(NSClassDescription, for: AnyClass)](./register%28_,for%29.md)
  Registers an `NSClassDescription` object for a given class in the `NSClassDescription` cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription/invalidateclassdescriptioncache())*