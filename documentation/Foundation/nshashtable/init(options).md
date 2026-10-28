# init(options:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a hash table with given pointer functions options.

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
init(options: NSPointerFunctions.Options = [])
```

```objc
+ (NSHashTable<id> *) hashTableWithOptions:(NSPointerFunctionsOptions) options;
```

## Return Value

A hash table with given pointer functions options.

## Parameters

- `options`: A bit field that specifies the options for the elements in the hash table. For possible values, see [`NSHashTableOptions`](../nshashtableoptions.md).

## See Also

### Convenience Constructors
- [class func weakObjects() -> NSHashTable<ObjectType>](./weakobjects%28%29.md)
  Returns a new hash table for storing weak references to its contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nshashtable/init(options:))*