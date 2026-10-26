# init(coder:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a sort descriptor by decoding from the coder you specify.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## Parameters

- `coder`: The coder to read data from.

## See Also

### Creating a Sort Descriptor
- [init(key: String?, ascending: Bool)](./init%28key,ascending%29.md)
  Creates a sort descriptor with a specified string key path and sort order.
- [init(key: String?, ascending: Bool, selector: Selector?)](./init%28key,ascending,selector%29.md)
  Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool)](./init%28keypath,ascending%29.md)
  Creates a sort descriptor with a specified key path and ordering.
- [init(key: String?, ascending: Bool, comparator: Comparator)](./init%28key,ascending,comparator%29.md)
  Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [convenience init<Root, Value>(keyPath: KeyPath<Root, Value>, ascending: Bool, comparator: Comparator)](./init%28keypath,ascending,comparator%29.md)
  Creates a sort descriptor with a specified key path and ordering, and a comparator block.
- [convenience init<Compared>(SortDescriptor<Compared>)](./init%28_%29-7qf91.md)
  Creates a sort descriptor using a sort descriptor you specify.
- [+ sortDescriptorWithKey:ascending:](./sortdescriptorwithkey_ascending_.md)
  Creates and returns a sort descriptor with the specified key path and ordering.
- [+ sortDescriptorWithKey:ascending:selector:](./sortdescriptorwithkey_ascending_selector_.md)
  Creates a sort descriptor with the specified key path, ordering, and comparison selector.
- [+ sortDescriptorWithKey:ascending:comparator:](./sortdescriptorwithkey_ascending_comparator_.md)
  Creates and returns a sort descriptor initialized with the specified key path and ordering, and a comparator block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/init(coder:))*