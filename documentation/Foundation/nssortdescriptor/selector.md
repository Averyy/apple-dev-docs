# selector

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The selector for comparing objects.

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
var selector: Selector? { get }
```

```objc
@property (readonly, nullable) SEL selector;
```

## See Also

### Getting Information About a Sort Descriptor
- [var ascending: Bool](./ascending.md)
  A Boolean value that indicates whether the receiver specifies sorting in ascending order.
- [var key: String?](./key.md)
  The key that specifies the property to compare during sorting.
- [var keyPath: AnyKeyPath?](./keypath.md)
  The key path that specifies the property to compare during sorting.
- [var comparator: Comparator](./comparator.md)
  The comparator for the sort descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssortdescriptor/selector)*