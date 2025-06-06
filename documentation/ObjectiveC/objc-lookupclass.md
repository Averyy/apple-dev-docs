# objc_lookUpClass(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the class definition of a specified class.

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
func objc_lookUpClass(_ name: UnsafePointer<CChar>) -> AnyClass?
```

#### Return Value

The Class object for the named class, or `nil` if the class is not registered with the Objective-C runtime.

#### Discussion

The implementation of this function is identical to the implementation of the  [`objc_getClass(_:)`](objc_getclass(_:).md) function.

## Parameters

- `name`: The name of the class to look up.

## See Also

- [func objc_getClassList(AutoreleasingUnsafeMutablePointer<AnyClass>?, Int32) -> Int32](objc_getclasslist(_:_:).md)
  Obtains the list of registered class definitions.
- [func objc_copyClassList(UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<AnyClass>?](objc_copyclasslist(_:).md)
  Creates and returns a list of pointers to all registered class definitions.
- [func objc_getClass(UnsafePointer<CChar>) -> Any!](objc_getclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getRequiredClass(UnsafePointer<CChar>) -> AnyClass](objc_getrequiredclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getMetaClass(UnsafePointer<CChar>) -> Any!](objc_getmetaclass(_:).md)
  Returns the metaclass definition of a specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_lookupclass(_:))*