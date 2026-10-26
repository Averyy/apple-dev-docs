# sortDescriptorWithKey:ascending:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a sort descriptor with the specified key path and ordering.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) sortDescriptorWithKey:(NSString *) key ascending:(BOOL) ascending;
```

#### Return Value

A sort descriptor initialized with the specified key path and sort order, and the default comparison selector ([compare](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/ci_gslang_ext.html#//apple_ref/doc/uid/TP40004397-CH206-BCIECEBI)).

## Parameters

- `key`: The key path to use when performing a comparison.

  For information about key paths, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).
- `ascending`: [`true`](../../Swift/true.md) if the receiver specifies sorting in ascending order, otherwise [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [Sort Descriptor Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SortDescriptors/SortDescriptors.html#//apple_ref/doc/uid/10000174i)
### Creating a Sort Descriptor
- [init(key: String?, ascending: Bool)](./init%28key,ascending%29.md)
  Creates a sort descriptor with a specified string key path and sort order.
- [+ sortDescriptorWithKey:ascending:selector:](./sortdescriptorwithkey_ascending_selector_.md)
  Creates a sort descriptor with the specified key path, ordering, and comparison selector.
- [init(key: String?, ascending: Bool, selector: Selector?)](./init%28key,ascending,selector%29.md)
  Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [+ sortDescriptorWithKey:ascending:comparator:](./sortdescriptorwithkey_ascending_comparator_.md)
  Creates and returns a sort descriptor initialized with the specified key path and ordering, and a comparator block.
- [init(key: String?, ascending: Bool, comparator: Comparator)](./init%28key,ascending,comparator%29.md)
  Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a sort descriptor by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/sortdescriptorwithkey:ascending:)*