# init(options:capacity:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a hash table initialized with the given attributes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(options: NSPointerFunctions.Options = [], capacity initialCapacity: Int)
```

```objc
- (instancetype) initWithOptions:(NSPointerFunctionsOptions) options capacity:(NSUInteger) initialCapacity;
```

## Return Value

A hash table initialized with options specified by `options` and initial capacity of `capacity`.

## Parameters

- `options`: A bit field that specifies the options for the elements in the hash table. For possible values, see [`NSHashTableOptions`](../nshashtableoptions.md).
- `initialCapacity`: The initial number of elements the hash table can hold.

## See Also

### Related Documentation
- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)
### Initialization
- [init(pointerFunctions: NSPointerFunctions, capacity: Int)](./init%28pointerfunctions,capacity%29.md)
  Returns a hash table initialized with the given functions and capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/init(options:capacity:))*