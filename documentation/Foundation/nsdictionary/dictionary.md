# dictionary

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates an empty dictionary.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) dictionary;
```

#### Return Value

A new empty dictionary.

#### Discussion

This method is declared primarily for use with mutable subclasses of [`NSDictionary`](../nsdictionary.md).

If you don’t want a temporary object, you can also create an empty dictionary using `alloc` and [`init()`](./init%28%29.md).

## See Also

### Related Documentation
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
- [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i)
### Creating an Empty Dictionary
- [init()](./init%28%29.md)
  Initializes a newly allocated dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/dictionary)*