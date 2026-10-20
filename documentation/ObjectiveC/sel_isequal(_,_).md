# sel_isEqual(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether two selectors are equal.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func sel_isEqual(_ lhs: Selector, _ rhs: Selector) -> Bool
```

```c
extern BOOL sel_isEqual(SEL lhs, SEL rhs);
```

#### Return Value

[`YES`](./yes.md) if `rhs` and `rhs` are equal, otherwise [`NO`](./no.md).

#### Discussion

`sel_isEqual` is equivalent to `==`.

## Parameters

- `lhs`: The selector to compare with `rhs`.
- `rhs`: The selector to compare with `lhs`.

## See Also

### Working with Selectors
- [func sel_getName(Selector) -> UnsafePointer<CChar>](./sel_getname%28_%29.md)
  Returns the name of the method specified by a given selector.
- [func sel_registerName(UnsafePointer<CChar>) -> Selector](./sel_registername%28_%29.md)
  Registers a method with the Objective-C runtime system, maps the method name to a selector, and returns the selector value.
- [func sel_getUid(UnsafePointer<CChar>) -> Selector](./sel_getuid%28_%29.md)
  Registers a method name with the Objective-C runtime system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/sel_isequal(_:_:))*