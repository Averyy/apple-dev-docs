# CFTypeID

**Framework**: Core Foundation  
**Kind**: typealias

A type for unique, constant integer values that identify particular Core Foundation opaque types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CFTypeID = UInt
```

#### Discussion

Defines a type identifier in Core Foundation. A type ID is an integer that identifies the opaque type to which a Core Foundation object “belongs.” You use type IDs in various contexts, such as when you are operating on heterogeneous collections. Core Foundation provides programmatic interfaces for obtaining and evaluating type IDs.

Because the value for a type ID can change from release to release, your code should not rely on stored or hard-coded type IDs nor should it hard-code any observed properties of a type ID (such as, for example, it being a small integer).

## See Also

- [typealias CFHashCode](cfhashcode.md)
  A type for hash codes returned by the `CFHash` function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftypeid)*