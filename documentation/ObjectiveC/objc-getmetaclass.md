# objc_getMetaClass(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the metaclass definition of a specified class.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func objc_getMetaClass(_ name: UnsafePointer<CChar>) -> Any!
```

#### Return Value

The `Class` object for the metaclass of the named class, or `nil` if the class is not registered with the Objective-C runtime.

#### Discussion

If the definition for the named class is not registered, this function calls the class handler callback and then checks a second time to see if the class is registered. However, every class definition must have a valid metaclass definition, and so the metaclass definition is always returned, whether it’s valid or not.

## Parameters

- `name`: The name of the class to look up.

## See Also

- [func objc_getClassList(AutoreleasingUnsafeMutablePointer<AnyClass>?, Int32) -> Int32](objc_getclasslist(_:_:).md)
  Obtains the list of registered class definitions.
- [func objc_copyClassList(UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<AnyClass>?](objc_copyclasslist(_:).md)
  Creates and returns a list of pointers to all registered class definitions.
- [func objc_lookUpClass(UnsafePointer<CChar>) -> AnyClass?](objc_lookupclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getClass(UnsafePointer<CChar>) -> Any!](objc_getclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getRequiredClass(UnsafePointer<CChar>) -> AnyClass](objc_getrequiredclass(_:).md)
  Returns the class definition of a specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_getmetaclass(_:))*