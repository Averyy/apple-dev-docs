# objc_copyClassList(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Creates and returns a list of pointers to all registered class definitions.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func objc_copyClassList(_ outCount: UnsafeMutablePointer<UInt32>?) -> AutoreleasingUnsafeMutablePointer<AnyClass>?
```

#### Return Value

A `nil` terminated array of classes. You must free the array with `free()`.

## Parameters

- `outCount`: An integer pointer used to store the number of classes returned by this function in the list. This parameter may be  .

## See Also

- [func objc_getClassList(AutoreleasingUnsafeMutablePointer<AnyClass>?, Int32) -> Int32](objc_getclasslist(_:_:).md)
  Obtains the list of registered class definitions.
- [func objc_lookUpClass(UnsafePointer<CChar>) -> AnyClass?](objc_lookupclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getClass(UnsafePointer<CChar>) -> Any!](objc_getclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getRequiredClass(UnsafePointer<CChar>) -> AnyClass](objc_getrequiredclass(_:).md)
  Returns the class definition of a specified class.
- [func objc_getMetaClass(UnsafePointer<CChar>) -> Any!](objc_getmetaclass(_:).md)
  Returns the metaclass definition of a specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_copyclasslist(_:))*