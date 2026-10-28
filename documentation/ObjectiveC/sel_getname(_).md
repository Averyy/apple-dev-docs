# sel_getName(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns the name of the method specified by a given selector.

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
func sel_getName(_ sel: Selector) -> UnsafePointer<CChar>
```

```c
extern const char *sel_getName(SEL sel);
```

## Return Value

A C string indicating the name of the selector.

## Parameters

- `sel`: A pointer of type [`SEL`](./sel.md). Pass the selector whose name you wish to determine.

## See Also

### Working with Selectors
- [func sel_registerName(UnsafePointer<CChar>) -> Selector](./sel_registername%28_%29.md)
  Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.
- [func sel_getUid(UnsafePointer<CChar>) -> Selector](./sel_getuid%28_%29.md)
  Registers a method name with the Objective-C runtime system.
- [func sel_isEqual(Selector, Selector) -> Bool](./sel_isequal%28_,_%29.md)
  Returns a Boolean value that indicates whether two selectors are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/sel_getname(_:))*