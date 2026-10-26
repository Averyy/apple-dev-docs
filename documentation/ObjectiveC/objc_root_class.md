# OBJC_ROOT_CLASS

**Framework**: Objective-C Runtime  
**Kind**: macro  
**Role**: Macro

If you define an Objective-C root class, you receive a compiler error indicating that the class is defined without specifying a base class. You can avoid this compiler error by preceding the definition of the root class (that is, before the `@interface` directive) with `OBJC_ROOT_CLASS`.

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
#define OBJC_ROOT_CLASS
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_root_class)*