# init(key:ascending:comparator:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a sort descriptor with a specified string key path and ordering, and a comparator block.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(key: String?, ascending: Bool, comparator cmptr: @escaping Comparator)
```

```objc
- (instancetype) initWithKey:(NSString *) key ascending:(BOOL) ascending comparator:(NSComparator) cmptr;
```

## Return Value

A sort descriptor that initializes with the specified key, ordering, and comparator.

## Parameters

- `key`: The property key for performing a comparison.

  For information about key paths, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).
- `ascending`: [`true`](../../Swift/true.md) if the receiver specifies sorting in ascending order; otherwise, [`false`](../../Swift/false.md).
- `cmptr`: A comparator block.

## See Also

### Creating a Sort Descriptor
- [init(key: String?, ascending: Bool)](./init%28key,ascending%29.md)
  Creates a sort descriptor with a specified string key path and sort order.
- [init(key: String?, ascending: Bool, selector: Selector?)](./init%28key,ascending,selector%29.md)
  Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool)](./init%28keypath,ascending%29.md)
  Creates a sort descriptor with a specified key path and ordering.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool, comparator: Comparator)](./init%28keypath,ascending,comparator%29.md)
  Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a sort descriptor by decoding from the coder you specify.
- [convenience init<Compared>(SortDescriptor<Compared>)](./init%28_%29-7qf91.md)
  Creates a sort descriptor using a sort descriptor you specify.
- [+ sortDescriptorWithKey:ascending:](./sortdescriptorwithkey_ascending_.md)
  Creates and returns a sort descriptor with the specified key path and ordering.
- [+ sortDescriptorWithKey:ascending:selector:](./sortdescriptorwithkey_ascending_selector_.md)
  Creates a sort descriptor with the specified key path, ordering, and comparison selector.
- [+ sortDescriptorWithKey:ascending:comparator:](./sortdescriptorwithkey_ascending_comparator_.md)
  Creates and returns a sort descriptor initialized with the specified key path and ordering, and a comparator block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/init(key:ascending:comparator:))*