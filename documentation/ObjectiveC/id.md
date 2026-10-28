# id

**Framework**: Objective-C Runtime  
**Kind**: typealias  
**Role**: Type Alias

A pointer to an instance of a class.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef struct objc_object * id;
```

## Discussion

When you create an instance of a particular class, the allocated memory contains an `objc_object` data structure, which is directly followed by the data for the instance variables of the class.

The `alloc` and `allocWithZone:` methods of the Foundation framework class NSObject use the function [`class_createInstance(_:_:)`](./class_createinstance%28_,_%29.md) to create `objc_object` data structures.

## See Also

### Instance Data Types
- [struct objc_object](./objc_object.md)
  Represents an instance of a class.
- [struct objc_super](./objc_super-swift.struct.md)
  Specifies the superclass of an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/id)*