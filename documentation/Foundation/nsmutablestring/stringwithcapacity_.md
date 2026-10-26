# stringWithCapacity:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an empty `NSMutableString` object with initial storage for a given number of characters.

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
+ (NSMutableString *) stringWithCapacity:(NSUInteger) capacity;
```

#### Return Value

An empty `NSMutableString` object with initial storage for `capacity` characters.

#### Discussion

The number of characters indicated by `capacity` is simply a hint to increase the efficiency of data storage. The value does *not* limit the length of the string.

## Parameters

- `capacity`: The number of characters the string is expected to initially contain.

## See Also

### Related Documentation
- [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i)
### Creating and Initializing a Mutable String
- [init(capacity: Int)](./init%28capacity%29.md)
  Returns an `NSMutableString` object initialized with initial storage for a given number of characters,


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutablestring/stringwithcapacity:)*