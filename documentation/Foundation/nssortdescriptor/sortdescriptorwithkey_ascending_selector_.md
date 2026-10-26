# sortDescriptorWithKey:ascending:selector:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a sort descriptor with the specified key path, ordering, and comparison selector.

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
+ (instancetype) sortDescriptorWithKey:(NSString *) key ascending:(BOOL) ascending selector:(SEL) selector;
```

#### Return Value

A sort descriptor that initializes with the specified key path, sort order, and comparison selector.

## Parameters

- `key`: The key path for performing a comparison.

  For information about key paths, see [Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i).
- `ascending`: [`true`](../../Swift/true.md) if the receiver specifies sorting in ascending order; otherwise, [`false`](../../Swift/false.md).
- `selector`: The method to use when comparing the properties of objects, for example [`localizedStandardCompare(_:)`](../nsstring/localizedstandardcompare%28_%29.md). The selector must specify a method implemented by the value of the property identified by the key path. The selector used for the comparison is passed a single parameter, the object to compare against, and it returns the appropriate [`ComparisonResult`](../comparisonresult.md) constant.

## See Also

### Creating a Sort Descriptor
- [+ sortDescriptorWithKey:ascending:](./sortdescriptorwithkey_ascending_.md)
  Creates and returns a sort descriptor with the specified key path and ordering.
- [init(key: String?, ascending: Bool)](./init%28key,ascending%29.md)
  Creates a sort descriptor with a specified string key path and sort order.
- [init(key: String?, ascending: Bool, selector: Selector?)](./init%28key,ascending,selector%29.md)
  Creates a sort descriptor with a specified string key path, ordering, and comparison selector.
- [+ sortDescriptorWithKey:ascending:comparator:](./sortdescriptorwithkey_ascending_comparator_.md)
  Creates and returns a sort descriptor initialized with the specified key path and ordering, and a comparator block.
- [init(key: String?, ascending: Bool, comparator: Comparator)](./init%28key,ascending,comparator%29.md)
  Creates a sort descriptor with a specified string key path and ordering, and a comparator block.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a sort descriptor by decoding from the coder you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/sortdescriptorwithkey:ascending:selector:)*