# init(for:)

**Framework**: Foundation  
**Kind**: init

Returns the class description for a given class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
init?(for aClass: AnyClass)
```

#### Return Value

The class description for `aClass`, or `nil` if a class description cannot be found.

#### Discussion

If a class description for `aClass` is not found, the method posts an NSClassDescriptionNeededForClassNotification on behalf of `aClass`, allowing an observer to register a class description. The method then checks for a class description again. Returns `nil` if a class description is still not found.

If you have an instance of the receiver’s class, you can use the `NSObject` instance method [`classDescription`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/classDescription) instead.

> **Note**:  In macOS 10.6 and later, this method (and as a result [`classDescription`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/classDescription) methods of any object) will return `nil` when the sdef contains no `<class>` element for the Cocoa class, but there is a `<class>` element defined for a superclass. This is incorrect, as object instances should never be required to be exactly a given class, any class should be allowed to be a subclass of the required class and receive the correct `<class>` value. This situation can have a serious impact on Cocoa Scripting, and there is no plan on changing this behavior. Instead of using this method, you should use the [`init(for:)`](nsscriptclassdescription/init(for:).md) method of [`NSScriptClassDescription`](nsscriptclassdescription.md) instead.

## Parameters

- `aClass`: The class for which to return a class description. See note below for important details.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)
- [class func invalidateClassDescriptionCache()](nsclassdescription/invalidateclassdescriptioncache.md)
  Removes all `NSClassDescription` objects from the cache.
- [class func register(NSClassDescription, for: AnyClass)](nsclassdescription/register(_:for:).md)
  Registers an `NSClassDescription` object for a given class in the `NSClassDescription` cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription/init(for:))*