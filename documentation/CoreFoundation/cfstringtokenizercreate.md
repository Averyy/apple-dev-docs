# CFStringTokenizerCreate(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a tokenizer for a given string.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFStringTokenizerCreate(_ alloc: CFAllocator!, _ string: CFString!, _ range: CFRange, _ options: CFOptionFlags, _ locale: CFLocale!) -> CFStringTokenizer!
```

#### Return Value

A tokenizer to analyze the range `range` of `string` for the given locale and options. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or   to use the current default allocator.
- `string`: The string to tokenize.
- `range`: The range of the characters in   to tokenize.
- `options`: A tokenization unit option that specifies how   should be tokenized. The options can be modified by adding unit modifier options to tell the tokenizer to prepare specified attributes when it tokenizes  .   For possible values, see  .
- `locale`: A locale that specifies language- or region-specific behavior for the tokenization. You can pass   to use the default system locale, although this is typically not recommended—instead use   to specify the locale of the current user.   For more information, see  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringtokenizercreate(_:_:_:_:_:))*