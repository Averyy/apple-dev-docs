# key

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The key that specifies the property to compare during sorting.

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
var key: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * key;
```

## See Also

### Getting Information About a Sort Descriptor
- [var ascending: Bool](./ascending.md)
  A Boolean value that indicates whether the receiver specifies sorting in ascending order.
- [var keyPath: AnyKeyPath?](./keypath.md)
  The key path that specifies the property to compare during sorting.
- [var selector: Selector?](./selector.md)
  The selector for comparing objects.
- [var comparator: Comparator](./comparator.md)
  The comparator for the sort descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/key)*