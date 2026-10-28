# objc_destructInstance

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Destroys an instance of a class without freeing memory and removes any of its associated references.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```c
extern void *objc_destructInstance(id obj);
```

## Discussion

This method does nothing if `obj` is `nil`.

> ❗ **Important**:  The garbage collector does not call this function. As a result, if you edit this function, you should also edit finalize. That said, Core Foundation and other clients do call this function under garbage collection.

## See Also

### Instantiating Classes
- [func class_createInstance(AnyClass?, Int) -> Any?](./class_createinstance%28_,_%29.md)
  Creates an instance of a class, allocating memory for the class in the default malloc memory zone.
- [objc_constructInstance](./objc_constructinstance.md)
  Creates an instance of a class at the specified location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_destructinstance)*