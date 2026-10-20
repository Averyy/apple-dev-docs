# sel_registerName(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.

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
func sel_registerName(_ str: UnsafePointer<CChar>) -> Selector
```

```c
extern SELsel_registerName(const char *str);
```

#### Return Value

A pointer of type [`SEL`](./sel.md) specifying the selector for the named method.

#### Discussion

You must register a method name with the Objective-C runtime system to obtain the method’s selector before you can add the method to a class definition. If the method name has already been registered, this function simply returns the selector.

## Parameters

- `str`: A pointer to a C string. Pass the name of the method you wish to register.

## See Also

### Working with Selectors
- [func sel_getName(Selector) -> UnsafePointer<CChar>](./sel_getname%28_%29.md)
  Returns the name of the method specified by a given selector.
- [func sel_getUid(UnsafePointer<CChar>) -> Selector](./sel_getuid%28_%29.md)
  Registers a method name with the Objective-C runtime system.
- [func sel_isEqual(Selector, Selector) -> Bool](./sel_isequal%28_,_%29.md)
  Returns a Boolean value that indicates whether two selectors are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/sel_registername(_:))*